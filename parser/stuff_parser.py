from typing import List
from parser.baseparser import BaseParser
from parser_config import FOOD_URL, BASE_URL
from bs4 import BeautifulSoup


class ItemParser(BaseParser):
    def get_item_links(self, url: str, item_type: str) -> List[str]: 
        try:
            response = self.fetch(url)
            item_links = []

            soup = BeautifulSoup(response.text, 'html.parser')
            item_box = soup.find('div', class_='custom-scrollbar')
            links = item_box.find_all('a')
            imgs = item_box.find_all('img')
            for idx in range(len(links)):
                if 'F' + item_type not in imgs[idx].get('src', ''):
                    continue
                item_links.append(BASE_URL + links[idx]['href'])
            
            print(len(item_links))
            return item_links

        except Exception as e:
            print(f"Error: {e}")
            return None
        
    def get_item_stats(self, link: str) -> dict | None:
        try:
            response = self.fetch(link)

            stats = {}

            soup = BeautifulSoup(response.text, "html.parser")
            item_box = soup.find('div', class_='self-start')
            item_name = item_box.find('h1').get_text(strip=True)

            stats['Название'] = item_name

            stat_box = soup.find('div', class_='inline-block')
            base_stats_box = stat_box.find('ul', class_='text-primary')
            base_stat_rows = base_stats_box.find_all('li')

            for row in base_stat_rows:
                lines = row.find_all('span', style=lambda value: value and 'color' in value)
                if len(lines) == 2:
                    stat_name = lines[0].get_text(strip=True)
                    stat_val = lines[1].get_text(strip=True)
                    stats[stat_name] = stat_val

            return stats

        except Exception as e:
            print(f"Error {e}")
            return None