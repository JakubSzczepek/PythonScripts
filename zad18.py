class Kontakt:
    def __init__(self, imie, nazwisko, adresy=[]):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adresy = adresy


    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.adresy):
            raise StopIteration
        adres = self.adresy[self.index]
        self.index += 1
        return adres

class Adres:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return str(self.__dict__)


ksiazka_adresowa = Kontakt(imie='Max', nazwisko='Peck', adresy=[
        Adres(ulica='2101 E NASA Pkwy', miasto='Houston', stan='Texas',
              kod='77058', panstwo='USA'),
        Adres(ulica=None, miasto='Kennedy Space Center', kod='32899',
              panstwo='USA'),
        Adres(ulica='4800 Oak Grove Dr', miasto='Pasadena', kod='91109',
              panstwo='USA'),
        Adres(ulica='2825 E Ave P', miasto='Palmdale', stan='California',
              kod='93550', panstwo='USA')])


for x in ksiazka_adresowa:
    print(x)