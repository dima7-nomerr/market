from Fishs import Fish
from fish_functions import *
prodykt= []
kypul = []
porol=3455

to_log_in_to_the_admin_panel=vvod_porol(porol)
user_state=-1
is_running= True
while is_running==True:
    if to_log_in_to_the_admin_panel == "no":
        user_state=market()



        

    if user_state == 1:
        ID = proverka_na_int("Введи id: ")
        fisshi=id_poisk(ID, prodykt)
        print_id_fish(fisshi)

        print("напиши 1 если хочешь купить")
        print("напиши 0 если хочешь выйти")
        state=user_state_by_id_sort()
        input("нажмите enter для продолжения ")

        if state == 1:
            kypul.append(fisshi)
            pop_id_fish(fisshi, prodykt)
            print("вы купили продукт")
            print()

        elif state == 0:
            pass
    elif user_state == 2:
        print_prodyktov(prodykt)

    elif user_state == 3:
        pravelinye_slova="большой | средний | маленький"
        text=("напиши сюда нужный размер ")
        nuzhnyy_razmer=proverka_na_str(text, pravelinye_slova)
        print_po_razmery(nuzhnyy_razmer, prodykt)
        input("нажмите enter для продолжения ")

    elif user_state == 4:
        pravelinye_slova='рыба | икра | водоросль'
        text=("напиши сюда нужное название продукта ")
        mazvanie_prodykta=proverka_na_str(text, pravelinye_slova)
        print_po_mazvanie_prodykta(mazvanie_prodykta, prodykt)
        input("нажмите enter для продолжения ")

    elif user_state == 5:
        pravelinye_slova="парной | свежий | замороженый"
        text=("введите способ приготовления ")
        nuzhnyy_prigotovlenie=proverka_na_str(text, pravelinye_slova)
        print_po_prigotovlenie(nuzhnyy_prigotovlenie, prodykt)
        input("нажмите enter для продолжения ")

    elif user_state == 6:

        summa(prodykt)
        input("нажмите enter для продолжения  ")

    elif user_state == 7:
        to_log_in_to_the_admin_panel=vvod_porol(porol)
        if to_log_in_to_the_admin_panel == "klys":
            pass

    elif user_state == 8:
            file_neim=file_neim_vvod()
            save_to_file_for_print(file_neim, prodykt)
            print("файл записан")

    elif user_state == 9:
        sort_by_weight_desc(prodykt)
    elif user_state == 10:
        sort_by_tsene(prodykt)

    elif user_state == 11:
        sort_by_weight_desc(prodykt)

    elif user_state == 12:
        sort_by_tsene(prodykt)

    elif user_state == 0:
        print("это всё что вы купили")
        print_prodyktov(kypul)
        break


   
# админ панель

    while to_log_in_to_the_admin_panel=="cypher":
        admin_state= menu()

        if admin_state == 1:
            new_fish=input_fish_market()
            new_fish.id=id_fish()
            input_prodykt_B_list(prodykt, new_fish)
            
            

        elif admin_state == 2:
            ID = proverka_na_int("Введи id: ")
            fisshi=id_poisk(ID, prodykt)
            print_id_fish(fisshi)
            print("напиши 1 если хочешь удалить")
            print("напиши 2 если хочешь изменить")
            print("напиши 3 если хочешь купить")
            print("напиши 0 если хочешь выйти")
            admin_state_id_sort=admin_state__by_id_sort()
            input("нажмите enter для продолжения ")

            if admin_state_id_sort == 1:
                pop_id_fish(fisshi, prodykt)
                print()
            elif admin_state_id_sort == 2:
                pop_id_fish(fisshi, prodykt)
                updeit_po_id(fisshi)
                input_prodykt_B_list(prodykt, new_fish)
                print()
            elif admin_state_id_sort ==3:
                
                kypul.append(fisshi)
                pop_id_fish(fisshi, prodykt)
                print("вы купили продукт")
                print()
            elif admin_state_id_sort == 0:
                pass
        elif admin_state == 3:
            print_prodyktov(prodykt)



        elif admin_state == 4:
            running= True
            while running==True:
                state_sort=sort_prodykt()


                if state_sort == 1:
                    pravelinye_slova="большой | средний | маленький"
                    text=("напиши сюда нужный размер ")
                    nuzhnyy_razmer=proverka_na_str(text, pravelinye_slova)
                    print_po_razmery(nuzhnyy_razmer, prodykt)
                    input("нажмите enter для продолжения ")
                elif state_sort == 2:
                    pravelinye_slova='рыба | икра | водоросль'
                    text=("напиши сюда нужное название продукта ")
                    mazvanie_prodykta=proverka_na_str(text, pravelinye_slova)
                    print_po_mazvanie_prodykta(mazvanie_prodykta, prodykt)
                    input("нажмите enter для продолжения ")

                elif state_sort == 3:
                    pravelinye_slova="парной | свежий | замороженый"
                    text=("введите способ приготовления ")
                    nuzhnyy_prigotovlenie=proverka_na_str(text, pravelinye_slova)
                    print_po_prigotovlenie(nuzhnyy_prigotovlenie, prodykt)
                    input("нажмите enter для продолжения ")
                elif state_sort == 4:
                    summa(prodykt)
                    input("нажмите enter для продолжения ")
                elif state_sort == 5:
                    sort_by_weight_desc(prodykt)
                elif state_sort == 6:
                    sort_by_tsene(prodykt)
                elif state_sort == 7:
                    print_by_sort_vid(prodykt)
                    input("нижми enter для продолжения ")



                
        elif admin_state == 5:
            porol=new_porol()

        elif admin_state == 6:
            to_log_in_to_the_admin_panel="no"


        elif admin_state == 7:
            file_neim=file_neim_vvod()
            save_to_file_for_print(file_neim, prodykt)
            print("файл записан")


        elif admin_state == 8:
            
            save_to_file_to_upload(prodykt)
            print("файл записан")  

        elif admin_state == 9:
            upload_from_file(prodykt)

            
        elif admin_state == 0:
            print("это всё что вы купили")
            print_prodyktov(kypul)
            is_running= False



# пороль 3455




