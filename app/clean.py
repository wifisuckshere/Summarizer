from bs4 import BeautifulSoup
from readability import Document
import markdown

def clean_output(output):
    return markdown.markdown(output, extensions=["extra", "sane_lists", "codehilite"])