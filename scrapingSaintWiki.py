import requests
from bs4 import BeautifulSoup

def scrapeSaintWikipedia(url):
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')

    section = soup.find_all('div', {'class': 'mw-content-ltr mw-parser-output'})
    if len(section) == 0:
        return None
    section = section[0]

    text = ""
    paragraph_count = 0

    for sibling in section.find_all_next(['th', 'td', 'p']):
        if sibling.name == 'p':
            paragraph_count += 1
            text += sibling.get_text(strip=True) + "/"
            if paragraph_count >= 8:
                break
        else:
            text += sibling.get_text(strip=True) + "/"
    
    return text

if __name__ == '__main__':
    url = 'https://fr.wikipedia.org/wiki/Pierre_(apôtre)'
    text = scrapeSaintWikipedia(url)
    print(text)
