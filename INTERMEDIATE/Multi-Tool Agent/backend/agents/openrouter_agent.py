import os
from openai import OpenAI
from typing import Dict, List

class OpenRouterAgent:
    def __init__(self, api_key=None, base_url=None):
        self.api_key = api_key or os.getenv('OPENROUTER_API_KEY')
        self.base_url = base_url or os.getenv('OPENROUTER_BASE_URL', 'https://openrouter.ai/api/v1')

        if not self.api_key:
            raise ValueError("OpenRouter API key not provided")

        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )

    def analyze(self, prompt: str, model: str = "google/gemini-flash-1.5",
                system_prompt: str = None, max_tokens: int = 2000) -> Dict:
        """
        Analyze text using OpenRouter API

        Args:
            prompt: User prompt/query
            model: Model to use (default: Claude 3.5 Sonnet)
            system_prompt: Optional system prompt
            max_tokens: Maximum tokens in response

        Returns:
            Dictionary with analysis result
        """
        try:
            messages = []

            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})

            messages.append({"role": "user", "content": prompt})

            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens
            )

            return {
                'success': True,
                'result': response.choices[0].message.content,
                'model': model,
                'usage': {
                    'prompt_tokens': response.usage.prompt_tokens,
                    'completion_tokens': response.usage.completion_tokens,
                    'total_tokens': response.usage.total_tokens
                }
            }

        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def summarize_search_results(self, query: str, search_results: List[Dict]) -> Dict:
        """Summarize web search results using AI"""
        results_text = "\n\n".join([
            f"Title: {r.get('title', '')}\nSnippet: {r.get('snippet', '')}"
            for r in search_results
        ])

        prompt = f"""Based on the following search results for the query "{query}",
provide a comprehensive summary:

{results_text}

Please provide:
1. A concise summary of the key information
2. Main insights or findings
3. Any relevant conclusions"""

        return self.analyze(prompt, system_prompt="You are a helpful AI assistant that summarizes search results clearly and concisely.")
