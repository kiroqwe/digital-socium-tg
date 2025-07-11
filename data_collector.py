from pytrends.request import TrendReq
import pandas as pd

def collect_data():
    try:
        pytrends = TrendReq()
        keywords = ['инфляция', 'курс доллара', 'криптовалюта', 'акции', 'недвижимость']

        pytrends.build_payload(keywords, timeframe='today 1-m', geo='RU')
        ru_data = pytrends.interest_over_time().drop(columns=['isPartial'])

        pytrends.build_payload(keywords, timeframe='today 1-m', geo='')
        world_data = pytrends.interest_over_time().drop(columns=['isPartial'])

        ru_data.to_csv('ru_trends.csv')
        world_data.to_csv('world_trends.csv')

        print("[✔] Данные собраны")
        return ru_data, world_data

    except Exception as e:
        print(f"[!] Ошибка сбора данных: {e}")
        return None, None

if __name__ == "__main__":
    collect_data()
