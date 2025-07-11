from telegram import Bot
import os
from content_generator import generate_post

def post_to_channel():
    print("📌 Генерация контента...")
    content = generate_post()

    if not content:
        print("[!] Контент не сгенерирован")
        return

    print("📌 Инициализация бота...")
    bot = Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])

    print("📌 Попытка отправки поста...")
    try:
        with open(content['image'], 'rb') as photo:
            bot.send_photo(
                chat_id=os.environ['TELEGRAM_CHANNEL_ID'],
                photo=photo,
                caption=content['text']
            )
        print("[✔] Пост опубликован")
    except Exception as e:
        print(f"[!] Ошибка отправки поста: {e}")

if __name__ == "__main__":
    post_to_channel()
