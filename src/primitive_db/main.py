#!/usr/bin/env python3
from .engine import welcome


def main():
    welcome() 
    while True:
        command = input("Введите команду: ")  
        if command == "exit":
            print("До свидания!")
            break
        elif command == "help":
            welcome()
        else:
            print("Неизвестная команда. Попробуйте 'help'.")

if __name__ == "__main__":
    main() 
    