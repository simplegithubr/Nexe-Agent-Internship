"""
Web UI for Tool-Calling Agent
==============================
Flask-based web interface for the agent
"""

from flask import Flask, render_template, request, jsonify
from agent import ToolCallingAgent
import os

app = Flask(__name__)
agent = ToolCallingAgent()

# Enable CORS for development
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
    return response


@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')


@app.route('/api/tools', methods=['GET'])
def get_tools():
    """Get list of available tools"""
    tools = agent.get_available_tools()
    tool_info = agent.get_tool_info()

    return jsonify({
        "success": True,
        "tools": tools,
        "tool_info": tool_info
    })


@app.route('/api/call', methods=['POST'])
def call_tool():
    """Call a specific tool"""
    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "success": False,
                "error": "No data provided"
            }), 400

        tool_name = data.get('tool')
        params = data.get('params', {})

        if not tool_name:
            return jsonify({
                "success": False,
                "error": "Tool name is required"
            }), 400

        # Call the tool
        result = agent.call_tool(tool_name, **params)

        return jsonify(result)

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e),
            "error_type": type(e).__name__
        }), 500


@app.route('/api/calculator', methods=['POST'])
def calculator():
    """Calculator endpoint"""
    data = request.get_json()
    result = agent.call_tool(
        "calculator",
        operation=data.get('operation'),
        num1=float(data.get('num1', 0)),
        num2=float(data.get('num2', 0))
    )
    return jsonify(result)


@app.route('/api/time', methods=['GET'])
def get_time():
    """Get current time"""
    result = agent.call_tool("get_time")
    return jsonify(result)


@app.route('/api/weather', methods=['POST'])
def get_weather():
    """Get weather for a city"""
    data = request.get_json()
    result = agent.call_tool("weather", city=data.get('city', ''))
    return jsonify(result)


@app.route('/api/analyze', methods=['POST'])
def analyze_text():
    """Analyze text"""
    data = request.get_json()
    result = agent.call_tool("text_analyzer", text=data.get('text', ''))
    return jsonify(result)


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "agent": "Tool-Calling AI Agent",
        "version": "1.0.0"
    })


if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Tool-Calling Agent Web UI")
    print("="*60)
    print("\n📍 Server starting at: http://localhost:5000")
    print("📋 Available tools:", ", ".join(agent.get_available_tools()))
    print("\n" + "="*60 + "\n")

    app.run(debug=True, host='0.0.0.0', port=5000)
