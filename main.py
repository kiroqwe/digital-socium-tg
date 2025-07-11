import asyncio
from telegram import Bot

TOKEN = '7972913800:AAGk6QVX2fVSUe3-C-hs9uMAxko7sQHWpGA'
CHAT_ID = '-1002873768312'
bot = Bot(token=TOKEN)

async def main():
    with open('plot.png', 'rb') as photo:
        await bot.send_photo(chat_id=CHAT_ID, photo=photo, caption="📊 Google Trends анализ")

if __name__ == "__main__":
    asyncio.run(main())
