"""
Tool-Calling AI Agent - Beginner Level
======================================
Yeh agent different tools ko call kar sakta hai aur JSON format mein response deta hai.
"""

import json
import sys
from typing import Dict, List, Any, Callable
from datetime import datetime

# Set UTF-8 encoding for Windows console
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass


class ToolCallingAgent:
    """
    Main Agent class jo tools ko manage karta hai aur unhe call karta hai.
    """

    def __init__(self):
        # Available tools ko store karne ke liye dictionary
        self.tools: Dict[str, Callable] = {}
        self._register_default_tools()

    def _register_default_tools(self):
        """Default tools ko register karta hai"""
        self.register_tool("calculator", self.calculator_tool)
        self.register_tool("get_time", self.get_time_tool)
        self.register_tool("weather", self.weather_tool)
        self.register_tool("text_analyzer", self.text_analyzer_tool)

    def register_tool(self, tool_name: str, tool_function: Callable):
        """
        Naya tool register karne ke liye

        Args:
            tool_name: Tool ka naam
            tool_function: Function jo execute hoga
        """
        self.tools[tool_name] = tool_function
        print(f"✓ Tool registered: {tool_name}")

    def calculator_tool(self, operation: str, num1: float, num2: float) -> Dict[str, Any]:
        """
        Calculator tool - basic math operations

        Args:
            operation: add, subtract, multiply, divide
            num1: Pehla number
            num2: Dusra number
        """
        try:
            operations = {
                "add": num1 + num2,
                "subtract": num1 - num2,
                "multiply": num1 * num2,
                "divide": num1 / num2 if num2 != 0 else None
            }

            if operation not in operations:
                raise ValueError(f"Invalid operation: {operation}")

            result = operations[operation]

            if result is None:
                raise ValueError("Cannot divide by zero")

            return {
                "success": True,
                "result": result,
                "operation": operation,
                "inputs": {"num1": num1, "num2": num2}
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__
            }

    def get_time_tool(self) -> Dict[str, Any]:
        """Current time return karta hai"""
        try:
            now = datetime.now()
            return {
                "success": True,
                "time": now.strftime("%H:%M:%S"),
                "date": now.strftime("%Y-%m-%d"),
                "day": now.strftime("%A"),
                "timestamp": now.timestamp()
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__
            }

    def weather_tool(self, city: str) -> Dict[str, Any]:
        """
        Weather information (simulated - real API ke liye API key chahiye)

        Args:
            city: City ka naam
        """
        try:
            # Simulated weather data
            weather_data = {
                "karachi": {"temp": 32, "condition": "Sunny", "humidity": 65},
                "lahore": {"temp": 28, "condition": "Cloudy", "humidity": 70},
                "islamabad": {"temp": 25, "condition": "Pleasant", "humidity": 55},
                "london": {"temp": 15, "condition": "Rainy", "humidity": 80},
                "new york": {"temp": 20, "condition": "Partly Cloudy", "humidity": 60}
            }

            city_lower = city.lower()

            if city_lower not in weather_data:
                return {
                    "success": False,
                    "error": f"Weather data not available for {city}",
                    "available_cities": list(weather_data.keys())
                }

            data = weather_data[city_lower]
            return {
                "success": True,
                "city": city,
                "temperature": data["temp"],
                "condition": data["condition"],
                "humidity": data["humidity"],
                "unit": "Celsius"
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__
            }

    def text_analyzer_tool(self, text: str) -> Dict[str, Any]:
        """
        Text ko analyze karta hai

        Args:
            text: Analyze karne ke liye text
        """
        try:
            if not text:
                raise ValueError("Text cannot be empty")

            words = text.split()
            chars = len(text)
            chars_no_space = len(text.replace(" ", ""))

            return {
                "success": True,
                "word_count": len(words),
                "character_count": chars,
                "character_count_no_spaces": chars_no_space,
                "sentence_count": text.count('.') + text.count('!') + text.count('?'),
                "uppercase_count": sum(1 for c in text if c.isupper()),
                "lowercase_count": sum(1 for c in text if c.islower())
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__
            }

    def call_tool(self, tool_name: str, **kwargs) -> Dict[str, Any]:
        """
        Tool ko call karta hai aur JSON response return karta hai

        Args:
            tool_name: Kis tool ko call karna hai
            **kwargs: Tool ke arguments

        Returns:
            JSON response dictionary
        """
        try:
            # Check if tool exists
            if tool_name not in self.tools:
                return {
                    "success": False,
                    "error": f"Tool '{tool_name}' not found",
                    "available_tools": list(self.tools.keys())
                }

            # Tool ko call karo
            tool_function = self.tools[tool_name]
            result = tool_function(**kwargs)

            # Response mein metadata add karo
            result["tool_name"] = tool_name
            result["timestamp"] = datetime.now().isoformat()

            return result

        except TypeError as e:
            # Wrong arguments pass hue
            return {
                "success": False,
                "error": f"Invalid arguments for tool '{tool_name}': {str(e)}",
                "error_type": "TypeError",
                "tool_name": tool_name
            }

        except Exception as e:
            # Koi aur error
            return {
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__,
                "tool_name": tool_name
            }

    def get_available_tools(self) -> List[str]:
        """Available tools ki list return karta hai"""
        return list(self.tools.keys())

    def get_tool_info(self) -> Dict[str, str]:
        """Har tool ki information return karta hai"""
        info = {}
        for tool_name, tool_func in self.tools.items():
            info[tool_name] = tool_func.__doc__ or "No description available"
        return info


def main():
    """Main function - Agent ko test karne ke liye"""

    print("=" * 60)
    print("Tool-Calling AI Agent - Demo")
    print("=" * 60)
    print()

    # Agent create karo
    agent = ToolCallingAgent()

    print("\n📋 Available Tools:")
    for tool in agent.get_available_tools():
        print(f"  • {tool}")

    print("\n" + "=" * 60)
    print("Testing Tools...")
    print("=" * 60)

    # Test 1: Calculator
    print("\n1️⃣ Calculator Tool:")
    result = agent.call_tool("calculator", operation="add", num1=10, num2=5)
    print(json.dumps(result, indent=2))

    # Test 2: Time
    print("\n2️⃣ Get Time Tool:")
    result = agent.call_tool("get_time")
    print(json.dumps(result, indent=2))

    # Test 3: Weather
    print("\n3️⃣ Weather Tool:")
    result = agent.call_tool("weather", city="Karachi")
    print(json.dumps(result, indent=2))

    # Test 4: Text Analyzer
    print("\n4️⃣ Text Analyzer Tool:")
    result = agent.call_tool("text_analyzer", text="Hello World! This is a test.")
    print(json.dumps(result, indent=2))

    # Test 5: Error Handling - Invalid Tool
    print("\n5️⃣ Error Handling - Invalid Tool:")
    result = agent.call_tool("invalid_tool")
    print(json.dumps(result, indent=2))

    # Test 6: Error Handling - Wrong Arguments
    print("\n6️⃣ Error Handling - Wrong Arguments:")
    result = agent.call_tool("calculator", operation="add", num1=10)  # num2 missing
    print(json.dumps(result, indent=2))

    # Test 7: Error Handling - Division by Zero
    print("\n7️⃣ Error Handling - Division by Zero:")
    result = agent.call_tool("calculator", operation="divide", num1=10, num2=0)
    print(json.dumps(result, indent=2))

    print("\n" + "=" * 60)
    print("✅ All tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
