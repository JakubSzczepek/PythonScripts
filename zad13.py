from pprint import pformat, pprint
import json

class Kontakt:
    def __init__(self, imie, nazwisko, adresy=[]):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adresy

    def pokaz_adres(self):
        lista = []
        lista.append(self.imie)
        lista.append(self.nazwisko)
        for index, item in enumerate(self.adres):
            lista.extend(item.pokaz_adres(index))
        return lista


class Adres:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def pokaz_adres(self,index):
        lista = []
        for key in self.__dict__:
            lista.extend([key + '_' + str(index), self.__dict__[key]])
            # lista.append(pformat(f'{key}_{index} {self.__dict__[key]}'))
        return lista

ksiazka_adresowa = [
    Kontakt(imie='Max', nazwisko='Peck', adresy=[
        Adres(ulica='2101 E NASA Pkwy', miasto='Houston', stan='Texas', kod='77058', panstwo='USA'),
        Adres(ulica=None, miasto='Kennedy Space Center', kod='32899', panstwo='USA'),
        Adres(ulica='4800 Oak Grove Dr', miasto='Pasadena', kod='91109', panstwo='USA'),
        Adres(ulica='2825 E Ave P', miasto='Palmdale', stan='California', kod='93550', panstwo='USA', data_urodzenia=None),
    ]),
    Kontakt(imie='José', nazwisko='Jiménez'),
    Kontakt(imie='Иван', nazwisko='Иванович', adresy=[]),
]

for item in ksiazka_adresowa:
    pprint(item.pokaz_adres())
