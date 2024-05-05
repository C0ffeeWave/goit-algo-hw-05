import re
from typing import Callable

def input_error(func):
    """
    Декоратор, який обробляє помилки введення для функцій.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            if isinstance(e, KeyError):
                return "Контакт не знайдено."
            elif isinstance(e, ValueError):
                return "Введіть ім'я та номер телефону, будь ласка."
            elif isinstance(e, IndexError):
                return "Невірна команда. Формат: команда [ім'я] [телефон]"
    return inner

@input_error
def add_contact(args, contacts):
    """
    Додає новий контакт.
    """
    if len(args) != 2:
        raise IndexError
    name, phone = args
    contacts[name] = phone
    return "Контакт додано."

@input_error
def change_contact(args, contacts):
    """
    Змінює існуючий контакт.
    """
    if len(args) != 2:
        raise IndexError
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Контакт оновлено."

@input_error
def show_phone(args, contacts):
    """
    Показує номер телефону для вказаного контакту.
    """
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name not in contacts:
        raise KeyError
    return contacts[name]

@input_error
def show_all(contacts):
    """
    Показує всі контакти.
    """
    if not contacts:
        return "Контакти не знайдено."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def parse_input(user_input):
    """
    Розбиває введену команду на команду та аргументи.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def main():
    """
    Головна функція програми.
    """
    contacts = {}
    print("Ласкаво просимо до бота-помічника!")
    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("До побачення!")
            break
        elif command == "hello":
            print("Як я можу вам допомогти?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Невірна команда.")

if __name__ == "__main__":
    main()