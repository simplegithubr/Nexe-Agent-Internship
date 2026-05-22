"""
Interactive Examples - Tool-Calling Agent
==========================================
Yeh file different scenarios mein agent ko use karne ke examples dikhati hai
"""

from agent import ToolCallingAgent
import json


def example_1_basic_usage():
    """Basic usage - Simple tool calls"""
    print("\n" + "="*60)
    print("Example 1: Basic Usage")
    print("="*60)

    agent = ToolCallingAgent()

    # Simple calculator call
    result = agent.call_tool("calculator", operation="multiply", num1=7, num2=8)

    if result["success"]:
        print(f"✅ 7 × 8 = {result['result']}")
    else:
        print(f"❌ Error: {result['error']}")


def example_2_chaining_tools():
    """Multiple tools ko sequence mein use karna"""
    print("\n" + "="*60)
    print("Example 2: Chaining Multiple Tools")
    print("="*60)

    agent = ToolCallingAgent()

    # Step 1: Get current time
    time_result = agent.call_tool("get_time")
    print(f"📅 Current time: {time_result['time']} on {time_result['date']}")

    # Step 2: Check weather
    weather_result = agent.call_tool("weather", city="Lahore")
    print(f"🌤️  Weather in Lahore: {weather_result['temperature']}°C, {weather_result['condition']}")

    # Step 3: Analyze some text
    text = f"Today is {time_result['day']} and the weather is {weather_result['condition']}"
    analysis = agent.call_tool("text_analyzer", text=text)
    print(f"📝 Text has {analysis['word_count']} words and {analysis['character_count']} characters")


def example_3_error_handling():
    """Error handling ko demonstrate karna"""
    print("\n" + "="*60)
    print("Example 3: Proper Error Handling")
    print("="*60)

    agent = ToolCallingAgent()

    # Try different operations and handle errors
    operations = [
        ("add", 10, 5),
        ("divide", 100, 0),  # This will fail
        ("multiply", 3, 7),
        ("invalid_op", 1, 2)  # This will fail
    ]

    for op, num1, num2 in operations:
        result = agent.call_tool("calculator", operation=op, num1=num1, num2=num2)

        if result["success"]:
            print(f"✅ {num1} {op} {num2} = {result['result']}")
        else:
            print(f"❌ {num1} {op} {num2} failed: {result['error']}")


def example_4_batch_processing():
    """Multiple items ko process karna"""
    print("\n" + "="*60)
    print("Example 4: Batch Processing")
    print("="*60)

    agent = ToolCallingAgent()

    # Multiple cities ka weather check karo
    cities = ["Karachi", "Lahore", "Islamabad", "London", "Dubai"]  # Dubai available nahi hai

    print("🌍 Checking weather for multiple cities:\n")

    for city in cities:
        result = agent.call_tool("weather", city=city)

        if result["success"]:
            print(f"  {city:15} → {result['temperature']}°C, {result['condition']}")
        else:
            print(f"  {city:15} → ❌ Not available")


def example_5_data_collection():
    """Data collect karke analyze karna"""
    print("\n" + "="*60)
    print("Example 5: Data Collection & Analysis")
    print("="*60)

    agent = ToolCallingAgent()

    # Multiple calculations karo aur results collect karo
    calculations = [
        ("add", 10, 5),
        ("subtract", 20, 8),
        ("multiply", 6, 7),
        ("divide", 100, 4)
    ]

    results = []

    for op, num1, num2 in calculations:
        result = agent.call_tool("calculator", operation=op, num1=num1, num2=num2)
        if result["success"]:
            results.append(result["result"])

    # Analyze collected data
    print(f"📊 Collected {len(results)} results: {results}")
    print(f"   Sum: {sum(results)}")
    print(f"   Average: {sum(results)/len(results):.2f}")
    print(f"   Max: {max(results)}")
    print(f"   Min: {min(results)}")


def example_6_custom_tool():
    """Apna custom tool add karna"""
    print("\n" + "="*60)
    print("Example 6: Adding Custom Tool")
    print("="*60)

    agent = ToolCallingAgent()

    # Custom tool define karo
    def string_reverser(text: str):
        """String ko reverse karta hai"""
        try:
            if not text:
                raise ValueError("Text cannot be empty")

            return {
                "success": True,
                "original": text,
                "reversed": text[::-1],
                "length": len(text)
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    # Tool register karo
    agent.register_tool("reverse", string_reverser)

    # Use karo
    result = agent.call_tool("reverse", text="Hello World")

    if result["success"]:
        print(f"Original: {result['original']}")
        print(f"Reversed: {result['reversed']}")


def example_7_json_export():
    """Results ko JSON file mein save karna"""
    print("\n" + "="*60)
    print("Example 7: Exporting Results to JSON")
    print("="*60)

    agent = ToolCallingAgent()

    # Multiple operations perform karo
    operations_log = []

    # Weather check
    weather = agent.call_tool("weather", city="Karachi")
    operations_log.append(weather)

    # Time check
    time = agent.call_tool("get_time")
    operations_log.append(time)

    # Calculation
    calc = agent.call_tool("calculator", operation="add", num1=100, num2=50)
    operations_log.append(calc)

    # Save to JSON file
    with open("operations_log.json", "w") as f:
        json.dump(operations_log, f, indent=2)

    print("✅ Results saved to operations_log.json")
    print(f"📝 Total operations logged: {len(operations_log)}")


def example_8_conditional_logic():
    """Conditional logic ke saath tools use karna"""
    print("\n" + "="*60)
    print("Example 8: Conditional Tool Usage")
    print("="*60)

    agent = ToolCallingAgent()

    # Weather check karo
    weather = agent.call_tool("weather", city="Karachi")

    if weather["success"]:
        temp = weather["temperature"]

        # Temperature ke basis pe message
        if temp > 30:
            message = "It's very hot! Stay hydrated."
        elif temp > 20:
            message = "Pleasant weather today!"
        else:
            message = "It's cold. Wear warm clothes."

        print(f"🌡️  Temperature: {temp}°C")
        print(f"💬 Advice: {message}")

        # Text analyze karo
        analysis = agent.call_tool("text_analyzer", text=message)
        print(f"📊 Message has {analysis['word_count']} words")


def interactive_mode():
    """Interactive mode - User input le kar tools call karo"""
    print("\n" + "="*60)
    print("Interactive Mode")
    print("="*60)
    print("\nAvailable commands:")
    print("  1. calc    - Calculator")
    print("  2. time    - Get current time")
    print("  3. weather - Check weather")
    print("  4. analyze - Analyze text")
    print("  5. quit    - Exit")
    print("="*60)

    agent = ToolCallingAgent()

    while True:
        command = input("\n➤ Enter command: ").strip().lower()

        if command == "quit":
            print("👋 Goodbye!")
            break

        elif command == "calc":
            try:
                op = input("  Operation (add/subtract/multiply/divide): ")
                num1 = float(input("  First number: "))
                num2 = float(input("  Second number: "))

                result = agent.call_tool("calculator", operation=op, num1=num1, num2=num2)

                if result["success"]:
                    print(f"  ✅ Result: {result['result']}")
                else:
                    print(f"  ❌ Error: {result['error']}")

            except ValueError:
                print("  ❌ Invalid input!")

        elif command == "time":
            result = agent.call_tool("get_time")
            if result["success"]:
                print(f"  🕐 Time: {result['time']}")
                print(f"  📅 Date: {result['date']}")
                print(f"  📆 Day: {result['day']}")

        elif command == "weather":
            city = input("  City name: ")
            result = agent.call_tool("weather", city=city)

            if result["success"]:
                print(f"  🌤️  Temperature: {result['temperature']}°C")
                print(f"  ☁️  Condition: {result['condition']}")
                print(f"  💧 Humidity: {result['humidity']}%")
            else:
                print(f"  ❌ {result['error']}")

        elif command == "analyze":
            text = input("  Enter text: ")
            result = agent.call_tool("text_analyzer", text=text)

            if result["success"]:
                print(f"  📝 Words: {result['word_count']}")
                print(f"  🔤 Characters: {result['character_count']}")
                print(f"  📄 Sentences: {result['sentence_count']}")

        else:
            print("  ❌ Unknown command!")


def main():
    """Run all examples"""
    print("\n" + "🚀"*30)
    print("Tool-Calling Agent - Interactive Examples")
    print("🚀"*30)

    # Run all examples
    example_1_basic_usage()
    example_2_chaining_tools()
    example_3_error_handling()
    example_4_batch_processing()
    example_5_data_collection()
    example_6_custom_tool()
    example_7_json_export()
    example_8_conditional_logic()

    # Ask if user wants interactive mode
    print("\n" + "="*60)
    response = input("\n🎮 Want to try interactive mode? (yes/no): ").strip().lower()

    if response in ["yes", "y"]:
        interactive_mode()
    else:
        print("\n✅ All examples completed!")


if __name__ == "__main__":
    main()
