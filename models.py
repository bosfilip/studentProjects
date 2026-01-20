import pickle

class Pojazd:
    def __init__(self, marka, rok):
        self.marka = marka
        self.rok = rok
    def __str__(self):
        return f"[Pojazd] Marka: {self.marka}, Rok: {self.rok}"
    def __eq__(self, other):
        return self.marka == other.marka and self.rok == other.rok

class Ksiazka:
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor
    def __str__(self):
        return f"[Ksiazka] Tytul: {self.tytul}, Autor: {self.autor}"
    def __eq__(self, other):
        return self.tytul == other.tytul and self.autor == other.autor

class Kot:
    def __init__(self, imie, rasa):
        self.imie = imie
        self.rasa = rasa
    def __str__(self):
        return f"[Kot] Imie: {self.imie}, Rasa: {self.rasa}"
    def __eq__(self, other):
        return self.imie == other.imie and self.rasa == other.rasa