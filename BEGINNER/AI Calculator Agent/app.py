from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime
import re

load_dotenv()

app = Flask(__name__)
CORS(app)

OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
OPENROUTER_API_URL = 'https://openrouter.ai/api/v1/chat/completions'


calculation_memory = []

def extract_math_expression(text):
    """Extract mathematical expressions from text"""
    patterns = [
        r'(\d+\.?\d*)\s*([\+\-\*\/\^])\s*(\d+\.?\d*)',
        r'sqrt\((\d+\.?\d*)\)',
        r'(\d+\.?\d*)\s*\*\*\s*(\d+\.?\d*)',
    ]

    for pattern in patterns:
        match = re.search(pattern, text.lower())
        if match:
            return match.group(0)
    return None

def calculate_with_ai(query):
    """Send calculation request to OpenRouter API"""

    system_prompt = """You are an advanced AI Calculator Agent. Your capabilities include:

1. **Math Operations**: Perform basic arithmetic (add, subtract, multiply, divide) and advanced operations (power, square root, trigonometry, logarithms)
2. **Natural Language Understanding**: Parse math queries from natural language
3. **Structured Output**: Always respond in JSON format

Response Format:
{
    "expression": "the mathematical expression",
    "result": numeric_result,
    "steps": ["step 1", "step 2", ...],
    "explanation": "brief explanation"
}

Examples:
- "What is 25 + 37?" → {"expression": "25 + 37", "result": 62, "steps": ["25 + 37 = 62"], "explanation": "Addition of 25 and 37"}
- "Calculate square root of 144" → {"expression": "√144", "result": 12, "steps": ["√144 = 12"], "explanation": "Square root of 144"}
- "15 times 8" → {"expression": "15 × 8", "result": 120, "steps": ["15 × 8 = 120"], "explanation": "Multiplication of 15 and 8"}

Always provide accurate calculations and clear explanations."""

    headers = {
        'Authorization': f'Bearer {OPENROUTER_API_KEY}',
        'Content-Type': 'application/json',
        'HTTP-Referer': 'http://localhost:5000',
        'X-Title': 'AI Calculator Agent'
    }

    memory_context = ""
    if calculation_memory:
        recent_calcs = calculation_memory[-5:]
        memory_context = "\n\nRecent calculations:\n" + "\n".join([
            f"- {calc['query']}: {calc['result']}"
            for calc in recent_calcs
        ])

    data = {
        'model': 'meta-llama/llama-3-8b-instruct',
        'messages': [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': f"{query}{memory_context}"}
        ],
        'temperature': 0.1,
        'max_tokens': 1000
    }

    try:
        print(f"DEBUG - API Key (first 20 chars): {OPENROUTER_API_KEY[:20] if OPENROUTER_API_KEY else 'None'}")
        print(f"DEBUG - Model: {data['model']}")
        print(f"DEBUG - URL: {OPENROUTER_API_URL}")
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=data, timeout=30)
        print(f"DEBUG - Response status: {response.status_code}")
        response.raise_for_status()

        result = response.json()
        ai_response = result['choices'][0]['message']['content']

        try:
            json_match = re.search(r'\{.*\}', ai_response, re.DOTALL)
            if json_match:
                parsed_result = json.loads(json_match.group(0))
            else:
                parsed_result = json.loads(ai_response)

            return {
                'success': True,
                'data': parsed_result
            }
        except json.JSONDecodeError:
            return {
                'success': True,
                'data': {
                    'expression': query,
                    'result': ai_response,
                    'steps': ['AI processed the query'],
                    'explanation': ai_response
                }
            }

    except requests.exceptions.RequestException as e:
        return {
            'success': False,
            'error': f'API Error: {str(e)}'
        }
    except Exception as e:
        return {
            'success': False,
            'error': f'Error: {str(e)}'
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    query = data.get('query', '').strip()

    if not query:
        return jsonify({'success': False, 'error': 'Query is required'}), 400

    if not OPENROUTER_API_KEY:
        return jsonify({'success': False, 'error': 'OpenRouter API key not configured'}), 500

    result = calculate_with_ai(query)

    if result['success']:
        calculation_entry = {
            'id': len(calculation_memory) + 1,
            'query': query,
            'result': result['data'].get('result', 'N/A'),
            'expression': result['data'].get('expression', query),
            'steps': result['data'].get('steps', []),
            'explanation': result['data'].get('explanation', ''),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        calculation_memory.append(calculation_entry)

        result['data']['id'] = calculation_entry['id']
        result['data']['timestamp'] = calculation_entry['timestamp']

    return jsonify(result)

@app.route('/memory', methods=['GET'])
def get_memory():
    return jsonify({
        'success': True,
        'memory': calculation_memory
    })

@app.route('/memory/clear', methods=['POST'])
def clear_memory():
    calculation_memory.clear()
    return jsonify({
        'success': True,
        'message': 'Memory cleared'
    })

@app.route('/memory/<int:calc_id>', methods=['DELETE'])
def delete_memory_item(calc_id):
    global calculation_memory
    calculation_memory = [calc for calc in calculation_memory if calc['id'] != calc_id]
    return jsonify({
        'success': True,
        'message': f'Calculation {calc_id} deleted'
    })

if __name__ == '__main__':
    print("=" * 50)
    print("AI Calculator Agent Starting...")
    print("=" * 50)
    print(f"OpenRouter API configured: {'YES' if OPENROUTER_API_KEY else 'NO'}")
    print(f"Server running at: http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, port=5000)
