class Kontakt:

    def __init__(self, imie = None, nazwisko = None, adresy = [] ):
        self.imie  = imie
        self.nazwisko = nazwisko
        self.adres = adresy

    def pokaz_kontakt(self):
        print(self.imie, self.nazwisko)
        for item in self.adres:
            item.pokaz_adres()

    # def __str__(self):
    #     return f'{self.imie}{self.nazwisko}: {self.adres}'
    #
    # def __repr__(self):
    #     return self.__str__()

    def miejsce_zamieszkania(self):
        for item in self.adres:
            item.pokaz_adres()

    def pokaz_osobe(self):
        print(self.imie, self.nazwisko)


class Adres:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    def pokaz_adres(self):
        for key in self.__dict__:
            print("     {} {}".format(key, self.__dict__[key]))
        #     # print('Adres: ' , list(self.__dict__.items()))
    #
    # def __str__(self):
    #     for key in self.__dict__:
    #         print("     {} {}".format(key, self.__dict__[key]))
    #
    # def __repr__(self):
    #     self.__str__()




ksiazka_adresowa = [
     Kontakt(imie='Max', nazwisko='Peck', adresy=[
        Adres(ulica='2101 E NASA Pkwy', miasto='Houston', stan='Texas', kod='77058', panstwo='USA'),
        Adres(ulica=None, miasto='Kennedy Space Center', kod='32899', panstwo='USA'),
        Adres(ulica='4800 Oak Grove Dr', miasto='Pasadena', kod='91109', panstwo='USA'),
        Adres(ulica='2825 E Ave P', miasto='Palmdale', stan='California', kod='93550', panstwo='USA'),
    ]),
    Kontakt(imie='José', nazwisko='Jiménez'),
    Kontakt(imie='Иван', nazwisko='Иванович', adresy=[]),
]

# print(ksiazka_adresowa)

ksiazka_adresowa[0].pokaz_kontakt()
ksiazka_adresowa[1].pokaz_kontakt()
ksiazka_adresowa[2].pokaz_kontakt()
#
# ksiazka_adresowa[0].miejsce_zamieszkania()
# ksiazka_adresowa[1].miejsce_zamieszkania()
# ksiazka_adresowa[2].miejsce_zamieszkania()
# #
# ksiazka_adresowa[0].pokaz_osobe()
# ksiazka_adresowa[1].pokaz_osobe()
# ksiazka_adresowa[2].pokaz_osobe()