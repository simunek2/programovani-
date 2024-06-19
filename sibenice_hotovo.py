import random
hlavni_mesta_evropy = ["tirana", "andorra la vella", "jerevan", "vídeň", "baku", "minsk", "brusel", "sarajevo", "sofie", "záhřeb", "nikósie", "praha", "kodaň", "tallinn", "helsinky", "paříž", "tbilisi", "berlín", "atény", "budapešť", "reykjavík", "dublin", "řím", "nur-sultan (astana)", "priština", "riga", "vaduz", "vilnius", "lucemburk", "valletta", "kišiněv", "monako", "podgorica", "amsterdam", "skopje", "oslo", "varšava", "lisabon", "bukurešť", "moskva", "san marino", "bělehrad", "bratislava", "lublaň", "madrid", "stockholm", "bern", "ankara", "kyjev", "londýn", "vatikán"]
random_mesto = random.choice(hlavni_mesta_evropy)

import turtle               # allows us to use the turtles library
wn = turtle.Screen()        # creates a graphics window
t = turtle.Turtle()

counter = 0

slovo = random_mesto
spravne = set(slovo)
znak = len(spravne)
pocet_znak = 0
cislo = int(znak)

uhodnuta_pismena = []
pouzita_pismena = []

for _ in range(cislo):
        print("_", end=" ")

print()

while True:

    hadane_pismeno = input("zadej_pismeno: ")

    if len(hadane_pismeno) != 1:
        print("pouze_jedno_pismeno")
        continue


    je_tam = hadane_pismeno in slovo

    if hadane_pismeno == "`":
        break

    if hadane_pismeno in pouzita_pismena:
        print("uz_si hadal")

    else:
        if je_tam:
            pocet_znak = pocet_znak + 1
            print(hadane_pismeno, "tam je.")

            if pocet_znak == znak:
                print("VYHRAL_JSI")
                break
            else:
                for pismeno_ze_slova in slovo:
                    if pismeno_ze_slova == hadane_pismeno:
                        print(pismeno_ze_slova, end=" ")

                        uhodnuta_pismena.append(pismeno_ze_slova)
                        # uhodnuta_pismena = uhodnuta_pismena + [pismeno_ze_slova]
                    elif pismeno_ze_slova in uhodnuta_pismena:
                        print(pismeno_ze_slova, end=" ")
                    else:
                        print("_", end=" ")
              
            print()
        else:
            counter = counter + 1
            print(hadane_pismeno, "tam neni.")
            print("pocet_chyb_je",counter)

            if counter == 1:
                t.penup()
                t.right(90)
                t.forward(200)
                t.left(90)
                t.forward(120)
                t.left(180)
                t.pendown()
                t.forward(240)
                t.left(180)
                t.forward(20)
                t.left(90)
                t.circle(-100,180)

            if counter == 2:
                t.penup()
                t.right(135)
                t.forward(20000**0.5)
                t.pendown()
                t.right(45)
                t.forward(200)

            if counter == 3:
                t.left(90)
                t.forward(20)
                t.left(180)
                t.forward(150)
                t.right(90)
                t.forward(20)
                t.left(180)
                t.forward(20)
                t.left(90)
                t.forward(110)
                t.left(45)
                t.forward(800**0.5)

            if counter == 4:
                t.penup()
                t.left(135)
                t.forward(130)
                t.pendown()
                t.circle(-20)

            if counter == 5:
                t.penup()
                t.right(90)
                t.forward(40)
                t.pendown()
                t.forward(80)

            if counter == 6:
                t.right(30)
                t.forward(80)

            if counter == 7:
                t.back(80)
                t.left(60)
                t.forward(80)

            if counter == 8:
                t.back(80)
                t.right(30)
                t.back(70)
                t.right(30)
                t.forward(60)

            if counter == 9:
                t.back(60)
                t.left(60)
                t.forward(60)
                print("PROHRÁL_JSI")
                print("slovo bylo",slovo)
                turtle.done()
                break

     
    pouzita_pismena.append(hadane_pismeno)
