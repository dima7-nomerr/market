from Fishs import Fish
global_id_fish=0
kesh=0
def input_fish_market()-> Fish:
    print(f"пример(рыба | икра | водоросль)")
    mazvanie_prodykta=pravelnyy_vvod_clova("напиши название продукта: ", "рыба | икра | водоросль", 4, 9)
    print()
    print('пример( белая акулы | икра лосося | ламинария)')
    vid=pravelnyy_vvod('напиши вид продукта: ', 3, 43)
    print()
    print('пример(парной | свежий | замороженый)')
    prigotovlenie=pravelnyy_vvod_clova("напиши приготовления продукта: ","парной | свежий | замороженый",6,11)
    print()
    print("пример(18:39 4 марта)")
    data_isgotovleni=pravelnyy_vvod_data_isgotovleni("напиши время вылова или изготовления: ", 10 , 18)
    print()
    print('пример(18.25 кг)')
    ves=pravelnyy_vvod_float("напиши вес продукта в кг: ", 0 , 1000000000000)
    print()
    print('пример(18000) водить только цифры ')
    while True:
        try:
            tsena=int(input("напиши цену продукта: "))
            if tsena>0 and tsena<1000000000000:
                break
            print("вы ввели слишком маленькое или слишком большое число")
        except:
            print('вы ввели не число')
    print()
    print('пример(большой | средний | маленький)')
    razmer=pravelnyy_vvod_clova("напиши размер продукта: ", "большой | средний | маленький",7 ,9)
    return Fish(mazvanie_prodykta=mazvanie_prodykta, vid=vid, prigotovlenie=prigotovlenie, data_isgotovleni=data_isgotovleni, ves=ves, tsena=tsena, razmer=razmer)
def menu():
    input("нажми enter ")
    print("напиши цифру 1 для добовления продукта")
    print("напиши цифру 2 чтобы найти по id")
    print("напиши цифру 3 чтобы вывести все продукты")
    print("напиши цифру 4 чтобы сортировать товар")
    print("напиши цифру 5 чтобы изменить пороль")
    print("напиши цифру 6 чтобы стать покупателем")
    print("напиши цифру 7 чтобы сохранить для печати")
    print("напиши цифру 8 чтобы сохранить для загрузки ")
    print("напиши цифру 9 чтобы загрузить из файла")
    print("напиши цифру 0 для выхода")
    while True:
        try:
            polizovatel_tsufra=int(input("введи число: "))
            if 0<= polizovatel_tsufra<=9:
                return polizovatel_tsufra
            print("вы ввели не то число")
        except:
            print("вы ввели не число")

def pravelnyy_vvod_data_isgotovleni(opisanie,  min_pazmer, max_razmer):
    while True:
        try:
            pravelinoe_clovo=input(opisanie).lower().strip()
            if len(pravelinoe_clovo)>=min_pazmer and len(pravelinoe_clovo)<=max_razmer:
                if pravelinoe_clovo[2]==":" and pravelinoe_clovo[5]==" ":

                    return pravelinoe_clovo
                print("вы ввели дату не так")
            print("вы ввели слишком маленькоое или слишком большое слово ")
        except:
            print("вы ввели что-то не то")






def pravelnyy_vvod_clova(opisanie, clova, min_pazmer, max_razmer ):
    while True:
        try:
            print(f"напиши одно из этих слов {clova}")
            pravelinoe_clovo=input(opisanie).lower().strip()
            if pravelinoe_clovo in clova:
                if len(pravelinoe_clovo)>=min_pazmer and len(pravelinoe_clovo)<=max_razmer:

                    return pravelinoe_clovo
                print("вы ввели слишком маленькое или слишком большое число")
            print("вы ввели не те слова ")
        except:
            print("вы ввели что-то не то")

def pravelnyy_vvod(opisanie, min_pazmer, max_razmer):
    while True:
        try:
            pravelinoe_clovo=input(opisanie).lower().strip()
            if len(pravelinoe_clovo)>=min_pazmer and len(pravelinoe_clovo)<=max_razmer:
                return pravelinoe_clovo
            print("вы ввели слишком маленькоое или слишком большое слово ")
        except:
            print("вы ввели что-то не то")

def pravelnyy_vvod_float(opisanie,min_pazmer, max_razmer):
    while True:
        try:
            pravelinoe_float=float((input(opisanie)))  
            if pravelinoe_float>=min_pazmer and pravelinoe_float<=max_razmer:
                return pravelinoe_float
            print("слишком маленькое или слишком большое")     
        except:
            print("ты ввёл не число")  

    
def sort_prodykt():
    print("напиши цифру 1 чтобы вывести по размеру")
    print("напиши цифру 2 чтобы вывести по названию")
    print("напиши цифру 3 чтобы вывести по приготовлению")
    print("напиши цифру 4 чтобы вывести по цене")
    print("напиши цифру 5 чтобы отсортировать от большего к меньшему по весу ")
    print("напиши цифру 6 отсортировать от большего к меньшему по весу ")
    print("напиши цифру 7 чтобы найти по виду ")
    
    while True:

        try:
            admin_state_sort=int(input("напиши сюда число: "))
            if admin_state_sort>=1 and admin_state_sort<=7:
                return admin_state_sort
            print("вы ввели слишком маленькоое или слишком большое слово ")
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
    fisshi.mazvanie_prodykta = pravelnyy_vvod_clova("напиши название продукта: ", "рыба | икра | водоросль", 4, 9)
    fisshi.vid = pravelnyy_vvod('напиши вид продукта: ', 3, 43)
    fisshi.prigotovlenie = pravelnyy_vvod_clova("напиши приготовления продукта: ","парной | свежий | замороженый",6,11)
    fisshi.data_isgotovleni = pravelnyy_vvod_data_isgotovleni("напиши время вылова или изготовления: ", 10 , 18)
    fisshi.ves = pravelnyy_vvod("напиши вес продукта в кг: ", 2 , 10)
    while True:
        try:

            fisshi.tsena = int(input("Новая цена: "))
            if fisshi.tsena>0 and fisshi.tsena<100000000000000000:
                break
        except:
            print("вы ввели не число")
    fisshi.razmer = pravelnyy_vvod_clova("напиши размер продукта:", "большой | средний | маленький",7 ,9)

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

def proverka_na_int(text):
    while True:

        try:
            number=int(input(text))
            return number
        except:
            print("вы ввели не число")
    
        

def proverka_na_str(text, pravelinye_slova):
    while True:
        try:
            print(f"напиши только одно из этих слов - {pravelinye_slova}")
            nuzhnyy=input(text).lower().strip()
            if nuzhnyy in pravelinye_slova:

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
        if vse.tsena <= summa:
            print_one_fish(vse)
            correct_sumvol=1
    if correct_sumvol!=1:
        print("товары были не найдены")
        


def new_porol():
    porol=int(input("напиши новый пароль: "))
    return porol


def vvod_porol(porol):
    print("если ты продовец введи число 1 если ты покупатель введи число 2")
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
    vvod_porol(porol)
                
            

def market():
    input("нажми enter ")
    print("напиши цифру 1 чтобы найти по id")
    print("напиши цифру 2 чтобы вывести все продукты")
    print("напиши цифру 3 чтобы вывести по размеру")
    print("напиши цифру 4 чтобы вывести по названию")
    print("напиши цифру 5 чтобы вывести по приготовлению")
    print("напиши цифру 6 чтобы вывести по цене")
    print("напиши цифру 7 чтобы стать торговцем ")
    print("напиши цифру 8 чтобы сохранить для печати ")
    print("напиши цифру 9 чтобы отсортировать от большего к меньшему по весу  ")
    print("напиши цифру 10 чтобы отсортировать от большего к меньшему по весу ")
    print("напиши цифру 11 чтобы отсортировать от большего к меньшему по весу ")
    print("напиши цифру 12 отсортировать от большего к меньшему по весу ")
    print("напиши цифру 0 для выхода")
    while True:
        try:
            tsufra= int(input("введи число: "))
            if 0<=tsufra<=12:
                break
        except:
            print("вы ввели не число")
    return tsufra

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


def save_to_file_for_print(file_neim, prodykt:list[Fish]):
    with open(file_neim, "w", encoding="utf-8") as file:
            while True:
                try:
                    file.write("католог рыбного магазина - 'JapaneseWormFromChina 🐛'\n\n")
                    for fisshi in prodykt:

                        file.write(f"print('=='*20\n")
                        file.write(f"название продукта -{fisshi.mazvanie_prodykta}\n")
                        file.write(f"вид продукта - {fisshi.vid}\n")
                        file.write(f"приготовление - {fisshi.prigotovlenie}\n")
                        file.write(f"дата изготовления - {fisshi.data_isgotovleni}\n")
                        file.write(f"вес - {fisshi.ves}\n")
                        file.write(f"цена - {fisshi.tsena} рублей\n")
                        file.write(f"размер - {fisshi.razmer}\n")
                        file.write(f"Ид - {fisshi.id}\n\n")
                    break                    
                except:
                    print("что то сломалось")
                

def save_to_file_to_upload(prodykt:list[Fish]):
    with open("upload2.txt", "w", encoding="utf-8") as file:
            while True:
                try:
                    file.write(f"{len(prodykt)}\n")
                    for fisshi in prodykt:

                        
                        file.write(f"{fisshi.mazvanie_prodykta}\n")
                        file.write(f"{fisshi.vid}\n")
                        file.write(f"{fisshi.prigotovlenie}\n")
                        file.write(f"{fisshi.data_isgotovleni}\n")
                        file.write(f"{fisshi.ves}\n")
                        file.write(f"{fisshi.tsena}\n")
                        file.write(f"{fisshi.razmer}\n")
                        file.write(f"{fisshi.id}\n")
                    
                    break                    
                except:
                    print("что то сломалось")


def  upload_from_file(prodykt:list[Fish]):
    
        with open("upload2.txt", "r", encoding="utf-8") as file:
            count_produkt = int(file.readline().strip())
            for _ in range(count_produkt):
                prodykt.append(Fish(mazvanie_prodykta=file.readline().strip(), vid=file.readline().strip(), prigotovlenie=file.readline().strip(), data_isgotovleni=file.readline().strip(), ves=float(file.readline().strip()), tsena=int(file.readline().strip()), razmer=file.readline().strip(), id=id_fish()) )
                id_trash=file.readline().strip()
            print("файл загружен")   
    


def sort_by_weight_desc(prodykt:list[Fish]):
    sort=0
    for i in range(len(prodykt)):
        for j in range(len(prodykt)-1 - i):
            if prodykt[j].ves > prodykt[j+1].ves:
                sort=prodykt[j].ves
                prodykt[j].ves = prodykt[j+1].ves
                prodykt[j+1].ves = sort
    print("сортировка закончена")


def sort_by_tsene(prodykt:list[Fish]):
    sort=0
    for i in range(len(prodykt)):
        for j in range(len(prodykt)-1 - i):
            if prodykt[j].tsena > prodykt[j+1].tsena :
                sort=prodykt[j].tsena 
                prodykt[j].tsena  = prodykt[j+1].tsena 
                prodykt[j+1].tsena  = sort
    print("сортировка закончена")


def print_by_sort_vid(prodykt:list[Fish]):
    while True:
        try:
            nuznui_vid=input("нипиши сюда нажный вид для поиска: ").lower().strip()
            if len(nuznui_vid)>=3 and len(nuznui_vid)<=43:

                break
            print("вы ввели слтшком маленькое или слишком большое слово ")
        except:
            print("вы ввели что-то не то")
    for fisshi in prodykt:
        if fisshi.vid == nuznui_vid:
            print_one_fish(fisshi)

# пороль 3455
