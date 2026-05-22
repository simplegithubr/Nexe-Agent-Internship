"""
Unit Tests for Tool-Calling Agent
==================================
Proper testing examples using Python's unittest framework
"""

import unittest
import json
from agent import ToolCallingAgent


class TestToolCallingAgent(unittest.TestCase):
    """Test cases for ToolCallingAgent"""

    def setUp(self):
        """Har test se pehle naya agent create karo"""
        self.agent = ToolCallingAgent()

    def test_agent_initialization(self):
        """Test: Agent properly initialize hota hai"""
        self.assertIsNotNone(self.agent)
        self.assertIsInstance(self.agent.tools, dict)
        self.assertGreater(len(self.agent.tools), 0)

    def test_available_tools(self):
        """Test: All default tools available hain"""
        tools = self.agent.get_available_tools()
        expected_tools = ["calculator", "get_time", "weather", "text_analyzer"]

        for tool in expected_tools:
            self.assertIn(tool, tools)

    def test_calculator_addition(self):
        """Test: Calculator addition correctly karta hai"""
        result = self.agent.call_tool("calculator", operation="add", num1=10, num2=5)

        self.assertTrue(result["success"])
        self.assertEqual(result["result"], 15)
        self.assertEqual(result["operation"], "add")

    def test_calculator_subtraction(self):
        """Test: Calculator subtraction correctly karta hai"""
        result = self.agent.call_tool("calculator", operation="subtract", num1=20, num2=8)

        self.assertTrue(result["success"])
        self.assertEqual(result["result"], 12)

    def test_calculator_multiplication(self):
        """Test: Calculator multiplication correctly karta hai"""
        result = self.agent.call_tool("calculator", operation="multiply", num1=6, num2=7)

        self.assertTrue(result["success"])
        self.assertEqual(result["result"], 42)

    def test_calculator_division(self):
        """Test: Calculator division correctly karta hai"""
        result = self.agent.call_tool("calculator", operation="divide", num1=100, num2=4)

        self.assertTrue(result["success"])
        self.assertEqual(result["result"], 25)

    def test_calculator_division_by_zero(self):
        """Test: Division by zero properly handle hota hai"""
        result = self.agent.call_tool("calculator", operation="divide", num1=10, num2=0)

        self.assertFalse(result["success"])
        self.assertIn("error", result)
        self.assertIn("zero", result["error"].lower())

    def test_calculator_invalid_operation(self):
        """Test: Invalid operation error deta hai"""
        result = self.agent.call_tool("calculator", operation="power", num1=2, num2=3)

        self.assertFalse(result["success"])
        self.assertIn("error", result)

    def test_get_time_tool(self):
        """Test: Get time tool correctly kaam karta hai"""
        result = self.agent.call_tool("get_time")

        self.assertTrue(result["success"])
        self.assertIn("time", result)
        self.assertIn("date", result)
        self.assertIn("day", result)
        self.assertIn("timestamp", result)

    def test_weather_tool_valid_city(self):
        """Test: Weather tool valid city ke liye kaam karta hai"""
        result = self.agent.call_tool("weather", city="Karachi")

        self.assertTrue(result["success"])
        self.assertIn("temperature", result)
        self.assertIn("condition", result)
        self.assertIn("humidity", result)

    def test_weather_tool_invalid_city(self):
        """Test: Weather tool invalid city ke liye error deta hai"""
        result = self.agent.call_tool("weather", city="InvalidCity123")

        self.assertFalse(result["success"])
        self.assertIn("error", result)
        self.assertIn("available_cities", result)

    def test_text_analyzer_basic(self):
        """Test: Text analyzer basic text ko analyze karta hai"""
        text = "Hello World"
        result = self.agent.call_tool("text_analyzer", text=text)

        self.assertTrue(result["success"])
        self.assertEqual(result["word_count"], 2)
        self.assertGreater(result["character_count"], 0)

    def test_text_analyzer_empty_text(self):
        """Test: Empty text error deta hai"""
        result = self.agent.call_tool("text_analyzer", text="")

        self.assertFalse(result["success"])
        self.assertIn("error", result)

    def test_invalid_tool_name(self):
        """Test: Invalid tool name error deta hai"""
        result = self.agent.call_tool("nonexistent_tool")

        self.assertFalse(result["success"])
        self.assertIn("error", result)
        self.assertIn("available_tools", result)

    def test_missing_required_arguments(self):
        """Test: Missing arguments error deta hai"""
        result = self.agent.call_tool("calculator", operation="add", num1=10)

        self.assertFalse(result["success"])
        self.assertIn("error", result)
        self.assertEqual(result["error_type"], "TypeError")

    def test_response_contains_metadata(self):
        """Test: Response mein metadata hota hai"""
        result = self.agent.call_tool("get_time")

        self.assertIn("tool_name", result)
        self.assertIn("timestamp", result)
        self.assertEqual(result["tool_name"], "get_time")

    def test_custom_tool_registration(self):
        """Test: Custom tool register ho sakta hai"""
        def custom_tool():
            return {"success": True, "message": "Custom tool works!"}

        self.agent.register_tool("custom", custom_tool)

        self.assertIn("custom", self.agent.get_available_tools())

        result = self.agent.call_tool("custom")
        self.assertTrue(result["success"])

    def test_json_serializable_response(self):
        """Test: Response JSON serializable hai"""
        result = self.agent.call_tool("calculator", operation="add", num1=5, num2=3)

        try:
            json_string = json.dumps(result)
            parsed = json.loads(json_string)
            self.assertEqual(parsed["result"], 8)
        except (TypeError, ValueError):
            self.fail("Response is not JSON serializable")

    def test_error_type_in_response(self):
        """Test: Error response mein error_type hota hai"""
        result = self.agent.call_tool("calculator", operation="divide", num1=10, num2=0)

        self.assertFalse(result["success"])
        self.assertIn("error_type", result)
        self.assertIsInstance(result["error_type"], str)


class TestCalculatorEdgeCases(unittest.TestCase):
    """Calculator ke edge cases test karo"""

    def setUp(self):
        self.agent = ToolCallingAgent()

    def test_negative_numbers(self):
        """Test: Negative numbers ke saath kaam karta hai"""
        result = self.agent.call_tool("calculator", operation="add", num1=-5, num2=3)
        self.assertTrue(result["success"])
        self.assertEqual(result["result"], -2)

    def test_decimal_numbers(self):
        """Test: Decimal numbers ke saath kaam karta hai"""
        result = self.agent.call_tool("calculator", operation="multiply", num1=2.5, num2=4)
        self.assertTrue(result["success"])
        self.assertEqual(result["result"], 10.0)

    def test_large_numbers(self):
        """Test: Large numbers handle hote hain"""
        result = self.agent.call_tool("calculator", operation="multiply", num1=999999, num2=999999)
        self.assertTrue(result["success"])
        self.assertIsInstance(result["result"], (int, float))


class TestTextAnalyzerEdgeCases(unittest.TestCase):
    """Text analyzer ke edge cases"""

    def setUp(self):
        self.agent = ToolCallingAgent()

    def test_single_word(self):
        """Test: Single word analyze hota hai"""
        result = self.agent.call_tool("text_analyzer", text="Hello")
        self.assertTrue(result["success"])
        self.assertEqual(result["word_count"], 1)

    def test_multiple_sentences(self):
        """Test: Multiple sentences count hote hain"""
        text = "Hello. How are you? I am fine!"
        result = self.agent.call_tool("text_analyzer", text=text)
        self.assertTrue(result["success"])
        self.assertEqual(result["sentence_count"], 3)

    def test_special_characters(self):
        """Test: Special characters handle hote hain"""
        text = "Hello @world! #test $100"
        result = self.agent.call_tool("text_analyzer", text=text)
        self.assertTrue(result["success"])
        self.assertGreater(result["character_count"], 0)


def run_tests():
    """Tests ko run karo aur results dikhao"""
    print("\n" + "="*60)
    print("Running Unit Tests")
    print("="*60 + "\n")

    # Test suite create karo
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # All test classes add karo
    suite.addTests(loader.loadTestsFromTestCase(TestToolCallingAgent))
    suite.addTests(loader.loadTestsFromTestCase(TestCalculatorEdgeCases))
    suite.addTests(loader.loadTestsFromTestCase(TestTextAnalyzerEdgeCases))

    # Tests run karo
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Summary
    print("\n" + "="*60)
    print("Test Summary")
    print("="*60)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")

    if result.wasSuccessful():
        print("\n✅ All tests passed!")
    else:
        print("\n❌ Some tests failed!")

    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests()
