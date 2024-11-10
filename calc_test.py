import numpy as np
import pytest
from calc import dodaj, odejmij, mnoz, dziel, dodaj_wektory, odejmij_wektory, mnoz_wektory, dziel_wektory, dodaj_macierze, odejmij_macierze, mnoz_macierze, dziel_macierze
 
# Testy dla skalarów
def test_dodaj_dodatnie_calkowite():
    assert dodaj(2, 3) == 5
 
def test_dodaj_ujemne_calkowite():
    assert dodaj(-2, -3) == -5
 
def test_dodaj_zero():
    assert dodaj(0, 5) == 5
 
def test_odejmij_dodatnie_calkowite():
    assert odejmij(5, 2) == 3
 
def test_odejmij_ujemne_calkowite():
    assert odejmij(-5, -2) == -3
 
def test_mnoz_dodatnie_calkowite():
    assert mnoz(2, 3) == 6
 
def test_mnoz_ujemne_calkowite():
    assert mnoz(-2, -3) == 6
 
def test_dziel_dodatnie_calkowite():
    assert dziel(6, 2) == 3
 
def test_dziel_przez_zero():
    assert dziel(5, 0) == "Dzielenie przez zero!"
 
def test_dziel_ujemne_calkowite():
    assert dziel(-6, -2) == 3
 
# Testy dla wektorów
def test_dodaj_wektory_dodatnie():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    wynik = dodaj_wektory(a, b)
    oczekiwany = np.array([5, 7, 9])
    assert np.array_equal(wynik, oczekiwany)
 
def test_dodaj_wektory_ujemne():
    a = np.array([-1, -2, -3])
    b = np.array([-4, -5, -6])
    wynik = dodaj_wektory(a, b)
    oczekiwany = np.array([-5, -7, -9])
    assert np.array_equal(wynik, oczekiwany)
 
def test_dodaj_wektory_z_zerem():
    a = np.array([1, 2, 3])
    b = np.array([0, 0, 0])
    wynik = dodaj_wektory(a, b)
    oczekiwany = np.array([1, 2, 3])
    assert np.array_equal(wynik, oczekiwany)
 
def test_odejmij_wektory_dodatnie():
    a = np.array([5, 7, 9])
    b = np.array([1, 2, 3])
    wynik = odejmij_wektory(a, b)
    oczekiwany = np.array([4, 5, 6])
    assert np.array_equal(wynik, oczekiwany)
 
def test_odejmij_wektory_ujemne():
    a = np.array([-5, -7, -9])
    b = np.array([-1, -2, -3])
    wynik = odejmij_wektory(a, b)
    oczekiwany = np.array([-4, -5, -6])
    assert np.array_equal(wynik, oczekiwany)
 
def test_mnoz_wektory_dodatnie():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    wynik = mnoz_wektory(a, b)
    oczekiwany = np.array([4, 10, 18])
    assert np.array_equal(wynik, oczekiwany)
 
def test_mnoz_wektory_ujemne():
    a = np.array([-1, -2, -3])
    b = np.array([-4, -5, -6])
    wynik = mnoz_wektory(a, b)
    oczekiwany = np.array([4, 10, 18])
    assert np.array_equal(wynik, oczekiwany)
 
def test_dziel_wektory_dodatnie():
    a = np.array([6, 8, 10])
    b = np.array([2, 2, 2])
    wynik = dziel_wektory(a, b)
    oczekiwany = np.array([3, 4, 5])
    assert np.array_equal(wynik, oczekiwany)
 
def test_dziel_wektory_przez_zero():
    a = np.array([6, 8, 10])
    b = np.array([2, 0, 2])
    wynik = dziel_wektory(a, b)
    oczekiwany = np.array([3, np.inf, 5])
    assert np.allclose(wynik, oczekiwany, equal_nan=True)
 
def test_dziel_wektory_ujemne():
    a = np.array([-6, -8, -10])
    b = np.array([-2, -2, -2])
    wynik = dziel_wektory(a, b)
    oczekiwany = np.array([3, 4, 5])
    assert np.array_equal(wynik, oczekiwany)
 
# Testy dla macierzy
def test_dodaj_macierze_dodatnie():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    wynik = dodaj_macierze(a, b)
    oczekiwany = np.array([[6, 8], [10, 12]])
    assert np.array_equal(wynik, oczekiwany)
 
def test_dodaj_macierze_ujemne():
    a = np.array([[-1, -2], [-3, -4]])
    b = np.array([[-5, -6], [-7, -8]])
    wynik = dodaj_macierze(a, b)
    oczekiwany = np.array([[-6, -8], [-10, -12]])
    assert np.array_equal(wynik, oczekiwany)
 
def test_dodaj_macierze_z_zerem():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[0, 0], [0, 0]])
    wynik = dodaj_macierze(a, b)
    oczekiwany = np.array([[1, 2], [3, 4]])
    assert np.array_equal(wynik, oczekiwany)
 
def test_odejmij_macierze_dodatnie():
    a = np.array([[5, 7], [9, 11]])
    b = np.array([[1, 2], [3, 4]])
    wynik = odejmij_macierze(a, b)
    oczekiwany = np.array([[4, 5], [6, 7]])
    assert np.array_equal(wynik, oczekiwany)
 
def test_odejmij_macierze_ujemne():
    a = np.array([[-5, -7], [-9, -11]])
    b = np.array([[-1, -2], [-3, -4]])
    wynik = odejmij_macierze(a, b)
    oczekiwany = np.array([[-4, -5], [-6, -7]])
    assert np.array_equal(wynik, oczekiwany)
 
def test_mnoz_macierze_dodatnie():
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    wynik = mnoz_macierze(a, b)
    oczekiwany = np.array([[19, 22], [43, 50]])
    assert np.array_equal(wynik, oczekiwany)
 
def test_mnoz_macierze_ujemne():
    a = np.array([[-1, -2], [-3, -4]])
    b = np.array([[-5, -6], [-7, -8]])
    wynik = mnoz_macierze(a, b)
    oczekiwany = np.array([[19, 22], [43, 50]])
    assert np.array_equal(wynik, oczekiwany)
 
def test_dziel_macierze_dodatnie():
    a = np.array([[6, 8], [10, 12]])
    b = np.array([[2, 2], [2, 2]])
    wynik = dziel_macierze(a, b)
    oczekiwany = np.array([[3, 4], [5, 6]])
    assert np.array_equal(wynik, oczekiwany)
 
def test_dziel_macierze_przez_zero():
    a = np.array([[6, 8], [10, 12]])
    b = np.array([[2, 0], [0, 2]])
    wynik = dziel_macierze(a, b)
    oczekiwany = np.array([[3, np.inf], [np.inf, 6]])
    assert np.allclose(wynik, oczekiwany, equal_nan=True)
 
def test_dziel_macierze_ujemne():
    a = np.array([[-6, -8], [-10, -12]])
    b = np.array([[-2, -2], [-2, -2]])
    wynik = dziel_macierze(a, b)
    oczekiwany = np.array([[3, 4], [5, 6]])
    assert np.array_equal(wynik, oczekiwany)