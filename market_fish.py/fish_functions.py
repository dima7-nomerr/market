from Fishs import Fish
global_id_fish=0
kesh=0
def input_fish_market()-> Fish:
    print("пример(рыба | икра | водоросли)")
    mazvanie_prodykta=input("напиши название продукта: ")
    print()
    print('пример( белая акулы | икра лосося | ламинария)')
    vid=input("напиши вид продукта: ")
    print()
    print('пример(парной | свежий | замороженый)')
    prigotovlenie=input("напиши приготовления продукта: ")
    print()
    print("пример(18:39 4 марта)")
    data_isgotovleni=input("напиши время вылова или изготовления: ")
    print()
    print('пример(18.25 кг)')
    ves=input("напиши вес продукта в кг: ")
    print()
    print('пример(18000) водить только цифры ')
    while True:
        try:
            tsena=int(input("напиши цену продукта: "))
            if tsena>0:
                break
        except:
            print('вы ввели не число')
    print()
    print('пример(большой | средний | маленький)')
    razmer=input("напиши размер продукта:")
    return Fish(mazvanie_prodykta=mazvanie_prodykta, vid=vid, prigotovlenie=prigotovlenie, data_isgotovleni=data_isgotovleni, ves=ves, tsena=tsena, razmer=razmer)
def menu():
    input("нажми enter ")
    print("напиши цифру 1 для добовления продукта")
    print("напиши цифру 2 чтобы найти по id")
    print("напиши цифру 3 чтобы вывести все продукты")
    print("напиши цифру 4 чтобы вывести по размеру")
    print("напиши цифру 5 чтобы вывести по названию")
    print("напиши цифру 6 чтобы вывести по приготовлению")
    print("напиши цифру 7 чтобы вывести по цене")
    print("напиши цифру 8 чтобы изменить пороль")
    print("напиши цифру 9 чтобы стать покупателем ")
    print("напиши цифру 0 для выхода")
    while True:
        try:
            polizovatel_tsufra=int(input("введи число: "))
            if 0<= polizovatel_tsufra<=9:
                return polizovatel_tsufra
            print("вы ввели не то чесло")
        except:
            print("вы ввели не число")
    
    

def input_prodykt_B_list(prodykt:list[Fish], new_fish:Fish):
    prodykt.append(new_fish)

def id_fish():
    global global_id_fish
    global_id_fish+=1
    return global_id_fish
    
def id_poisk(ID, prodykt:list[Fish]):
    for fisshi in prodykt:
        if ID == fisshi.id:
            return fisshi
        
    print("вы ввели id каторово несуществует")
    
    
    ibd=int(input("введите id: "))
    
    id_poisk(ibd, prodykt)



def pop_id_fish(fisshi, prodykt:list[Fish]):
    prodykt.remove(fisshi)

def print_one_fish(fisshi):
    print("=="*20)
    print(f"название продукта -{fisshi.mazvanie_prodykta}")
    print(f"вид продукта - {fisshi.vid}")
    print(f"приготовление - {fisshi.prigotovlenie}")
    print(f"дата изготовления - {fisshi.data_isgotovleni}")
    print(f"вес - {fisshi.ves}")
    print(f"цена - {fisshi.tsena} рублей")
    print(f"размер - {fisshi.razmer}")
    print(f"Ид - {fisshi.id}")

def print_prodyktov(prodykt:list[Fish]):
    for fisshi in prodykt:
        print_one_fish(fisshi)

def print_id_fish(fisshi):
    print_one_fish(fisshi)

def updeit_po_id(fisshi):
    fisshi.mazvanie_prodykta = input("Новое название: ")
    fisshi.vid = input("Новый вид: ")
    fisshi.prigotovlenie = input("Новое приготовление: ")
    fisshi.data_isgotovleni = input("Новая дата изготовления: ")
    fisshi.ves = input("Новый вес: ")
    while True:
        try:

            fisshi.tsena = int(input("Новая цена: "))
            if fisshi.tsena>0:
                break
        except:
            print("вы ввули не число")
    fisshi.razmer = input("Новый размер: ")

def print_po_razmery(nuzhnyy_razmer, prodykt:list[Fish]):
    for rezmer in prodykt:
        if rezmer.razmer == nuzhnyy_razmer:
            print_one_fish(rezmer)
    
    print("продукты кончились или их нету")

def print_po_mazvanie_prodykta(nuzhnyy_mazvanie_prodykta, prodykt:list[Fish]):
    for mazvanie_prodykt in prodykt:
        if mazvanie_prodykt.mazvanie_prodykta == nuzhnyy_mazvanie_prodykta:
            print_one_fish(mazvanie_prodykt)

    print("продукты кончились или их нету")

def print_po_prigotovlenie(nuzhnyy_prigotovlenie, prodykt:list[Fish]):


    for prigotovleni in prodykt:
        
        if prigotovleni.prigotovlenie == nuzhnyy_prigotovlenie:
            print_one_fish(prigotovleni)
        

    print("продукты кончились или их нету")

def proverka(suda):
    while True:

        try:
            stoto=int(input(suda))
            return stoto
        except:
            print("вы ввели не число")
    
        

def proverka2(suda):
    while True:
        try:
            nuzhnyy=input(suda)
            return nuzhnyy
        except:
            print("ты ввёл чтото не то")


def stoto_tam_po_id():
    while True:
        try:
            polizovateli=int(input("введи число "))
            if 0<= polizovateli<=3:
                return polizovateli
            print("вы ввели не то число")
        except:
            print("вы ввели не число")
rre=0
def summa(prodykt:list[Fish]):
    while True:
        try:
            summa=int(input("введите сумму до которово будет показыватся продукты: ")) 
            break
        except:
            print("вы вели не число")

    for vse in prodykt:
        if vse.tsena <= summa:
            print_one_fish(vse)
            rer=1
    if rer!=1:
        print("товары были не найдены")
        


def poroliiii():
    porol=int(input("напиши новый пароль: "))
    return porol


def pol(porol):
    print("если ты продовец введи число 1 если ты покупатель введи число 2")
    while True:
        try:
            kto=int(input("введи число: "))
            if kto==1 or kto==2:
                break

        except:
            print("вы ввели не чесло ")

    if kto == 1:
        return "no"


    elif kto == 2:
        while True:
            try:
                pol_poroli=int(input("введи пороль: "))
                break
            except:
                print("вы ввели не число")

        if pol_poroli == porol:
            print("вы вошли как продовец")
            return "klys"
        print("ты чё пороль не знаешь? или хочешь зайти на аккаунт продовца?")
    pol(porol)
                
            

def market():
    input("нажми enter ")
    print("напиши цифру 1 чтобы найти по id")
    print("напиши цифру 2 чтобы вывести все продукты")
    print("напиши цифру 3 чтобы вывести по размеру")
    print("напиши цифру 4 чтобы вывести по названию")
    print("напиши цифру 5 чтобы вывести по приготовлению")
    print("напиши цифру 6 чтобы вывести по цене")
    print("напиши цифру 7 чтобы стать торговцем ")
    print("напиши цифру 0 для выхода")
    while True:
        try:
            tsufra= int(input("введи число: "))
            if 0<=tsufra<=7:
                break
        except:
            print("вы ввели не число")
    return tsufra

def stoto_tam_po_id2():
    while True:
        try:
            polizovate=int(input("введи число "))
            if 0<= polizovate<=1:
                return polizovate
            print("вы ввели не то число")
        except:
            print("вы ввели не число")