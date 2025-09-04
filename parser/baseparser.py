import requests
import pandas as pd

from parser_config import HEADERS
from pathlib import Path

class BaseParser:
    def __init__(self):
        pass

    @staticmethod
    def save_info_csv(file_name: str, data: pd.DataFrame) -> bool:
        try:
            file_exists = Path(file_name).exists()
            data.to_csv(
                file_name,
                mode='a',  # Дописываем, если файл есть
                header=not file_exists,  # Заголовок только для нового файла
                index=False,
                encoding='utf-8'
            )
            print("Datas Saved")
            return True
        except Exception as e:
            print(f"Error saving to CSV: {e}")
            return False
    
    
    def fetch(self, url) -> requests.Response | None:
        try:
            response = requests.get(url, headers=HEADERS)
            response.raise_for_status()
            return response
        except Exception as e:
            print(f'Request failed: {e}')
            return None