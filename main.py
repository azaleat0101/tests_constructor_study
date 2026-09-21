from datetime import date


def get_test_title():
    return input("Введите название теста: ")


def get_author():
    return input("Введите имя автора теста: ")


def format_header(title, author):
    """Формирует заголовок теста с текущей датой."""
    return f"Тест: {title}\nАвтор: {author}\nДата: {date.today()}"


def add_question():
    """
    Добавление вопроса: запрашивает текст, варианты и правильный ответ.
    Возвращает три значения (текст, варианты, номер правильного ответа).
    """
    question = input("Введите текст вопроса: ")
    options = input("Введите варианты ответов (например: 1. Да; 2. Нет): ")
    correct = input("Введите номер правильного ответа: ")
    return question, options, correct


def ask_question(question, options, correct):
    """Задаёт вопрос и проверяет ответ пользователя."""
    print(f"\nВопрос: {question}")
    print(f"Варианты: {options}")
    user_answer = input("Ваш ответ (номер): ")

    if user_answer.isdigit() and int(user_answer) == int(correct):
        return "Верно!"
    elif user_answer.isdigit():
        return f"Неверно. Правильный ответ: {correct}"
    else:
        return "Ошибка: введите число."


def main():
    print("--- Конструктор тестов ---")
    title = get_test_title()
    author = get_author()
    print("\n" + format_header(title, author))

    # Добавление вопроса
    question, options, correct = add_question()

    # Прохождение теста
    result = ask_question(question, options, correct)

    # Вывод результата
    print(result)


if __name__ == "__main__":
    main()