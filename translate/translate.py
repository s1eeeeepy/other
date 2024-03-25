from sys import exit
from time import sleep

end = ["exit", "выход"]
while True:
    text = input("Введите текст для перевода: ")
    if text.lower() not in end:
        for word in text.split():
            print("Квa", end=" ")
        print()
        print("Для выхода напишите exit/выход.")
    else:
        print("Удачного Вам ква!")
        sleep(3)
        exit()
