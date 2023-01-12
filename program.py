import json
import random
import sys
import os

zycia = ("__")
znaki = []
uzyte_znaki = []
valid = "abcdefghijklmnoprstuwxyz"

with open("hasla.json") as hasla_json:
    hasla = json.load(hasla_json)
    los = random.randint(1, len(hasla)-1)

haslo = hasla[los]["haslo"]

def informacje():
    print("")
    print("Kategoria:", hasla[los]["kategoria"])
    print("Pozostała ilość żyć:", zycia)
    print(znaki)
    print("")

def szukanie(haslo, litera):
    indexy = []
    
    for index, litery in enumerate(haslo):
        if litera == litery:
            indexy.append(index)
    return indexy

for _  in haslo:
    znaki.append("_")

os.system('clear')
informacje()
zycia = input("Wprowadż ilość żyć w danej grze: ")
zycia = int(zycia)
os.system('clear')

while True:
    informacje()
    litera = input("Wpisz literę: ")

    if litera in valid:
        os.system('clear')
        uzyte_znaki.append(litera)
        index = szukanie(haslo, litera)

        if len(index) == 0:
            zycia -= 1
            
            if zycia == 0:
                print("Koniec gry")
                sys.exit(0)
        else:
            for i in index:
                znaki[i] = litera

            if "".join(znaki) == haslo:
                informacje()
                print("")
                print("Udało Ci się")
                sys.exit(0)
    else:
        os.system('clear')
        print("Możesz podać tylko 1 małą literę.")