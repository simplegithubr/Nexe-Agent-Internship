"""
Advanced Example: AI-Powered Tool Selection
============================================
Yeh example dikhata hai ke kaise AI agent automatically decide kar sakta hai
ke konsa tool use karna hai based on user ki natural language query.

Note: Yeh example structure dikhata hai. Real implementation ke liye
OpenAI ya Anthropic API key chahiye.
"""

from agent import ToolCallingAgent
import json


class SmartAgent:
    """
    AI-powered agent jo automatically tool select karta hai
    """

    def __init__(self):
        self.tool_agent = ToolCallingAgent()
        self.conversation_history = []

    def get_tool_descriptions(self):
        """Tools ki descriptions AI ke liye format karo"""
        return {
            "calculator": {
                "description": "Performs mathematical operations (add, subtract, multiply, divide)",
                "parameters": {
                    "operation": "string (add/subtract/multiply/divide)",
                    "num1": "number",
                    "num2": "number"
                },
                "example": "Calculate 5 + 3"
            },
            "get_time": {
                "description": "Returns current date, time, and day",
                "parameters": {},
                "example": "What time is it?"
            },
            "weather": {
                "description": "Returns weather information for a city",
                "parameters": {
                    "city": "string (Karachi/Lahore/Islamabad/London/New York)"
                },
                "example": "What's the weather in Karachi?"
            },
            "text_analyzer": {
                "description": "Analyzes text and returns statistics",
                "parameters": {
                    "text": "string"
                },
                "example": "Analyze this text: Hello World"
            }
        }

    def parse_user_intent(self, user_query: str):
        """
        User ki query ko analyze karke tool aur parameters extract karo

        Real implementation mein yahan AI API call hogi (OpenAI/Claude)
        Abhi ke liye simple rule-based parsing hai
        """
        query_lower = user_query.lower()

        # Calculator detection
        math_keywords = ["calculate", "add", "subtract", "multiply", "divide", "plus", "minus", "times"]
        if any(keyword in query_lower for keyword in math_keywords):
            return self._parse_math_query(user_query)

        # Time detection
        time_keywords = ["time", "date", "today", "day", "clock"]
        if any(keyword in query_lower for keyword in time_keywords):
            return {
                "tool": "get_time",
                "parameters": {},
                "confidence": 0.95
            }

        # Weather detection
        weather_keywords = ["weather", "temperature", "forecast", "climate"]
        if any(keyword in query_lower for keyword in weather_keywords):
            return self._parse_weather_query(user_query)

        # Text analysis detection
        analyze_keywords = ["analyze", "count words", "count characters", "text statistics"]
        if any(keyword in query_lower for keyword in analyze_keywords):
            return self._parse_text_query(user_query)

        return {
            "tool": None,
            "error": "Could not understand the query",
            "confidence": 0.0
        }

    def _parse_math_query(self, query: str):
        """Math query se operation aur numbers extract karo"""
        query_lower = query.lower()

        # Operation detect karo
        operation = None
        if "add" in query_lower or "plus" in query_lower or "+" in query:
            operation = "add"
        elif "subtract" in query_lower or "minus" in query_lower or "-" in query:
            operation = "subtract"
        elif "multiply" in query_lower or "times" in query_lower or "*" in query:
            operation = "multiply"
        elif "divide" in query_lower or "/" in query:
            operation = "divide"

        # Numbers extract karo (simple approach)
        import re
        numbers = re.findall(r'-?\d+\.?\d*', query)

        if operation and len(numbers) >= 2:
            return {
                "tool": "calculator",
                "parameters": {
                    "operation": operation,
                    "num1": float(numbers[0]),
                    "num2": float(numbers[1])
                },
                "confidence": 0.9
            }

        return {
            "tool": "calculator",
            "error": "Could not extract numbers from query",
            "confidence": 0.3
        }

    def _parse_weather_query(self, query: str):
        """Weather query se city extract karo"""
        cities = ["karachi", "lahore", "islamabad", "london", "new york"]
        query_lower = query.lower()

        for city in cities:
            if city in query_lower:
                return {
                    "tool": "weather",
                    "parameters": {
                        "city": city.title()
                    },
                    "confidence": 0.9
                }

        return {
            "tool": "weather",
            "error": "Could not identify city in query",
            "confidence": 0.4
        }

    def _parse_text_query(self, query: str):
        """Text analysis query se text extract karo"""
        # Simple approach: text after "analyze" keyword
        if "analyze" in query.lower():
            parts = query.split("analyze", 1)
            if len(parts) > 1:
                text = parts[1].strip().strip('"').strip("'")
                if text:
                    return {
                        "tool": "text_analyzer",
                        "parameters": {
                            "text": text
                        },
                        "confidence": 0.85
                    }

        return {
            "tool": "text_analyzer",
            "error": "Could not extract text to analyze",
            "confidence": 0.3
        }

    def process_query(self, user_query: str):
        """
        User ki query ko process karke appropriate tool call karo
        """
        print(f"\n🤔 User Query: {user_query}")
        print("-" * 60)

        # Intent parse karo
        intent = self.parse_user_intent(user_query)

        if intent.get("tool") is None:
            return {
                "success": False,
                "error": intent.get("error", "Unknown error"),
                "query": user_query
            }

        print(f"🎯 Detected Tool: {intent['tool']}")
        print(f"📊 Confidence: {intent['confidence']*100:.1f}%")

        if "error" in intent:
            print(f"⚠️  Warning: {intent['error']}")
            return {
                "success": False,
                "error": intent["error"],
                "query": user_query
            }

        # Tool call karo
        print(f"🔧 Parameters: {json.dumps(intent['parameters'], indent=2)}")

        result = self.tool_agent.call_tool(
            intent["tool"],
            **intent["parameters"]
        )

        # History mein save karo
        self.conversation_history.append({
            "query": user_query,
            "intent": intent,
            "result": result
        })

        return result


def demo_smart_agent():
    """Smart agent ko test karo"""
    print("=" * 60)
    print("Smart AI Agent - Natural Language Tool Selection")
    print("=" * 60)

    agent = SmartAgent()

    # Test queries
    queries = [
        "What's 25 plus 17?",
        "Calculate 100 divided by 4",
        "What time is it?",
        "What's the weather in Lahore?",
        "Analyze this text: Hello World! How are you?",
        "Multiply 7 times 8",
        "Check weather in London",
        "What day is today?"
    ]

    for query in queries:
        result = agent.process_query(query)

        if result["success"]:
            print(f"✅ Result: {json.dumps(result, indent=2)}")
        else:
            print(f"❌ Error: {result.get('error', 'Unknown error')}")

        print("\n" + "=" * 60 + "\n")


def interactive_smart_agent():
    """Interactive mode for smart agent"""
    print("\n" + "=" * 60)
    print("Interactive Smart Agent")
    print("=" * 60)
    print("\nExamples:")
    print("  • What's 5 plus 3?")
    print("  • What time is it?")
    print("  • Weather in Karachi?")
    print("  • Analyze this text: Your text here")
    print("  • Type 'quit' to exit")
    print("=" * 60)

    agent = SmartAgent()

    while True:
        try:
            query = input("\n💬 You: ").strip()

            if query.lower() in ["quit", "exit", "bye"]:
                print("👋 Goodbye!")
                break

            if not query:
                continue

            result = agent.process_query(query)

            if result["success"]:
                # Format output based on tool
                tool_name = result.get("tool_name", "")

                if tool_name == "calculator":
                    print(f"🤖 Agent: The answer is {result['result']}")

                elif tool_name == "get_time":
                    print(f"🤖 Agent: It's {result['time']} on {result['date']} ({result['day']})")

                elif tool_name == "weather":
                    print(f"🤖 Agent: In {result['city']}, it's {result['temperature']}°C and {result['condition']}")

                elif tool_name == "text_analyzer":
                    print(f"🤖 Agent: That text has {result['word_count']} words and {result['character_count']} characters")

            else:
                print(f"🤖 Agent: Sorry, I couldn't process that. {result.get('error', '')}")

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


def ai_integration_guide():
    """
    Real AI integration ke liye guide
    """
    print("\n" + "=" * 60)
    print("How to Integrate Real AI (OpenAI/Claude)")
    print("=" * 60)

    guide = """

    STEP 1: Install Required Libraries
    -----------------------------------
    pip install openai anthropic


    STEP 2: Get API Key
    -----------------------------------
    OpenAI: https://platform.openai.com/api-keys
    Anthropic: https://console.anthropic.com/


    STEP 3: Replace parse_user_intent() with AI Call
    -----------------------------------

    # Example with OpenAI:
    import openai

    def parse_user_intent_with_ai(self, user_query):
        tools_description = self.get_tool_descriptions()

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"You are a tool selector. Available tools: {tools_description}"},
                {"role": "user", "content": f"Which tool should I use for: {user_query}"}
            ],
            functions=[...],  # Define tools as functions
            function_call="auto"
        )

        return response


    # Example with Claude:
    import anthropic

    def parse_user_intent_with_claude(self, user_query):
        client = anthropic.Anthropic(api_key="your-key")

        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            tools=[...],  # Define your tools
            messages=[
                {"role": "user", "content": user_query}
            ]
        )

        return response


    STEP 4: Benefits of Real AI Integration
    -----------------------------------
    ✅ Better natural language understanding
    ✅ Handles complex queries
    ✅ Multi-step reasoning
    ✅ Context awareness
    ✅ Handles ambiguity better


    STEP 5: Cost Considerations
    -----------------------------------
    • OpenAI GPT-4: ~$0.03 per 1K tokens
    • Claude Sonnet: ~$0.003 per 1K tokens
    • Use caching to reduce costs
    • Implement rate limiting
    """

    print(guide)


def main():
    """Main function"""
    print("\n" + "🚀" * 30)
    print("Advanced Tool-Calling Agent Examples")
    print("🚀" * 30)

    # Demo
    demo_smart_agent()

    # AI Integration Guide
    ai_integration_guide()

    # Interactive mode
    response = input("\n🎮 Try interactive mode? (yes/no): ").strip().lower()
    if response in ["yes", "y"]:
        interactive_smart_agent()


if __name__ == "__main__":
    main()
