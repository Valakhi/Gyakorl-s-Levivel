"""
1. Feladat
Thonny fejlesztői környezetben készíts egy rövid programot, amely
kommentként tartalmazza a program funkciójának leírását,
konstansként tárolja PI értékét,
egy másik változóban tárolja egy kör sugarának nagyságát (cm-ben megadva),
kiszámolja és a képernyőre kiírja a kör kerületét és területét!
[Megjegyzés] A szorzás jele: *

2. Feladat
Készíts egy rövid programot, amely egy változóban eltárol egy szót. Próbáld meg ennek a változónak a tartalmát int értékké átalakítani. Mit tapasztalsz? Milyen üzenet jelenik meg a képernyőn?


3. Feladat
Készíts egy rövid programot, amelyben egy olyan változó értékét szeretnéd kiíratni, ami előzőleg nem is szerepel a kódodban. Hogyan jelöli a fejlesztői környezet a hibát? Futtasd! Milyen hibaüzenetet kapsz?
"""
"""
1. Feladat
Thonny fejlesztői környezetben készíts egy rövid programot, amely
kommentként tartalmazza a program funkciójának leírását,
konstansként tárolja PI értékét,
egy másik változóban tárolja egy kör sugarának nagyságát (cm-ben megadva),
kiszámolja és a képernyőre kiírja a kör kerületét és területét!
[Megjegyzés] A szorzás jele: *

"""

import math

pi = math.pi
r = int(input("Adj meg a kör sugarának nagyságát cm-ben!: "))
kerulet = 2 * r * pi
terulet2 = r**2 * pi
terulet = pow(r, 2) * pi  # ugyanaz csak máshogy oldottuk meg
print(f"""
A kör területe: {terulet:.2f}
A kör kerülete: {kerulet:.2f}
""")
"""
2. Feladat
Készíts egy rövid programot, amely egy változóban eltárol egy szót. Próbáld meg ennek a változónak a tartalmát int értékké átalakítani. Mit tapasztalsz? Milyen üzenet jelenik meg a képernyőn?
"""
szam = input("Adjon meg egy szavat! ")
print(type(szam))
szam = int(szam)
print(type(szam))
"""
2. Feladat
Írj egy programot, ami a felhasználótól bekéri először a keresztnevét, majd a vezetéknevét. A program ezután összefűzi ezeket egy teljes_nev nevű változóba. Végül a program a teljes nevén üdvözli a felhasználót!
"""

kereszt = input("Adja meg a keresztnevét!: ")
vezetek = input("Adja meg a vezetéknevét!: ")
kereszt = kereszt.capitalize()
vezetek = vezetek.capitalize()

teljes_nev = kereszt + "\t" + vezetek
print(f"Üdvözletem {teljes_nev}")

#\n = új sor
#\t = tabulátornyi hely
"""
3. Feladat
Írj egy programot, ami bekér egy számot a felhasználótól, és valamilyen matemataikai műveletek sorozataként generál és kiír a felhasználónak egy szerencseszámot!
"""
"""
import random
print("Szerencseszám:")
szam=int(input("Adjon meg egy számot!: "))
#print(szam*4**random.randint(0, 7)/9)
"""

import random
import math

lista = ["*", "+", "/", "//", "**", "%", "-", "sqrt"]
hossz = len(lista) - 1
random_szam = random.randint(0, hossz)
random_operator = lista[random_szam]
#random_operator = random.choice(lista)

szam = int(input("Adjon meg egy számot!: "))
szam2 = int(input("Adjon meg egy másik számot!: "))


if random_operator == "*":
  print(f"{szam} {random_operator} {szam2} = {szam*szam2}")
elif random_operator == "+":
  print(f"{szam} {random_operator} {szam2} = {szam+szam2}")
elif random_operator == "/":
  print(f"{szam} {random_operator} {szam2} = {szam/szam2}")
elif random_operator == "//":
  print(f"{szam} {random_operator} {szam2} = {szam//szam2}")
elif random_operator == "**":
  print(f"{szam} {random_operator} {szam2} = {szam**szam2}")
elif random_operator == "%":
  print(f"{szam} {random_operator} {szam2} = {szam%szam2}")
elif random_operator == "-":
  print(f"{szam} {random_operator} {szam2} = {szam-szam2}")
elif random_operator == "sqrt":
  print(f"{szam} {random_operator} = {math.sqrt(szam)}")
  print(f"{szam} {random_operator} = {szam**0.5}")

#hf: Addig menjen az if, elif, amíg minden operátorral meg nem lesznek a műveletek!
