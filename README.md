# 📘 Learning Bot

Telegram-бот, который каждое утро присылает интересный факт об английском языке — с примером, переводом и пояснением.  
Идеально для лёгкой практики английского и расширения словарного запаса.  
Также к каждому сообщению прикрепляется случайное изображение.

---

## 🔧 Технологии
- Python 3.11+
- [aiogram 3.x](https://github.com/aiogram/aiogram)
- OpenAI API (для генерации фактов — опционально)
- JSON для хранения данных
- GitHub Actions / VPS (в перспективе для хостинга)

---

## 🚀 Запуск
1. Клонируй репозиторий:
   ```bash
   git clone git@github.com:David13777/learning_bot.git
   cd learning_bot
   
Создай файл .env:
BOT_TOKEN=твой_токен_бота
CHAT_ID=твой_chat_id

Установи зависимости:
pip install -r requirements.txt


📦 Структура проекта
learning_bot/
├── images/           # Картинки, прикрепляемые к сообщениям
├── main.py           # Основная логика отправки постов
├── convert.py        # Скрипт для конвертации jfif → jpg
├── facts.json        # База фактов
├── .env              # Скрытые данные (не в репозитории)
├── .gitignore
└── README.md

📬 Пример поста от бота
🌞 Good morning, team!
📘 Did you know? The word "unfriend" existed before Facebook — it was used in 1659!
Слово существовало задолго до соцсетей.
💬 Example: He unfriended me after the argument.
Он удалил меня из друзей после ссоры.
🔎 Note: Не обязательно только в соцсетях!

🧪 В планах
- Расширить базу фактов до 100+ 📚
- Добавить автохостинг (например, через Railway)
- Поддержка мультиботов (несколько чатов)
- Управление контентом через админку

🧑‍💻 Автор
David13777
https://github.com/David13777



