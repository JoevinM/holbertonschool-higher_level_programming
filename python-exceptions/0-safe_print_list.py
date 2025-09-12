#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    compteur = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            compteur += 1
        except IndexError:
            continue
    print()
    return compteur
