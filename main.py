"""
Kérj be 2 számot a felhasználótól.
írj eljárást 
    szamok néven, (ciklusok.py) 
    melynek a parametere a felhasználó által megadott két szám
    és 
    az eljárás kiírja a számokat ezen két paraméter között
"""
import ciklusok

szam1: int =(input("Adj meg egy számot: "))
szam2: int =(input("Adj meg még egy szamot: "))

ciklusok.szamok(szam1, szam2)
