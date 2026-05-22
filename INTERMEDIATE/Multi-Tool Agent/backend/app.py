from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
import os

from database.db import Database
from agents.web_search_agent import WebSearchAgent
from agents.email_agent import EmailAgent
from agents.openrouter_agent import OpenRouterAgent

load_dotenv()

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

db = Database()
search_agent = WebSearchAgent()
email_agent = EmailAgent()

try:
    openrouter_agent = OpenRouterAgent()
except ValueError as e:
    print(f"Warning: OpenRouter agent not initialized - {e}")
    openrouter_agent = None

@app.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'services': {
            'database': True,
            'search': True,
            'email': bool(os.getenv('SMTP_USER')),
            'openrouter': openrouter_agent is not None
        }
    })

@app.route('/api/search', methods=['POST'])
def search():
    data = request.json
    query = data.get('query')
    max_results = data.get('max_results', 5)
    search_type = data.get('type', 'web')

    if not query:
        return jsonify({'error': 'Query is required'}), 400

    if search_type == 'news':
        results = search_agent.search_news(query, max_results)
    else:
        results = search_agent.search(query, max_results)

    search_id = db.save_search(query, results)

    return jsonify({
        'search_id': search_id,
        'query': query,
        'results': results,
        'count': len(results)
    })

@app.route('/api/save', methods=['POST'])
def save_data():
    data = request.json
    title = data.get('title')
    content = data.get('content')
    category = data.get('category', 'general')
    metadata = data.get('metadata')

    if not title or not content:
        return jsonify({'error': 'Title and content are required'}), 400

    data_id = db.save_data(title, content, category, metadata)

    return jsonify({
        'success': True,
        'data_id': data_id,
        'message': 'Data saved successfully'
    })

@app.route('/api/data', methods=['GET'])
def get_data():
    category = request.args.get('category')
    limit = int(request.args.get('limit', 100))

    data = db.get_all_data(category, limit)

    return jsonify({
        'count': len(data),
        'data': data
    })

@app.route('/api/email', methods=['POST'])
def send_email():
    data = request.json
    recipient = data.get('recipient')
    subject = data.get('subject')
    body = data.get('body')
    html = data.get('html', False)

    if not all([recipient, subject, body]):
        return jsonify({'error': 'Recipient, subject, and body are required'}), 400

    result = email_agent.send_email(recipient, subject, body, html)

    status = 'sent' if result['success'] else 'failed'
    db.save_email_log(recipient, subject, body, status)

    return jsonify(result)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    if not openrouter_agent:
        return jsonify({
            'error': 'OpenRouter agent not configured. Please set OPENROUTER_API_KEY in .env file'
        }), 503

    data = request.json
    prompt = data.get('prompt')
    model = data.get('model', 'google/gemini-flash-1.5')
    system_prompt = data.get('system_prompt')

    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    result = openrouter_agent.analyze(prompt, model, system_prompt)

    if result['success']:
        db.save_analysis(prompt, result['result'], model)

    return jsonify(result)

@app.route('/api/search-and-analyze', methods=['POST'])
def search_and_analyze():
    if not openrouter_agent:
        return jsonify({
            'error': 'OpenRouter agent not configured'
        }), 503

    data = request.json
    query = data.get('query')
    max_results = data.get('max_results', 5)

    if not query:
        return jsonify({'error': 'Query is required'}), 400

    search_results = search_agent.search(query, max_results)
    analysis = openrouter_agent.summarize_search_results(query, search_results)

    search_id = db.save_search(query, search_results)
    if analysis['success']:
        db.save_analysis(query, analysis['result'], analysis.get('model', 'unknown'))

    return jsonify({
        'search_id': search_id,
        'query': query,
        'search_results': search_results,
        'analysis': analysis
    })

@app.route('/api/history/searches', methods=['GET'])
def get_search_history():
    limit = int(request.args.get('limit', 10))
    searches = db.get_recent_searches(limit)
    return jsonify({'searches': searches})

if __name__ == '__main__':
    print("🚀 Multi-Tool Agent Server Starting...")
    print(f"📊 Database: {os.getenv('DATABASE_PATH', './database/agent_data.db')}")
    print(f"🔍 Search: Enabled (DuckDuckGo)")
    print(f"📧 Email: {'Enabled' if os.getenv('SMTP_USER') else 'Not configured'}")
    print(f"🤖 OpenRouter: {'Enabled' if openrouter_agent else 'Not configured'}")
    port = int(os.getenv('PORT', 7860))
    print(f"\n🌐 Server running on port: {port}")

    app.run(debug=False, host='0.0.0.0', port=port)
