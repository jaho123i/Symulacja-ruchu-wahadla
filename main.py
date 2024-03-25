import math
import matplotlib.pyplot as plt
import numpy

przyspieszenie_ziemskie = -9.81
dlugosc_wahadla = 1.0
odstepy_czasowe = 0.01
calkowity_czas = 5
k1a = math.pi / 4
k1w = 0.0
masa = 1.0

liczba_pomiarow = int(calkowity_czas / odstepy_czasowe) + 1

def D(kat,predkosc_katowa):
    return predkosc_katowa,przyspieszenie_katowe(kat)

def E(kat,predkosc_katowa,odstepy_czasowe):
    return kat*odstepy_czasowe,predkosc_katowa*odstepy_czasowe

def przyspieszenie_katowe(kat):
    return przyspieszenie_ziemskie / dlugosc_wahadla * math.sin(kat)

def euler(kat,predkosc_katowa):
    tabela_katow = [kat]
    tabela_czasow = [0]
    tabela_predkosci = [predkosc_katowa]
    k1a = kat
    k1w = predkosc_katowa
    czas = 0
    for i in range(liczba_pomiarow):
        k1a,k1w = D(kat,predkosc_katowa)
        kat += E(k1a,k1w,odstepy_czasowe)[0]
        predkosc_katowa += E(k1a,k1w,odstepy_czasowe)[1]
        tabela_katow.append(kat)
        czas += odstepy_czasowe
        tabela_czasow.append(czas)
        tabela_predkosci.append(predkosc_katowa)
    return tabela_czasow,tabela_katow,tabela_predkosci,"Euler"

def plt_ruch(tabela_katow, dlugosc_wahadla, nazwa):
    os_x = dlugosc_wahadla * numpy.sin(tabela_katow)
    os_y = dlugosc_wahadla * -numpy.cos(tabela_katow)

    plt.plot(os_x, os_y, label=f'Ruch: {nazwa}')
    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')
    plt.legend()
    plt.title(f'Ruch: {nazwa}')
    plt.show()

def plt_energia(tabela_czasow,tabela_katow,tabela_predkosci,dlugosc_wahadla,masa,nazwa):
    energia_kinetyczna = masa * 0.5 * (dlugosc_wahadla * numpy.array(tabela_predkosci)) ** 2
    energia_potencjalna = masa * -przyspieszenie_ziemskie * dlugosc_wahadla * (1 - numpy.cos(numpy.array(tabela_katow)))
    energia_calkowita = energia_kinetyczna + energia_potencjalna

    plt.plot(tabela_czasow,energia_kinetyczna,label=f'Energia kinetyczna')
    plt.plot(tabela_czasow,energia_potencjalna,label=f'Energia potencjalna')
    plt.plot(tabela_czasow,energia_calkowita,label=f'Energia calkowita')
    plt.legend()
    plt.title(f'Energia: {nazwa}')
    plt.xlabel('Czas (s)')
    plt.ylabel('Energia (J)')
    plt.show()

czasy_euler, katy_euler, predkosci_euler, nazwa_euler = euler(k1a, k1w)
plt_ruch(katy_euler,dlugosc_wahadla,nazwa_euler)
plt_energia(czasy_euler,katy_euler,predkosci_euler,dlugosc_wahadla,masa,nazwa_euler)
print(czasy_euler, "\n", katy_euler, "\n", predkosci_euler, "\n", nazwa_euler)