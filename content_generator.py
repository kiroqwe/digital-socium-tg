import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def generate_post():
    try:
        ru_data = pd.read_csv('ru_trends.csv', index_col='date', parse_dates=True)
        latest_ru = ru_data.iloc[-1]
        top_ru_trend = latest_ru.idxmax()

        plt.figure(figsize=(10, 6))
        ru_data.plot()
        plt.title(f"Тренды в России на {datetime.today().strftime('%d.%m.%Y')}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('ru_trends.png')

        text = f"""📊 ТРЕНДЫ ДНЯ ({datetime.today().strftime('%d.%m.%Y')})

🔥 Самый популярный запрос в РФ: #{top_ru_trend.replace(' ', '_')}
📈 Рост за 7 дней: {ru_data[top_ru_trend].pct_change(7).iloc[-1]:+.0%}

#googletrends #экономика #аналитика
"""
        return {'text': text, 'image': 'ru_trends.png'}

    except Exception as e:
        print(f"[!] Ошибка генерации контента: {e}")
        return None
