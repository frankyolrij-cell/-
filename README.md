
# GPT Telegram Bot (aiogram 3 + OpenAI, Render Deploy)

## 🚀 Запуск локально
```bash
pip install -r requirements.txt
python bot.py
```

## 🌍 Деплой на Render
1. Создать новый проект → "New Web Service".  
2. Загрузить этот архив.  
3. В разделе **Environment variables** добавить:  
   ```
   BOT_TOKEN=твой_токен_от_BotFather
   OPENAI_API_KEY=твой_API_ключ_от_OpenAI
   ```
4. Render сам запустит `python bot.py` (через Procfile).  

Бот будет отвечать в Telegram с помощью ChatGPT 🤖
