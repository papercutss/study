efinitions = {
    "python": "Язык программирования общего назначения.",
    "git": "Система контроля версий.",
    "алгоритм": "Последовательность действий для решения задачи.",
    "функция": "Блок кода, выполняющий определённую задачу."
}

word = input("Введите слово для поиска: ").lower()

if word in definitions:
    print(f"{word.capitalize()}: {definitions[word]}")
else:
    print("Слово не найдено в словаре.")
    choice = input("Хотите добавить определение для этого слова? (да/нет): ").lower()
    if choice == "да":
        definition = input("Введите определение: ")
        definitions[word] = definition
        print(f"Слово '{word}' добавлено в словарь.")