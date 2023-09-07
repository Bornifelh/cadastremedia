import concurrent.futures
import requests
from bs4 import BeautifulSoup
from datetime import date
import mysql.connector

def scrape_site(base_url):
    publications = []

    while True:
        response = requests.get(base_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            for post in soup.find_all('div'):
                titre = post.find('h2').text if post.find('h2') else "N/A"
                lien = post.find('a')['href'] if post.find('a') and 'href' in post.find('a') else "N/A"
                description = post.find('p').text[:25] if post.find('p') else "N/A"
                date_publication = date.today()

                contenu = f"{titre} {description}".lower()
                if "gabon" in contenu or "ctri" in contenu:
                    publications.append((titre, lien, description, date_publication))

            next_page_link = soup.find('a', class_='pagination-next')
            if next_page_link:
                base_url = next_page_link['href']
            else:
                break

        else:
            print("La requête a échoué")
            break

    db_config = {
        "host": "185.166.188.154",
        "user": "u948053727_capal",
        "password": "Decembre@2023",
        "database": "u948053727_capal"
    }
    connection = mysql.connector.connect(**db_config)

    cursor = connection.cursor()
    for publication in publications:
        cursor.execute("INSERT INTO data_mel_inter(titre, lien, description, datesaisie) VALUES (%s, %s, %s, %s)",
                       publication)

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    # Liste des URL des sites à scraper
    sites_to_scrape = ["URL_DU_SITE_1", "URL_DU_SITE_2", "URL_DU_SITE_3"]

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(sites_to_scrape)) as executor:
        executor.map(scrape_site, sites_to_scrape)
