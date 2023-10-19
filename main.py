"""
Kérj be 2 számot a felhasználótól.
írj eljárást 
    szamok néven, (ciklusok.py) 
    melynek a parametere a felhasználó által megadott két szám
    és 
    az eljárás kiírja a számokat ezen két paraméter között
"""
import ciklusok

a: int =int(input("a: "))
b: int =int(input("b: "))
""" A felhasználó csak olyan b-t tudjon megadni, ami >a"""
while (a>=b):
    print("B-nek nagyobbnak kell lennie A-nal")
    b:int = int(input(f"adj{a}-nál nagyobban!"))


ciklusok.szamok(a, b)
