import unittest
from main import *

class MyTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello_world(), "hello world")

    def test_list_len(self):
        self.assertEqual(list_len(list(range(10))), 10)

    def test_dodawanie_lub_mnozenie(self):
        self.assertEqual(dodawanie_lub_mnozenie(2,6), 8)
        self.assertEqual(dodawanie_lub_mnozenie(3,6), 0.5)
        self.assertEqual(dodawanie_lub_mnozenie(5,3), 15)

    def test_dodawanie(self):
        self.assertEqual(dodawanie(1,1,1), 3)

    def test_wpisz_imie(self):
        self.assertEqual(wpisz_imie(self), 'dzień dobry Tomasz')

    def test_pole_kola(self):
        self.assertEqual(pole_kola(3), 28.26)