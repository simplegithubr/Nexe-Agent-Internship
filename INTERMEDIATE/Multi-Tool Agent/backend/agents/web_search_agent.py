from duckduckgo_search import DDGS
from typing import List, Dict

class WebSearchAgent:
    def __init__(self):
        self.ddgs = DDGS()

    def search(self, query: str, max_results: int = 5) -> List[Dict]:
        """
        Perform web search using DuckDuckGo

        Args:
            query: Search query string
            max_results: Maximum number of results to return

        Returns:
            List of search results with title, link, and snippet
        """
        try:
            results = []
            search_results = self.ddgs.text(query, max_results=max_results)

            for result in search_results:
                results.append({
                    'title': result.get('title', ''),
                    'link': result.get('href', ''),
                    'snippet': result.get('body', '')
                })

            return results
        except Exception as e:
            return [{'error': f'Search failed: {str(e)}'}]

    def search_news(self, query: str, max_results: int = 5) -> List[Dict]:
        """Search for news articles"""
        try:
            results = []
            news_results = self.ddgs.news(query, max_results=max_results)

            for result in news_results:
                results.append({
                    'title': result.get('title', ''),
                    'link': result.get('url', ''),
                    'snippet': result.get('body', ''),
                    'date': result.get('date', ''),
                    'source': result.get('source', '')
                })

            return results
        except Exception as e:
            return [{'error': f'News search failed: {str(e)}'}]
