from fishs import *
from fish_functions import *

def separator():
    print()
    print("=="*20)
    print()




def separator_2():
    print()
    print()
    print("=="*20)
    print("=="*20)
    print()
    print()




def menu_admin():
    input("нажми enter ")
    separator()
    print("напиши цифру 1 для добовления продукта")
    print("напиши цифру 2 чтобы найти по id")
    print("напиши цифру 3 чтобы вывести все продукты")
    print("напиши цифру 4 чтобы сортировать товар")
    print("напиши цифру 5 чтобы изменить пороль")
    print("напиши цифру 6 чтобы зайти в аккаунт покупателя")
    print("напиши цифру 7 чтобы сохранить для печати")
    print("напиши цифру 8 чтобы сохранить для загрузки ")
    print("напиши цифру 9 чтобы загрузить из файла")
    print("напиши цифру 10 чтобы в католог с напитками")
    print("напиши цифру 0 для выхода")
    separator_2()
    while True:
        try:
            user_number=int(input("введи число: "))
            separator()
            if 0<= user_number<=10:
                return user_number
            print("вы ввели не то число")
        except:
            print("вы ввели не число")




def sort_prodykt():
    separator()
    print("напиши цифру 1 чтобы вывести по размеру")
    print("напиши цифру 2 чтобы вывести по названию")
    print("напиши цифру 3 чтобы вывести по приготовлению")
    print("напиши цифру 4 чтобы вывести по цене")
    print("напиши цифру 5 чтобы отсортировать от большего к меньшему по весу ")
    print("напиши цифру 6 отсортировать от большего к меньшему по весу ")
    print("напиши цифру 7 чтобы найти по виду ")
    separator()
    
    while True:

        try:
            state_sort=int(input("напиши сюда число: "))
            if state_sort>=1 and state_sort<=7:
                return state_sort
            print("вы ввели слишком маленькоое или слишком большое слово ")
        except:
            print("вы ввели не число")
    



def user_menu():
    input("нажми enter ")
    separator()
    print("напиши цифру 1 чтобы найти по id")
    print("напиши цифру 2 чтобы вывести все продукты")
    print("напиши цифру 3 чтобы зайти в категорию сортировок товаров ")
    print("напиши цифру 4 чтобы войти в аккаунт продовца ")
    print("напиши цифру 5 чтобы сохранить для печати ")
    print("напиши цифру 6 чтобы зайти в категорию напитков")

    print("напиши цифру 0 для выхода")
    separator()
    while True:
        try:
            user_number= int(input("введи число: "))
            if 0<=user_number<=6:
                break
        except:
            print("вы ввели не число")
    return user_number




def drink_menu():
    print("напиши цифру 1 чтобы добавить новый напиток")
    print("напиши цифру 2 чтобы найти по id ")
    print("напиши цифру 3 чтобы сортировать ")
    print("напиши цифру 4 чтобы вывести все напитки")
    print("напиши цифру 0 для выхода")
    while True:
        try:
            admine_drink_numder=int(input("напиши нужную цифру: "))
            if admine_drink_numder>=0 or admine_drink_numder<=4:
                return admine_drink_numder
        except:
            print("вы ввели не число")
        




def sort_admine_or_user_menu():
    print("напиши цифру 1 чтобы вывести по названию ")
    print("напиши цифру 2 чтобы отсортировать по объёму")
    print("напиши цифру 3 чтобы отсортировать по цене")
    print("напиши цифру 4 чтобы отсортировать количеству")
    while True:
        try:
            admine_sort_numder=int(input("напиши нужную цифру: "))
            if admine_sort_numder>=1 or admine_sort_numder<=4:
                return admine_sort_numder
        except:
            print("вы ввели не число")
        

def drink_id_menu():
    print("напиши цифру 1 чтобы удалить")
    print("напиши цифру 2 чтобы пополнить напитки")
    print("напиши цифру 3 чтобы изменить")
    print("напиши цифру 4 чтобы купить")

    while True:
        try:
            admine_sort_id_numder=int(input("напиши нужную цифру: "))
            if admine_sort_id_numder>=1 or admine_sort_id_numder<=4:
                return admine_sort_id_numder
        except:
            print("вы ввели не число")
        




def drink_menu_user():
        print("напиши цифру 1 чтобы найти по id ")
        print("напиши цифру 2 чтобы сортировать ")
        print("напиши цифру 3 чтобы вывести все напитки")
        print("напиши цифру 0 для выхода")
        while True:
            try:
                user_drink_numder=int(input("напиши нужную цифру: "))
                if user_drink_numder>=0 or user_drink_numder<=3:
                    return user_drink_numder
            except:
                print("вы ввели не число")




def user_drink_id_menu():
    print("напиши цифру 1 чтобы купить")

    while True:
        try:
            user_sort_id_numder=int(input("напиши нужную цифру: "))
            if user_sort_id_numder==1:
                return user_sort_id_numder
        except:
            print("вы ввели не число")
