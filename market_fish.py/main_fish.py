from Fishs import Fish
from fish_functions import *
prodykt= []
kypul = []
porol=3455

l=pol(porol)
tsufra=-1
ttttt= True
while ttttt==True:
    if l == "no":
        tsufra=market()
    elif l == "klys":
        ttttt= -1


        

    if tsufra == 1:
        ID = proverka("Введи id: ")
        fisshi=id_poisk(ID, prodykt)
        print_id_fish(fisshi)

        print("напиши 1 если хочешь купить")
        print("напиши 0 если хочешь выйти")
        polizovate=stoto_tam_po_id2()
        input("нажмите enter для продолжения ")

        if polizovate == 1:
            kypul.append(fisshi)
            pop_id_fish(fisshi, prodykt)
            print("вы купили продукт")
            print()

        elif polizovateli == 0:
            pass
    elif tsufra == 2:
        print_prodyktov(prodykt)

    elif tsufra == 3:
        suda=("напиши сюда нужный размер ")
        nuzhnyy_razmer=proverka2(suda)
        print_po_razmery(nuzhnyy_razmer, prodykt)
        input("нажмите enter для продолжения ")

    elif tsufra == 4:
        suda=("напиши сюда нужное название продукта ")
        mazvanie_prodykta=proverka2(suda)
        print_po_mazvanie_prodykta(mazvanie_prodykta, prodykt)
        input("нажмите enter для продолжения ")

    elif tsufra == 5:
        suda=("введите способ приготовления  ")
        nuzhnyy_prigotovlenie=proverka2(suda)
        print_po_prigotovlenie(nuzhnyy_prigotovlenie, prodykt)
        input("нажмите enter для продолжения ")

    elif tsufra == 6:

        summa(prodykt)
        input("нажмите enter для продолжения  ")

    elif tsufra == 7:
        l=pol(porol)
        if l == "klys":
            pass

    elif tsufra == 0:
        print("это всё что вы купили")
        print(kypul)
        break

    while l=="klys":
        polizovatel_tsufra= menu()

        if polizovatel_tsufra == 1:
            new_fish=input_fish_market()
            new_fish.id=id_fish()
            input_prodykt_B_list(prodykt, new_fish)
            input("нажмите enter для продолжения ")
            

        elif polizovatel_tsufra == 2:
            ID = proverka("Введи id: ")
            fisshi=id_poisk(ID, prodykt)
            print_id_fish(fisshi)
            print("напиши 1 если хочешь удалить")
            print("напиши 2 если хочешь изменить")
            print("напиши 3 если хочешь купить")
            print("напиши 0 если хочешь выйти")
            polizovateli=stoto_tam_po_id()
            input("нажмите enter для продолжения ")

            if polizovateli == 1:
                pop_id_fish(fisshi, prodykt)
                print()
            elif polizovateli == 2:
                pop_id_fish(fisshi, prodykt)
                updeit_po_id(fisshi)
                input_prodykt_B_list(prodykt, new_fish)
                print()
            elif polizovateli ==3:
                
                kypul.append(fisshi)
                pop_id_fish(fisshi, prodykt)
                print("вы купили продукт")
                print()
            elif polizovateli == 0:
                pass
        elif polizovatel_tsufra == 3:
            print_prodyktov(prodykt)

        elif polizovatel_tsufra == 4:
            suda=("напиши сюда нужный размер ")
            nuzhnyy_razmer=proverka2(suda)
            print_po_razmery(nuzhnyy_razmer, prodykt)
            input("нажмите enter для продолжения ")

        elif polizovatel_tsufra == 5:
            suda=("напиши сюда нужное название продукта ")
            mazvanie_prodykta=proverka2(suda)
            print_po_mazvanie_prodykta(mazvanie_prodykta, prodykt)
            input("нажмите enter для продолжения ")

        elif polizovatel_tsufra == 6:
            suda=("введите способ приготовления ")
            nuzhnyy_prigotovlenie=proverka2(suda)
            print_po_prigotovlenie(nuzhnyy_prigotovlenie, prodykt)
            input("нажмите enter для продолжения ")

        elif polizovatel_tsufra == 7:

            summa(prodykt)
            input("нажмите enter для продолжения ")

        elif polizovatel_tsufra == 8:
            porol=poroliiii()


        elif polizovatel_tsufra == 9:
            l=pol(porol)
            if l == "no":
                pass



        elif polizovatel_tsufra == 0:
            print("это всё что вы купили")
            print(kypul)
            ttttt= False




