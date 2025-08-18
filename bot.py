import os
import asyncio
import logging
import aiohttp
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

async def ask_gpt(prompt: str) -> str:
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
    data = {
        "model": "gpt-5",
        "messages": [{"role": "user", "content": prompt}]
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as resp:
            res = await resp.json()
            try:
                return res["choices"][0]["message"]["content"]
            except Exception:
                return f"⚠️ Ошибка OpenAI API: {res}"

@dp.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer("Привет! Я GPT-бот 🤖 Напиши что-нибудь.")

@dp.message(F.text)
async def chat(message: Message):
    reply = await ask_gpt(message.text)
    await message.answer(reply)

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())