# import turtle
# slovo = turtle.Screen()
# t = turtle.Turtle()

# for i in range(6):
#     t.pendown()
#     t.forward(20)
#     t.penup()
#     t.forward(10)
counter=0

slovo = "postel"

uhodnuta_pismena = []
pouzita_pismena = []

while True:
    hadane_pismeno = input("zadej_pismeno: ")


    je_tam = hadane_pismeno in slovo

    if hadane_pismeno in pouzita_pismena:
        print("uz_si hadal")

    else:
        if je_tam:
            print(hadane_pismeno, "tam je.")

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
    pouzita_pismena.append(hadane_pismeno)
    
