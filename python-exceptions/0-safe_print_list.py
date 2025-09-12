#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
        try:
            compteur = 0
            for i in range(0, x):
                print(f"{my_list[i]}", end="")
                compteur += 1
            print()
            return compteur
        except IndexError:
            print()
            return compteur
    
