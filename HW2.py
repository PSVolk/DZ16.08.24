class StringStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []

    def push(self, string):
        if len(self.stack) < self.max_size:
            self.stack.append(string)
        else:
            print("Стек переполнен.")

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print("Стек пуст.")
            return None

    def count(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size

    def clear(self):
        self.stack = []

    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            print("Стек пуст.")
            return None

def main():
    max_size = int(input("Введите максимальный размер стека: "))
    stack = StringStack(max_size)

    while True:
        print("\nМеню:")
        print("1. Поместить строку в стек")
        print("2. Вытолкнуть строку из стека")
        print("3. Подсчитать количество строк в стеке")
        print("4. Проверить, пуст ли стек")
        print("5. Проверить, полон ли стек")
        print("6. Очистить стек")
        print("7. Получить значение верхней строки без её выталкивания")
        print("0. Выйти")

        choice = input("Выберите операцию (0-7): ")

        if choice == "1":
            string = input("Введите строку: ")
            stack.push(string)
        elif choice == "2":
            print("Удалена строка:", stack.pop())
        elif choice == "3":
            print("Количество строк в стеке:", stack.count())
        elif choice == "4":
            if stack.is_empty():
                print("Стек пуст.")
            else:
                print("Стек не пуст.")
        elif choice == "5":
            if stack.is_full():
                print("Стек полон.")
            else:
                print("Стек не полон.")
        elif choice == "6":
            stack.clear()
            print("Стек очищен.")
        elif choice == "7":
            print("Верхняя строка в стеке:", stack.top())
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
