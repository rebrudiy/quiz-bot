# Telegram Quiz Bot — инструкция (для любой ОС)

Этот бот задаёт вопросы из Excel и считает результат.  
Один Excel = одна тема (например ИБ).

Тебе нужно:
1) поставить Python  
2) поставить 2 библиотеки  
3) создать бота у BotFather и взять токен  
4) вставить токен и имя Excel в config.py  
5) запустить quiz_bot.py  

---

## 1) Установи Python

Проверь, что Python есть.

**Windows:**  
1. Открой CMD или PowerShell  
2. Введи команду:

    python --version

**Mac / Linux:**  
1. Открой Terminal  
2. Введи команду:

    python3 --version

Если показалась версия — Python есть.  
Если нет — установи Python с python.org обычной установкой.

---

## 2) Установи библиотеки (один раз)

Открой терминал в папке проекта.

**Windows:**

    pip install pytelegrambotapi openpyxl

**Mac / Linux:**

    python3 -m pip install pytelegrambotapi openpyxl

---

## 3) Создай бота в Telegram и получи токен

1. В Telegram открой @BotFather  
2. Введи:

    /newbot

3. Он спросит имя — введи любое, например:

    IB Quiz Bot

4. Он спросит username — обязательно заканчивается на `bot`, например:

    ib_quiz_7class_bot

5. BotFather пришлёт TOKEN, выглядит так:

    1234567890:AAE.............

Скопируй TOKEN.

---

## 4) Вставь токен и Excel в config.py

Открой файл config.py и сделай так:

    TOKEN = "ТВОЙ_ТОКЕН_ОТ_BOTFATHER"
    XLS_PATH = "questions_infosec.xlsx"
    SHUFFLE_QUESTIONS = True
    SHOW_CORRECT_ON_WRONG = True

Сохрани файл.

Если делаешь другую тему — просто меняешь Excel:

    XLS_PATH = "questions_steganography.xlsx"

---

## 5) Заполни Excel с вопросами

Открой questions_infosec.xlsx (или свой файл).

Первая строка — названия колонок:

- question  
- option1  
- option2  
- option3  
- option4  
- correct_option  

Пример строки:

- question: Что такое фишинг?  
- option1: Спам  
- option2: Обман ради пароля  
- option3: Вирус  
- option4: Сайт школы  
- correct_option: 2  

Правила:
- вариантов всегда 4  
- correct_option только 1, 2, 3 или 4  
- сколько строк добавишь — столько вопросов будет  

Сохрани Excel.

---

## 6) Запусти бота

Открой терминал в папке проекта.

**Windows:**

    python quiz_bot.py

**Mac / Linux:**

    python3 quiz_bot.py

Если всё нормально, будет:

    Бот запущен...

Не закрывай терминал, иначе бот выключится.  
Остановить бота:

    Ctrl + C

---

## 7) Проверь бота в Telegram

1. Найди бота по username  
2. Введи:

    /start

3. Введи:

    /quiz

4. Придёт вопрос и кнопки ответов  
5. Отвечай до конца — бот покажет результат  

---

## Если что-то не работает

**Случай 1: в терминале ошибка 401 Unauthorized**  
Причина: неправильный токен.  
Решение: вставь токен заново в config.py.

**Случай 2: бот пишет “Вопросов не найдено”**  
Причина: Excel не найден или колонки не такие.  
Решение:
- Excel должен лежать рядом с quiz_bot.py (или путь в XLS_PATH должен быть верный)  
- колонки должны называться ровно так:  
  question, option1, option2, option3, option4, correct_option

**Случай 3: ошибка про telebot/openpyxl**  
Причина: не установлены библиотеки.  
Решение: повтори шаг 2.

---

Готово.  
Для новой темы: новый Excel → поменять XLS_PATH → снова запустить бота.
