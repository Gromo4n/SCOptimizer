from typing import List
from parser.baseparser import BaseParser
from bs4 import BeautifulSoup
from parser_config import ART_URL, BASE_URL

class ArtParser(BaseParser):
    def get_art_links(self) -> List[str] | None:
        url = ART_URL
        try:
            response = self.fetch(url)

            art_links = []
            
            soup = BeautifulSoup(response.text, "html.parser")
            arts_box = soup.find('div', class_='custom-scrollbar')
            links = arts_box.find_all('a')
            for link in links:
                art_links.append(BASE_URL + link['href'])
            
            return art_links

        except Exception as e:
            print(f"Error: {e}")
            return None
        
    def get_art_stats(self, link):
        try:
            response = self.fetch(link)

            stats = {}

            soup = BeautifulSoup(response.text, "html.parser")
            item_box = soup.find('div', class_='self-start')
            item_name = item_box.find('h1').get_text(strip=True)

            stats['Название'] = item_name

            stat_box = soup.find('div', class_='inline-block')
            base_stats_box = stat_box.find('ul', class_='mb-2')
            base_stat_rows = base_stats_box.find_all('li')
            for row in base_stat_rows:
                stat_name = row.find_all('span')[0].get_text(strip=True)
                stat_val = row.find_all('span')[1].get_text(strip=True)
                stats[stat_name] = stat_val

            add_stats_box = stat_box.find('div', class_='pl-1')
            add_stat_rows = add_stats_box.find_all('li')
            for row in add_stat_rows:
                stat_name = row.find_all('span')[0].get_text(strip=True)
                stat_val = row.find_all('span')[1].get_text(strip=True)
                stats["add_" + stat_name] = stat_val

            return stats

        except Exception as e:
            print(f"Error {e}")
            return None
    
    