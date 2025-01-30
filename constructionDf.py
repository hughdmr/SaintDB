import pandas as pd
from scrapingListSaintWiki import scrapeListSaintWikipedia
from scrapingSaintWiki import scrapeSaintWikipedia

def constructDf():
    print("----Scraping de la liste des saints----")
    url = 'https://fr.wikipedia.org/wiki/Liste_de_saints_catholiques'
    df_saints = scrapeListSaintWikipedia(url)
    print("----Liste des saints sauvegardee----")  
    print("----Scraping de la vie des saints----")  
    
    # Limit to first 10 rows
    for index, row in df_saints.iterrows():  # Iterate over the first 10 rows
        if row.get('Wikipedia', ''):
            wikipedia_url = 'https://fr.wikipedia.org' + row.get('Wikipedia', '')
        
            print(f"Scraping {wikipedia_url}...")
            text = scrapeSaintWikipedia(wikipedia_url)
            df_saints.at[index, 'scrapingWikipedia'] = text  # Add the scraped text to the row

        else:
            df_saints.at[index, 'scrapingWikipedia'] = None
    
    # Save to CSV
    df_saints.to_csv('saintsDf.csv', index=False)
    
    print(df_saints.head())  # Display the first 10 rows of the DataFrame

if __name__ == '__main__':
    constructDf()  # Call the function to scrape and save the DataFrame
