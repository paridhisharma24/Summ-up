import requests
from bs4 import BeautifulSoup

def Generate_artc_transcript(article_link):
    r = requests.get(article_link)
    htmlContent = r.content

    soup = BeautifulSoup(htmlContent,'html.parser')

    gen_transcript = ""
    for para in soup.find_all("p"):
        gen_transcript += para.get_text()
        gen_transcript += " "

    return gen_transcript