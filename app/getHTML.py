from firecrawl import Firecrawl
import os

def get_HTML(url):
    firecrawl = Firecrawl(api_key=os.getenv("FIRECRAWL_API_KEY"))
    result = firecrawl.scrape(url, formats=["summary"])
    return result.summary