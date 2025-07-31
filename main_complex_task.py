questions = [
    {
        "question": "Кто был первым президентом России после развала СССР?",
        "options": ["A) Сталин", "B) Борис Ельцин", "C) Владимир Путин", "D) Михаил Горбачёв"],
        "answer": "B"
    },
    {
        "question": "Какой город является столицей Казахстана?",
        "options": ["A) Алматы", "B) Астана", "C) Шымкент", "D) Караганда"],
        "answer": "B"
    },
    {
        "question": "Какое самое большое озеро на Земле?",
        "options": ["A) Каспийское море", "B) Байкал", "C) Верхнее озеро", "D) Виктория"],
        "answer": "A"
    },
    {
        "question": "Какое место занимает Казахстан по площади на земле?",
        "options": ["A) Первое", "B) Пятое", "C) Девятое", "D) Одиннадцатое"],
        "answer": "C"
    },
    {
        "question": "Какой язык является государственным в Казахстане?",
        "options": ["A) Русский", "B) Английский", "C) Казахский", "D) Узбекский"],
        "answer": "C"
    },
    {
        "question": "Какой город является самым крупным в Казахстане?",
        "options": ["A) Алматы", "B) Нур-Султан", "C) Шымкент", "D) Караганда"],
        "answer": "A"
    }
]

score = 0

for i, question in enumerate(questions):
    print(f"Вопрос {i + 1}: {question['question']}")
    for option in question['options']:
        print(option)
    
    user_answer = input("Ваш ответ (A, B, C, D): ").strip().upper()
    
    if user_answer == question['answer']:
        print("Правильно!")
        score += 1
    else:
        print(f"Неправильно! Правильный ответ: {question['answer']}")
    
    print()  # Пустая строка для разделения вопросов
print(f"Ваш итоговый счет: {score} из {len(questions)}")
if score == len(questions):
    print("Поздравляем! Вы ответили на все вопросы правильно!")