import requests
from bs4 import BeautifulSoup
import pandas as pd

def extractWordOfLi(li, pos: int):
    li_text = li.get_text(strip=True)
    words = li_text.split(',')[0].split()
    title = words[pos] if len(words) > pos else li_text[0]
    return title

def scrapeListSaintWikipedia(url):
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    data = []

    headings = soup.find_all('div', {'class': 'colonnes'})
    
    for heading in headings:
        table = heading.find('ul')
        
        if table:
            for li in table.find_all('li'):
                a_tag = li.find('a')

                if not a_tag: 
                    title = extractWordOfLi(li=li, pos=1)
                    href = None
                else:
                    href = a_tag['href']
                    if 'title' not in a_tag.attrs: title = extractWordOfLi(li=li, pos=1)
                    else: title = a_tag['title']
                data.append((title, href))

    
    df = pd.DataFrame(data, columns=['Saint', 'Wikipedia'])
    return df

if __name__ == '__main__':
    print("Bonjour")
    url = 'https://fr.wikipedia.org/wiki/Liste_de_saints_catholiques'
    df_saints = scrapeListSaintWikipedia(url)
    
    df_saints.to_csv('saints_df.csv', index=False)
    
    print(df_saints.head())
