
from fishs import *
from menu_main_fish import *
import random


global_id_fish=0
global_id_drink=0




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

# ввод данных в датакласс
def input_fish_dataclass()-> Fish:
    print(f"пример(рыба | икра | водоросль)")
    product_name=correct_input_word("напиши название продукта: ", "рыба | икра | водоросль", 4, 9)
    separator()


    print('пример( белая акулы | икра лосося | ламинария)')
    view=correct_input('напиши вид продукта: ', 3, 43)
    separator()


    print('пример(парной | свежий | замороженый)')
    preparetion=correct_input_word("напиши приготовления продукта: ","парной | свежий | замороженый",6,11)
    separator()


    print("пример(18:39 4 марта)")
    date_of_manufacture=correct_input_date_of_manufacture("напиши время вылова или изготовления: ", 10 , 18)
    separator()


    print('пример(18.25 кг)')
    weight=correct_input_float("напиши вес продукта в кг: ", 0 , 1000000000000)
    separator()

    # проверка на нужный ввод
    print('пример(18000) водить только цифры ')
    price=price_input_by_int("напиши цену продукта: ", 0, 10000000000000 )
    separator()

    
    print('пример(большой | средний | маленький)')
    size=correct_input_word("напиши размер продукта: ", "большой | средний | маленький",7 ,9)
    separator_2()


    return Fish(product_name=product_name, view=view, preparetion=preparetion, date_of_manufacture=date_of_manufacture, weight=weight, price=price, size=size)




# проверяет, что пользователь ввёл целое число в нужном диапазоне
def price_input_by_int(opisanie, min_pazmer, max_razmer ):
    while True:

        try:
            number=int(input(opisanie))
            if number>=min_pazmer and number<=max_razmer:
                return number
        except:
            print("вы ввели не число")





# напитки

# генерирует стартовый ассортимент напитков в магазин
def generation_drink(drinks:list[Drink]):
    volume=0.5
    prince=90
    
    new_drink=Drink(drink_name="Fanta", volume=volume , price=prince,  quantity=random.randint(100, 1000))
    new_drink.id=id_drink()
    input_drink_by_list(drinks, new_drink)


    new_drink=Drink(drink_name="Spite", volume=volume, price=prince,  quantity=random.randint(100, 1000))
    new_drink.id=id_drink()
    input_drink_by_list(drinks, new_drink)


    volume=1.0
    new_drink=Drink(drink_name="вода", volume=volume, price=50,  quantity=random.randint(100, 1000))
    new_drink.id=id_drink()
    input_drink_by_list(drinks, new_drink)


    volume=0.2
    new_drink=Drink(drink_name="морской коктель", volume=volume, price=250,  quantity=random.randint(100, 1000))
    new_drink.id=id_drink()
    input_drink_by_list(drinks, new_drink)
        



def input_drink_by_dataclass_Drink():
    separator()
    drink_name=correct_input_word("напиши название напитка: ", "fanta | sprite | pepsi", 2, 15)
    separator()


    volume=correct_input_float("напиши объём напитка в литрах: ", 0 , 1000000000)
    separator()


    price=price_input_by_int("напиши цену напитка: ", 0, 10000000000)
    separator()


    quantity=price_input_by_int("напиши количество напитков: ", 0, 10000000)
    separator_2()

    return Drink(drink_name=drink_name,  volume=volume,  price=price,  quantity=quantity )




def input_drink_by_list(drinks:list[Drink], new_drink):
    drinks.append(new_drink)





def id_drink():
    global global_id_drink
    global_id_drink+=1
    return global_id_drink





def search_by_id_drink(drinks:list[Drink], ID):
    for drink in drinks:
        if ID == drink.id:
            return drink
    print("вы ввели id каторово несуществует")
    
    
    id=int(input("введите id: "))
    
    search_by_id(id, drinks)
   




def del_drink_by_id(drinks:list[Drink], pop_drink):
    drinks.remove(pop_drink)





def replenish_quantity(drinks:list[Drink], replenish_drink):
    while True:
        try:
            replenish=int(input("напишите на сколько вы хотите пополнить напиток "))
            if replenish>0 and replenish<=100000000000:
                print("пополнено")
                break

            
        except:
            print("вы ввели не числи")

    old_quantity=replenish_drink.quantity

    replenish_drink.quantity=old_quantity+replenish





def to_change_drink(drinks:list[Fish], new_drink):
    new_drink.drink_name =correct_input_word("напиши название напитка: ", "fanta | sprite | pepsi", 2, 15)
    new_drink.volume = correct_input_float("напиши объём напитка в литрах: ", 0 , 1000000000)
    new_drink.price=price_input_by_int("напиши количество напитков: ", 0, 10000000)
    new_drink.quantity = price_input_by_int("напиши количество напитков: ", 0, 10000000)





def buy_drink(drinks_buy:list[Drink], id_buy_drink, drinks:list[Drink]):
    print("какое количество напитков вы хотите приобрести? ")
    while True:
        try:
            quantity=int(input("напиши колличество напитков: "))
            if quantity>0 or quantity<10000000000000000000000000000:
                if id_buy_drink.quantity >= quantity:
                    id_buy_drink.quantity = id_buy_drink.quantity - quantity
                    print("вы купили напитки")
                print("такого количества нету на складе")

            else:   
                print("вы ввели слишком большое или слишком маленькое число")
        except:
            print("вы ввели не число")

        id_buy_drink.quantity=quantity

        drinks_buy.append=id_buy_drink


def print_one_drink(drink_one):
    print("=="*20)
    print(f"название напитка - {drink_one.drink_name}")
    print(f"объём напитка - {drink_one.volume}")
    print(f"цена напитка  - {drink_one.price}")
    print(f"количесто  - {drink_one.quantity}")
    print(f"Ид - {drink_one.id}")

def print_drinks(drinks:list[Drink]):
    for drink_one in drinks:
        print_one_drink(drink_one)

def sort_by_drink_name(drinks:list[Drink], necessary_drink_name):
    for productname in drinks:
        if productname.product_name == necessary_drink_name:
            print_one_fish(productname)


# до какого объёма
def sort_by_volume(drinks:list[Drink], necessary_volume_max, necessary_volume_min):
    for productname in drinks:
        if productname.volume <= necessary_volume_max or productname.volume >= necessary_volume_min :
            print_one_fish(productname)



# до какой цены
def sort_by_price(drinks:list[Drink], necessary_price_max,necessary_price_min):
    for productname in drinks:
        if productname.price <= necessary_price_max or productname.price >= necessary_price_min:
            print_one_fish(productname)


# от какого количества напитков
def sort_by_quantity(drinks:list[Drink], necessary_quantity_max, necessary_quantity_min):
    for productname in drinks:
        if productname.quantity >= necessary_quantity_max or productname.quantity >= necessary_quantity_min:
            print_one_fish(productname)

            


def correct_input_date_of_manufacture(opisanie,  min_pazmer, max_razmer):
    while True:
        try:
            correct_word=input(opisanie).lower().strip()
            if len(correct_word)>=min_pazmer and len(correct_word)<=max_razmer:
                if correct_word[2]==":" and correct_word[5]==" ":

                    return correct_word
                print("вы ввели дату не так")
            print("вы ввели слишком маленькоое или слишком большое слово ")
        except:
            print("вы ввели что-то не то")






def correct_input_word(opisanie, clova, min_pazmer, max_razmer ):
    while True:
        try:
            print(f"напиши одно из этих слов {clova}")
            correct_word=input(opisanie).lower().strip()
            if correct_word in clova:
                if len(correct_word)>=min_pazmer and len(correct_word)<=max_razmer:

                    return correct_word
                print("вы ввели слишком маленькое или слишком большое число")
            print("вы ввели не те слова ")
        except:
            print("вы ввели что-то не то")




def correct_input(opisanie, min_pazmer, max_razmer):
    while True:
        try:
            correct_word=input(opisanie).lower().strip()
            if len(correct_word)>=min_pazmer and len(correct_word)<=max_razmer:
                return correct_word
            print("вы ввели слишком маленькоое или слишком большое слово ")
        except:
            print("вы ввели что-то не то")

def correct_input_float(opisanie,min_pazmer, max_razmer):
    while True:
        try:
            correct_float=float((input(opisanie)))  
            if correct_float>=min_pazmer and correct_float<=max_razmer:
                return correct_float
            print("слишком маленькое или слишком большое")     
        except:
            print("ты ввёл не число")  

    
    


def input_prodykt_by_list(prodykt:list[Fish], new_fish:Fish):
    prodykt.append(new_fish)




def id_fish():
    global global_id_fish
    global_id_fish+=1
    return global_id_fish
    
    


# находит продукт по id, если не нашёл - спрашивает снова
def search_by_id(ID, prodykt:list[Fish]):
    for fisshi in prodykt:
        if ID == fisshi.id:
            return fisshi
        
    print("вы ввели id каторово несуществует")
    
    
    ib=int(input("введите id: "))
    
    search_by_id(ib, prodykt)




def pop_id_fish(fisshi, prodykt:list[Fish]):
    prodykt.remove(fisshi)




def print_one_fish(fisshi):
    print("=="*20)
    print(f"название продукта -{fisshi.product_name}")
    print(f"вид продукта - {fisshi.view}")
    print(f"приготовление - {fisshi.preparetion}")
    print(f"дата изготовления - {fisshi.date_of_manufacture}")
    print(f"вес - {fisshi.weight}")
    print(f"цена - {fisshi.price} рублей")
    print(f"размер - {fisshi.size}")
    print(f"Ид - {fisshi.id}")




def print_products(prodykt:list[Fish]):
    for fisshi in prodykt:
        print_one_fish(fisshi)




def print_by_id_fish(fisshi):
    print_one_fish(fisshi)




def updeit_by_id(fisshi):
    fisshi.product_name = correct_input_word("напиши название продукта: ", "рыба | икра | водоросль", 4, 9)
    fisshi.view = correct_input('напиши вид продукта: ', 3, 43)
    fisshi.preparetion = correct_input_word("напиши приготовления продукта: ","парной | свежий | замороженый",6,11)
    fisshi.date_of_manufacture = correct_input_date_of_manufacture("напиши время вылова или изготовления: ", 10 , 18)
    fisshi.weight = correct_input("напиши вес продукта в кг: ", 2 , 10)
    while True:
        try:

            fisshi.price = int(input("Новая цена: "))
            if fisshi.price>0 and fisshi.tsena<100000000000000000:
                break
        except:
            print("вы ввели не число")
    fisshi.size = correct_input_word("напиши размер продукта:", "большой | средний | маленький",7 ,9)




def print_by_size(necessary_size, prodykt:list[Fish]):
    for razmer in prodykt:
        if razmer.size == necessary_size:
            print_one_fish(razmer)
    
    print("продукты кончились или их нету")



# некак не используетсь!!!!!!!!!!!!!!!!!!!!!!!!!
def print_by_product_name(necessary_product_name, prodykt:list[Fish]):
    for productname in prodykt:
        if productname.product_name == necessary_product_name:
            print_one_fish(productname)

    print("продукты кончились или их нету")




def print_by_preparetion(necessary_preparetion, prodykt:list[Fish]):


    for preparetions in prodykt:
        
        if preparetions.preparetion == necessary_preparetion:
            print_one_fish(preparetions)
        

    print("продукты кончились или их нету")




def check_by_int(text):
    while True:

        try:
            number=int(input(text))
            if number>0:

                return number
        except:
            print("вы ввели не число")
    
        

def check_by_str(text, correct_word):
    while True:
        try:
            print(f"напиши только одно из этих слов - {correct_word}")
            nuzhnyy=input(text).lower().strip()
            if nuzhnyy in correct_word:

                return nuzhnyy
            print("вы ввели не те слова")
        except:
            print("ты ввёл чтото не то")




def admin_state__by_id_sort():
    while True:
        try:
            state=int(input("введи число "))
            if 0<= state<=3:
                return state
            print("вы ввели не то число")
        except:
            print("вы ввели не число")





correct_sumvol=0





def summa(prodykt:list[Fish]):
    while True:
        try:
            summa=int(input("введите сумму до которово будет показыватся продукты: ")) 
            break
        except:
            print("вы вели не число")

    for vse in prodykt:
        if vse.price <= summa:
            print_one_fish(vse)
            correct_sumvol=1
    if correct_sumvol!=1:
        print("товары были не найдены")
        



def new_porol():
    porol=int(input("напиши новый пароль: "))
    return porol




def input_porol(porol):
    print("в какой аккаунт вы хотите зайти? ")
    print("1 - в аккаунт покупателя")
    print("2 - в аккаунт продовца")
    while True:
        try:
            start=int(input("введи число: "))
            if start==1 or start==2:
                break

        except:
            print("вы ввели не чесло ")

    if start == 1:
        return "no"


    elif start == 2:
        while True:
            try:
                user_porol=int(input("введи пороль: "))
                break
            except:
                print("вы ввели не число")

        if user_porol == porol:
            print("вы вошли как продовец")
            return "cypher"
        print("ты чё пороль не знаешь? или хочешь зайти на аккаунт продовца?")
    input_porol(porol)
                
            



def user_state_by_id_sort():
    while True:
        try:
            state=int(input("введи число "))
            if 0<= state<=1:
                return state
            print("вы ввели не то число")
        except:
            print("вы ввели не число")




def file_neim_vvod():
    opisanie="напиши название файла: "
    while True:
        try:
            file_neim=input(opisanie)
            return file_neim
        except:
            print("вы ввели что-то не то")


# сохраняет каталог продуктов в файл для печати
def save_to_file_for_print(file_neim, prodykt:list[Fish]):
    with open(file_neim, "w", encoding="utf-8") as file:
            while True:
                try:
                    file.write("католог рыбного магазина - 'JapaneseWormFromChina 🐛'\n\n")
                    for fisshi in prodykt:

                        file.write(f"print('=='*20\n")
                        file.write(f"название продукта -{fisshi.product_name}\n")
                        file.write(f"вид продукта - {fisshi.view}\n")
                        file.write(f"приготовление - {fisshi.preparetion}\n")
                        file.write(f"дата изготовления - {fisshi.date_of_manufacture}\n")
                        file.write(f"вес - {fisshi.weight}\n")
                        file.write(f"цена - {fisshi.price} рублей\n")
                        file.write(f"размер - {fisshi.size}\n")
                        file.write(f"Ид - {fisshi.id}\n\n")
                    break                    
                except:
                    print("что то сломалось")
                



# сохраняет продукты в файл для последующей загрузки
def save_to_file_to_upload(prodykt:list[Fish]):
    with open("upload2.txt", "w", encoding="utf-8") as file:
            while True:
                try:
                    file.write(f"{len(prodykt)}\n")
                    for fisshi in prodykt:

                        
                        file.write(f"{fisshi.product_name}\n")
                        file.write(f"{fisshi.view}\n")
                        file.write(f"{fisshi.preparetion}\n")
                        file.write(f"{fisshi.date_of_manufacture}\n")
                        file.write(f"{fisshi.weight}\n")
                        file.write(f"{fisshi.price}\n")
                        file.write(f"{fisshi.size}\n")
                        file.write(f"{fisshi.id}\n")
                    
                    break                    
                except:
                    print("что то сломалось")




# загружает продукты из файла обратно в программу
def  upload_from_file(prodykt:list[Fish]):
    
        with open("upload2.txt", "r", encoding="utf-8") as file:
            count_produkt = int(file.readline().strip())
            for _ in range(count_produkt):
                prodykt.append(Fish(product_name=file.readline().strip(), view=file.readline().strip(), preparetion=file.readline().strip(), date_of_manufacture=file.readline().strip(), weight=float(file.readline().strip()), price=int(file.readline().strip()), size=file.readline().strip(), id=id_fish()) )
                id_trash=file.readline().strip()
            print("файл загружен")   
    


# пузырьковые сортировки
def sort_by_weight_desc(prodykt:list[Fish]):
    sort=0
    for i in range(len(prodykt)):
        for j in range(len(prodykt)-1 - i):
            if prodykt[j].weight > prodykt[j+1].weight:
                sort=prodykt[j].weight
                prodykt[j].weight = prodykt[j+1].weight
                prodykt[j+1].weight = sort
    print("сортировка закончена")




def sort_by_price(prodykt:list[Fish]):
    sort=0
    for i in range(len(prodykt)):
        for j in range(len(prodykt)-1 - i):
            if prodykt[j].price > prodykt[j+1].price :
                sort=prodykt[j].price 
                prodykt[j].price  = prodykt[j+1].price 
                prodykt[j+1].price  = sort
    print("сортировка закончена")


def print_by_sort_view(prodykt:list[Fish]):
    while True:
        try:
            necessary_view=input("нипиши сюда нажный вид для поиска: ").lower().strip()
            if len(necessary_view)>=3 and len(necessary_view)<=43:

                break
            print("вы ввели слтшком маленькое или слишком большое слово ")
        except:
            print("вы ввели что-то не то")
    for fisshi in prodykt:
        if fisshi.view == necessary_view:
            print_one_fish(fisshi)

# пороль 3455
