import numpy as np
 
# Operacje na skalarach
def dodaj(a, b):
    return a + b
 
def odejmij(a, b):
    return a - b
 
def mnoz(a, b):
    return a * b
 
def dziel(a, b):
    if b != 0:
        return a / b
    else:
        return "Dzielenie przez zero!"
 
# Operacje na tensorach pierwszego stopnia (wektorach)
def dodaj_wektory(a, b):
    return np.add(a, b)
 
def odejmij_wektory(a, b):
    return np.subtract(a, b)
 
def mnoz_wektory(a, b):
    return np.multiply(a, b)
 
def dziel_wektory(a, b):
    return np.divide(a, b)
 
# Operacje na tensorach drugiego stopnia (macierzach)
def dodaj_macierze(a, b):
    return np.add(a, b)
 
def odejmij_macierze(a, b):
    return np.subtract(a, b)
 
def mnoz_macierze(a, b):
    return np.matmul(a, b)
 
def dziel_macierze(a, b):
    return np.divide(a, b)