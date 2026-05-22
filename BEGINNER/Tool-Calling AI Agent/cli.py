#!/usr/bin/env python3
"""
Command Line Interface for Tool-Calling Agent
==============================================
Simple CLI to interact with the agent from terminal
"""

import sys
import json
import argparse
from agent import ToolCallingAgent


class AgentCLI:
    """Command-line interface for the agent"""

    def __init__(self):
        self.agent = ToolCallingAgent()
        self.history = []

    def run_interactive(self):
        """Interactive mode - chat with the agent"""
        print("\n" + "="*60)
        print("Tool-Calling Agent - Interactive CLI")
        print("="*60)
        print("\nAvailable commands:")
        print("  calc <op> <num1> <num2>  - Calculator (add/subtract/multiply/divide)")
        print("  time                     - Get current time")
        print("  weather <city>           - Check weather")
        print("  analyze <text>           - Analyze text")
        print("  tools                    - List available tools")
        print("  history                  - Show command history")
        print("  help                     - Show this help")
        print("  quit                     - Exit")
        print("="*60 + "\n")

        while True:
            try:
                command = input("agent> ").strip()

                if not command:
                    continue

                if command.lower() in ["quit", "exit", "q"]:
                    print("Goodbye!")
                    break

                self.process_command(command)

            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")

    def process_command(self, command: str):
        """Process a single command"""
        parts = command.split()
        cmd = parts[0].lower()

        try:
            if cmd == "calc" and len(parts) >= 4:
                operation = parts[1]
                num1 = float(parts[2])
                num2 = float(parts[3])
                result = self.agent.call_tool("calculator", operation=operation, num1=num1, num2=num2)
                self.display_result(result)

            elif cmd == "time":
                result = self.agent.call_tool("get_time")
                self.display_result(result)

            elif cmd == "weather" and len(parts) >= 2:
                city = " ".join(parts[1:])
                result = self.agent.call_tool("weather", city=city)
                self.display_result(result)

            elif cmd == "analyze" and len(parts) >= 2:
                text = " ".join(parts[1:])
                result = self.agent.call_tool("text_analyzer", text=text)
                self.display_result(result)

            elif cmd == "tools":
                tools = self.agent.get_available_tools()
                print(f"\nAvailable tools: {', '.join(tools)}")

            elif cmd == "history":
                self.show_history()

            elif cmd == "help":
                self.show_help()

            else:
                print("Unknown command. Type 'help' for available commands.")

            # Add to history
            self.history.append(command)

        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"Error: {e}")

    def display_result(self, result: dict):
        """Display result in a user-friendly format"""
        if result["success"]:
            tool = result.get("tool_name", "unknown")

            if tool == "calculator":
                print(f"\n✓ Result: {result['result']}")

            elif tool == "get_time":
                print(f"\n✓ Time: {result['time']}")
                print(f"  Date: {result['date']}")
                print(f"  Day: {result['day']}")

            elif tool == "weather":
                print(f"\n✓ Weather in {result['city']}:")
                print(f"  Temperature: {result['temperature']}°C")
                print(f"  Condition: {result['condition']}")
                print(f"  Humidity: {result['humidity']}%")

            elif tool == "text_analyzer":
                print(f"\n✓ Text Analysis:")
                print(f"  Words: {result['word_count']}")
                print(f"  Characters: {result['character_count']}")
                print(f"  Sentences: {result['sentence_count']}")

        else:
            print(f"\n✗ Error: {result.get('error', 'Unknown error')}")

    def show_history(self):
        """Show command history"""
        if not self.history:
            print("\nNo command history yet.")
            return

        print("\nCommand History:")
        for i, cmd in enumerate(self.history[-10:], 1):
            print(f"  {i}. {cmd}")

    def show_help(self):
        """Show help message"""
        print("\nAvailable Commands:")
        print("  calc add 5 3           - Add two numbers")
        print("  calc subtract 10 4     - Subtract numbers")
        print("  calc multiply 6 7      - Multiply numbers")
        print("  calc divide 20 4       - Divide numbers")
        print("  time                   - Get current time")
        print("  weather Karachi        - Check weather")
        print("  analyze Hello World    - Analyze text")
        print("  tools                  - List all tools")
        print("  history                - Show history")
        print("  quit                   - Exit")

    def run_single_command(self, tool: str, **kwargs):
        """Run a single command and exit"""
        result = self.agent.call_tool(tool, **kwargs)
        print(json.dumps(result, indent=2))
        return 0 if result["success"] else 1


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Tool-Calling AI Agent CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                                    # Interactive mode
  %(prog)s --tool calculator --op add --num1 5 --num2 3
  %(prog)s --tool weather --city Karachi
  %(prog)s --tool time
  %(prog)s --tool text_analyzer --text "Hello World"
        """
    )

    parser.add_argument(
        "--tool",
        help="Tool to execute (calculator, get_time, weather, text_analyzer)"
    )

    parser.add_argument("--op", help="Calculator operation (add/subtract/multiply/divide)")
    parser.add_argument("--num1", type=float, help="First number for calculator")
    parser.add_argument("--num2", type=float, help="Second number for calculator")
    parser.add_argument("--city", help="City name for weather")
    parser.add_argument("--text", help="Text to analyze")

    parser.add_argument(
        "--json",
        action="store_true",
        help="Output in JSON format"
    )

    args = parser.parse_args()

    cli = AgentCLI()

    # If tool specified, run single command
    if args.tool:
        if args.tool == "calculator":
            if not all([args.op, args.num1 is not None, args.num2 is not None]):
                print("Error: Calculator requires --op, --num1, and --num2")
                return 1
            return cli.run_single_command("calculator", operation=args.op, num1=args.num1, num2=args.num2)

        elif args.tool in ["get_time", "time"]:
            return cli.run_single_command("get_time")

        elif args.tool == "weather":
            if not args.city:
                print("Error: Weather requires --city")
                return 1
            return cli.run_single_command("weather", city=args.city)

        elif args.tool in ["text_analyzer", "analyze"]:
            if not args.text:
                print("Error: Text analyzer requires --text")
                return 1
            return cli.run_single_command("text_analyzer", text=args.text)

        else:
            print(f"Error: Unknown tool '{args.tool}'")
            return 1

    # Otherwise, run interactive mode
    cli.run_interactive()
    return 0


if __name__ == "__main__":
    sys.exit(main())
