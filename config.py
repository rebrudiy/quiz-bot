"""
config.py — настройки бота.

Для каждого проекта меняешь ТОЛЬКО:
- TOKEN
- XLS_PATH

Excel-файл ДЛЯ ОДНОЙ ТЕМЫ.

Формат Excel:
question | option1 | option2 | option3 | option4 | correct_option
"""

TOKEN = "PASTE_YOUR_TOKEN_HERE"

# файл вопросов (отдельный на тему)
XLS_PATH = "questions_steganography.xlsx"

SHUFFLE_QUESTIONS = True
SHOW_CORRECT_ON_WRONG = True
