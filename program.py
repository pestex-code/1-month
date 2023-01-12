import json

zycia = 5

with open("hasla.json") as hasla_json:
    hasla = json.load(hasla_json)


#print(hasla[i]["haslo"])
while True:
    litera = input("Wpisz literę: ")