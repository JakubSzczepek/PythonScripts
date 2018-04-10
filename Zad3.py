import statistics

dzienniczek = []
def dodajDoDzienniczka(ocena):
    possible = [2, 3, 3.5, 4, 4.5, 5]
    srednia = 0
    ocena = float(ocena)
    if ocena in possible:
        dzienniczek.append(ocena)
        srednia = statistics.mean(dzienniczek)
    else:
        print('Podałeś złą ocene')
    return print(srednia)

stop = '0'
while stop != '1':
    ocena = input('Poadaj ocene: ')
    dodajDoDzienniczka(ocena)
    stop = input('Czy chcesz dodać koljną ocene 0 Tak 1 Nie: ')