import asyncio
import json
import random
import os
from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import FSInputFile
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

def load_facts():
    with open("facts.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_random_image():
    images_dir = "images"
    files = [f for f in os.listdir(images_dir) if os.path.isfile(os.path.join(images_dir, f))]
    if not files:
        return None
    return os.path.join(images_dir, random.choice(files))

async def send_daily_fact():
    while True:
        now = datetime.now()
        target = now.replace(hour=8, minute=5, second=0, microsecond=0)

        if now >= target:
            target += timedelta(days=1)

        wait_seconds = (target - now).total_seconds()
        await asyncio.sleep(wait_seconds)

        facts = load_facts()
        fact = random.choice(facts)
        image_path = get_random_image()

        text = (
            "🌞 <b>Good morning, team!</b>\n\n"
            f"📘 <b>Did you know?</b> {fact['fact_en']}\n"
            f"<i>{fact['fact_ru']}</i>\n\n"
            f"💬 <b>Example:</b> {fact['example_en']}\n"
            f"<i>{fact['example_ru']}</i>\n\n"
            f"🔎 <b>Note:</b> {fact['note']}"
        )

        if image_path:
            photo = FSInputFile(image_path)
            await bot.send_photo(chat_id=CHAT_ID, photo=photo, caption=text)
        else:
            await bot.send_message(chat_id=CHAT_ID, text=text)


    await bot.session.close()

asyncio.run(send_daily_fact())
