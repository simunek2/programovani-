# delala i Maky s Elou :)
def pocet_vyher(T=60, rekord=601):
    x = range(T + 1)

    vyhry = 0

    for doba in x:
        d = T*doba-doba**2

        if d > rekord:
            vyhry = vyhry + 1
    return vyhry

# vyhry01 = pocet_vyher(T=60, rekord=601)
# vyhry02 = pocet_vyher(80, 1163)
# vyhry03 = pocet_vyher(86, 1559)
# vyhry04 = pocet_vyher(76, 1300)

# y = vyhry01*vyhry02*vyhry03*vyhry04

# print(y)

soucin = 1
for T, rekord in [(60, 601), (80, 1163), (86, 1559), (76, 1300)]:
    soucin = soucin * pocet_vyher(T=T, rekord=rekord)
print(soucin)
