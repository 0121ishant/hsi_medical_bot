# import requests
# from typing import Dict

# from .pubmed_search import PubmedSearchAgent
# from .tavily_search import TavilySearchAgent

# class WebSearchAgent:
#     """
#     Agent responsible for retrieving real-time medical information from web sources.
#     """
    
#     def __init__(self, config):
#         self.tavily_search_agent = TavilySearchAgent()
        
#         # self.pubmed_search_agent = PubmedSearchAgent()
#         # self.pubmed_api_url = config.pubmed_api_url
    
#     def search(self, query: str) -> str:
#         """
#         Perform both general and medical-specific searches.
#         """
#         # print(f"[WebSearchAgent] Searching for: {query}")
        
#         tavily_results = self.tavily_search_agent.search_tavily(query=query)
#         # pubmed_results = self.pubmed_search_agent.search_pubmed(self.pubmed_api_url, query)
        
#         return f"Tavily Results:\n{tavily_results}\n"
#         # \nPubMed Results:\n{pubmed_results}"


import requests
from typing import Dict

from .pubmed_search import PubmedSearchAgent
from .tavily_search import TavilySearchAgent

class WebSearchAgent:
    """
    Agent responsible for retrieving real-time medical information from web sources.
    """
    
    def __init__(self, config):
        self.tavily_search_agent = TavilySearchAgent()
        
        # Optional: Enable PubMed search later
        # self.pubmed_search_agent = PubmedSearchAgent()
        # self.pubmed_api_url = config.pubmed_api_url
    
    def search(self, query: str) -> str:
        """
        Perform both general and medical-specific searches.
        Return results along with their sources.
        """
        results = []

        # Tavily search
        tavily_data = self.tavily_search_agent.search_tavily(query=query)
        if tavily_data:
            results.append(f"[Source: Tavily]\n{tavily_data.strip()}")

        # Optional: Uncomment to include PubMed
        # pubmed_data = self.pubmed_search_agent.search_pubmed(self.pubmed_api_url, query)
        # if pubmed_data:
        #     results.append(f"[Source: PubMed]\n{pubmed_data.strip()}")

        return "\n\n".join(results) if results else "No relevant information found from web sources."

