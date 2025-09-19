from firecrawl import Firecrawl


def get_HTML(url):
    firecrawl = Firecrawl(api_key="fc-fc23f9fc3b3a47f2a453353a0a5ee51c")
    result = firecrawl.scrape(url, formats=["summary"])
    return result.summary