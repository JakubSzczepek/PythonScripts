from pprint import pformat, pprint
import json

class Kontakt:
    def __init__(self, imie, nazwisko, adresy=()):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adresy = adresy

    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.adresy}'

    def __repr__(self):
        return self.__str__()

    def pokaz_adres(self):
        lista = []
        lista.append(self.imie)
        lista.append(self.nazwisko)
        for index, item in enumerate(self.adres):
            lista.extend(item.pokaz_adres(index))
        return lista


class Adres:
    def __init__(self, **kwargs):
        self.ulica = kwargs.get('ulica', None)
        self.miasto = kwargs.get('miasto', None)

#        for k, v in kwargs.items():
#           setattr(self, k, v)

    def __str__(self):
        return f'{self.ulica} {self.miasto}'

    def __repr__(self):
        return self.__str__()

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

class JSONObjectEncoder(json.JSONEncoder):
    def default(self, obiekt):
        try:
            return super().default(obiekt)
        except TypeError:
            return obiekt.__dict__


class JSONObjectDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_object)

    def decode_object(self, slownik):
        if slownik.get('miasto'):
            return Adres(**slownik)
        else:
            return Kontakt(**slownik)


with open('/PythonProject/zad14.json', 'w') as file:
    serialized = json.dumps(ksiazka_adresowa, cls=JSONObjectEncoder)
    file.write(serialized)


with open('/PythonProject/zad14.json', 'r') as file:
    unserialized = json.loads(file.read(), cls=JSONObjectDecoder)

    for line in unserialized:
        print(line)


