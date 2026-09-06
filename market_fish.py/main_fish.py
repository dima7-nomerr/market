from fishs import *
from fish_functions import *
from menu_main_fish import *
prodykt= []
buy_fish = []
porol=3455
drinks= []
drinks_buy= []
to_log_in_to_the_admin_panel=input_porol(porol)
user_state=-1
is_running= True
generation_drink(drinks)


# сделать так чтобы при вводе нельзя было написать менше размер чем большой размер

while is_running==True:
    if to_log_in_to_the_admin_panel == "no":
        user_state=user_menu()



        

    if user_state == 1:
        ID = check_by_int("Введи id: ")
        fisshi=search_by_id(ID, prodykt)
        print_by_id_fish(fisshi)

        print("напиши 1 если хочешь купить")
        print("напиши 0 если хочешь выйти")
        state=user_state_by_id_sort()
        input("нажмите enter для продолжения ")

        if state == 1:
            buy_fish.append(fisshi)
            pop_id_fish(fisshi, prodykt)
            print("вы купили продукт")
            print()

        elif state == 0:
            pass
    elif user_state == 2:
        print_products(prodykt)

    elif user_state == 3:
        running= True
        while running==True:
            state_sort=sort_prodykt()
            if state_sort == 1:
                pravelinye_slova="большой | средний | маленький"
                text=("напиши сюда нужный размер ")
                nuzhnyy_razmer=check_by_str(text, pravelinye_slova)
                print_by_size(nuzhnyy_razmer, prodykt)
                input("нажмите enter для продолжения ")
            elif state_sort == 2:
                pravelinye_slova='рыба | икра | водоросль'
                text=("напиши сюда нужное название продукта ")
                mazvanie_prodykta=check_by_str(text, pravelinye_slova)
                print_by_product_name(mazvanie_prodykta, prodykt)
                input("нажмите enter для продолжения ")
            
            elif state_sort == 3:
                pravelinye_slova="парной | свежий | замороженый"
                text=("введите способ приготовления ")
                nuzhnyy_prigotovlenie=check_by_str(text, pravelinye_slova)
                print_by_preparetion(nuzhnyy_prigotovlenie, prodykt)
                input("нажмите enter для продолжения ")
            elif state_sort == 4:
                summa(prodykt)
                input("нажмите enter для продолжения ")
            elif state_sort == 5:
                sort_by_weight_desc(prodykt)
            elif state_sort == 6:
                sort_by_price(prodykt)
            elif state_sort == 7:
                print_by_sort_view(prodykt)
                input("нижми enter для продолжения ")


            running==False
        
        


    elif user_state == 4:
        to_log_in_to_the_admin_panel=input_porol(porol)


    elif user_state == 5:
            file_neim=file_neim_vvod()
            save_to_file_for_print(file_neim, prodykt)
            print("файл записан")

    elif user_state == 6:
        correct_input = True
        while correct_input == True:
            user_drink_numder=drink_menu_user()

            if 1 == user_drink_numder:
                user_sort_id_numder=user_drink_id_menu()

                if user_drink_id_menu == 1:

                    buy_drink(drinks_buy, id_one_drink, drinks)


            elif 2 == user_drink_numder:
                admine_sort_numder=sort_admine_or_user_menu()

                if 1 == admine_sort_numder:
                         
                    necessary_drink_name=input("напиши название напитка: ").lower().strip()
                    sort_by_drink_name(drinks, necessary_drink_name)


                elif 2 == admine_sort_numder:

                    necessary_volume_max=check_by_int("напиши до какого объёма будут показыватся напики")
                    necessary_volume_min=check_by_int("напиши от какого объёма будут показыватся напики")
                        
                    sort_by_volume(drinks, necessary_volume_max, necessary_volume_min)

                elif 3 == admine_sort_numder:
                    necessary_price_max=check_by_int("напиши до какой цены будут показыватся напики")
                    necessary_price_min=check_by_int("напиши от какой цены будут показыватся напики")
                        
                    sort_by_price(drinks, necessary_price_max, necessary_price_min)

                elif 4 == admine_sort_numder:
                    necessary_quantity_max=check_by_int("напиши до какого количества напитков будут показыватся напики")
                    necessary_quantity_min=check_by_int("напиши от какого количества напитков будут показыватся напики")


            elif  3 == user_drink_numder:
                print_drinks(drinks)



            elif 0 == user_drink_numder:
                correct_input = False


    elif user_state == 0:
        print("это всё что вы купили")
        print_products(buy_fish)
        print_products(drinks_buy)
        break


   
# админ панель

    while to_log_in_to_the_admin_panel=="cypher":
        admin_state= menu_admin()

        if admin_state == 1:
            new_fish=input_fish_dataclass()
            new_fish.id=id_fish()
            input_prodykt_by_list(prodykt, new_fish)
            
            

        elif admin_state == 2:
            ID = check_by_int("Введи id: ")
            fisshi=search_by_id(ID, prodykt)
            print_by_id_fish(fisshi)
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
                updeit_by_id(fisshi)
                input_prodykt_by_list(prodykt, new_fish)
                print()
            elif admin_state_id_sort ==3:
                
                buy_fish.append(fisshi)
                pop_id_fish(fisshi, prodykt)
                print("вы купили продукт")
                print()
            elif admin_state_id_sort == 0:
                pass
        elif admin_state == 3:
            print_products(prodykt)



        elif admin_state == 4:
            running= True
            while running==True:
                state_sort=sort_prodykt()


                if state_sort == 1:
                    pravelinye_slova="большой | средний | маленький"
                    text=("напиши сюда нужный размер ")
                    nuzhnyy_razmer=check_by_str(text, pravelinye_slova)
                    print_by_size(nuzhnyy_razmer, prodykt)
                    input("нажмите enter для продолжения ")

                elif state_sort == 2:

                    pravelinye_slova='рыба | икра | водоросль'
                    text=("напиши сюда нужное название продукта ")
                    mazvanie_prodykta=check_by_str(text, pravelinye_slova)
                    print_by_product_name(mazvanie_prodykta, prodykt)
                    input("нажмите enter для продолжения ")

                elif state_sort == 3:

                    pravelinye_slova="парной | свежий | замороженый"
                    text=("введите способ приготовления ")
                    nuzhnyy_prigotovlenie=check_by_str(text, pravelinye_slova)
                    print_by_preparetion(nuzhnyy_prigotovlenie, prodykt)
                    input("нажмите enter для продолжения ")

                elif state_sort == 4:
                    summa(prodykt)
                    input("нажмите enter для продолжения ")

                elif state_sort == 5:
                    sort_by_weight_desc(prodykt)

                elif state_sort == 6:
                    sort_by_price(prodykt)

                elif state_sort == 7:
                    print_by_sort_view(prodykt)
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

# начало ветки с напитками


        elif admin_state == 10:
            correct_input=True
            while correct_input == True:
                admine_drink_numder=drink_menu()

                if 1 ==admine_drink_numder:
                    new_drink=input_drink_by_dataclass_Drink()
                    new_drink.id = id_drink()
                    input_drink_by_list(drinks, new_drink)

                elif 2 == admine_drink_numder:
                    ID =check_by_int("напиши нужный id ")
                    id_one_drink=search_by_id_drink(drinks, ID)
                    print_one_drink(id_one_drink)
                    admine_sort_id_numder=drink_id_menu()

                    if 1==admine_sort_id_numder:
                        del_drink_by_id(drinks, id_one_drink)

                    elif 2==admine_sort_id_numder:
                        replenish_quantity(drinks, id_one_drink)

                    elif 3 ==admine_sort_id_numder:
                        to_change_drink(drinks, id_one_drink)

                    elif 4 == admine_sort_id_numder:
                        buy_drink(drinks_buy, id_one_drink, drinks)
        
                elif 3 == admine_drink_numder:
                    admine_sort_numder=sort_admine_or_user_menu()

                    if 1 == admine_sort_numder:
                         
                         necessary_drink_name=input("напиши название напитка: ").lower().strip()
                         sort_by_drink_name(drinks, necessary_drink_name)


                    elif 2 == admine_sort_numder:

                        necessary_volume_max=check_by_int("напиши до какого объёма будут показыватся напики")
                        necessary_volume_min=check_by_int("напиши от какого объёма будут показыватся напики")
                        
                        sort_by_volume(drinks, necessary_volume_max, necessary_volume_min)

                    elif 3 == admine_sort_numder:
                        necessary_price_max=check_by_int("напиши до какой цены будут показыватся напики")
                        necessary_price_min=check_by_int("напиши от какой цены будут показыватся напики")
                        
                        sort_by_price(drinks, necessary_price_max, necessary_price_min)

                    elif 4 == admine_sort_numder:
                        necessary_quantity_max=check_by_int("напиши до какого количества напитков будут показыватся напики")
                        necessary_quantity_min=check_by_int("напиши от какого количества напитков будут показыватся напики")
                                                

                        sort_by_quantity(drinks, necessary_quantity_max, necessary_quantity_min)

                    

                elif 4 == admine_drink_numder:
                    print_drinks(drinks)

                elif 0 == admine_drink_numder:
                    correct_input = False
            
        elif admin_state == 0:
            print("это всё что вы купили")
            print_products(buy_fish)
            print_products(drinks_buy)
            is_running= False



# пороль 3455
