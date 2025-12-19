import random
import string

def lae_andmed():
    kasutajad = []
    paroolid = []
    return kasutajad, paroolid


def registreeri(kasutajad, paroolid):
    nimi = input("Sisesta kasutajanimi: ")
    if nimi in kasutajad:
        print("Selline nimi on juba olemas!")
        return
    print("A – automaatne parool")
    print("B – loon ise")
    valik = input("Valik (A/B): ").upper()
    if valik == "A":
        parool = ""
        kõik = ".,:;!_*-+()/#¤%&0123456789" + string.ascii_letters
        for i in range(12):
            parool += random.choice(kõik)
        print("Sinu parool:", parool)
    elif valik == "B":
        while True:
            parool = input("Sisesta parool: ")
            num = any(c.isdigit() for c in parool)
            lower = any(c.islower() for c in parool)
            upper = any(c.isupper() for c in parool)
            special = any(c in ".,:;!_*-+()/#¤%&" for c in parool)
            if num and lower and upper and special:
                break
            print("Parool ei vasta nõuetele!")
    else:
        print("Vale valik!")
        return

    kasutajad.append(nimi)
    paroolid.append(parool)
    print("Registreerimine õnnestus!")


def logi_sisse(kasutajad, paroolid):
    nimi = input("Sisesta kasutajanimi: ")
    parool = input("Sisesta parool: ")

    if nimi in kasutajad:
        idx = kasutajad.index(nimi)
        if paroolid[idx] == parool:
            print("Sisselogimine õnnestus!")
        else:
            print("Vale parool!")
    else:
        print("Sellist kasutajat pole!")


def muuda_andmeid(kasutajad, paroolid):
    vana = input("Sisesta vana kasutajanimi: ")
    if vana not in kasutajad:
        print("Kasutajat ei leitud!")
        return

    idx = kasutajad.index(vana)
    print("1 – Muuda nime")
    print("2 – Muuda parooli")
    v = input("Valik: ")

    if v == "1":
        uus = input("Sisesta uus nimi: ")
        if uus not in kasutajad:
            kasutajad[idx] = uus
            print("Nimi muudetud!")
        else:
            print("Nimi on juba kasutusel!")

    elif v == "2":
        while True:
            uus = input("Sisesta uus parool: ")
            num = any(c.isdigit() for c in uus)
            lower = any(c.islower() for c in uus)
            upper = any(c.isupper() for c in uus)
            special = any(c in ".,:;!_*-+()/#¤%&" for c in uus)
            if num and lower and upper and special:
                paroolid[idx] = uus
                print("Parool muudetud!")
                break
            print("Parool ei vasta nõuetele!")


def taasta_parool(kasutajad, paroolid):
    nimi = input("Sisesta oma kasutajanimi: ")
    if nimi not in kasutajad:
        print("Kasutajat ei leitud!")
        return

    idx = kasutajad.index(nimi)
    parool = ""
    kõik = ".,:;!_*-+()/#¤%&0123456789" + string.ascii_letters

    for i in range(12):
        parool += random.choice(kõik)

    paroolid[idx] = parool
    print("Sinu uus parool:", parool)