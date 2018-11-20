import random
file_obj = open("text.txt", "r")
praeitas_ilgis = 0

for zodis in file_obj.readlines():
    ilgiausias_zodis = len(zodis[:-1])
    if praeitas_ilgis < ilgiausias_zodis:
        praeitas_ilgis = ilgiausias_zodis
        test = zodis
while True:

    try:
        lygis = int(raw_input("{} {} 2-{}".format("iveskite", "lygi", praeitas_ilgis)))
        break
    except ValueError:
        print "Prasome ivesti skaiciu"

file_obj = open("text.txt", "r")


zodziu_sarasas = []
for zodis in file_obj.readlines():
    zodzio_ilgis = len(zodis[:-1])
    if zodzio_ilgis <= lygis and zodzio_ilgis >= 2:
        zodziu_sarasas.append(zodis.rstrip())

zodis_kuri_reikia_atspeti = random.choice(zodziu_sarasas)
print 'Zodis turi', len(zodis_kuri_reikia_atspeti), 'raides'
pasleptas_zodis = "_" * len(zodis_kuri_reikia_atspeti)
print "_" * len(zodis_kuri_reikia_atspeti)

zodis_neatspetas = True
spejimai = 6
skaitliukas = 0

while zodis_neatspetas:
    print ("")
    spejama_raide = raw_input('Spekite_raide: ')

    if (spejama_raide.isdigit()):
        print("Jus ivedete skaiciu. Prasome ivesti raide")
    else:

        if spejama_raide in zodis_kuri_reikia_atspeti:
            paslepto_zodzio_listas = list(pasleptas_zodis)

            for index, raide in enumerate(zodis_kuri_reikia_atspeti):
                if raide == spejama_raide:
                    paslepto_zodzio_listas[index] = spejama_raide
            pasleptas_zodis = "".join(paslepto_zodzio_listas)
            print "Spejimas teisingas  ", pasleptas_zodis

        else:
            pass

            print "Sios raides zodyje nera"

            if spejama_raide not in zodis_kuri_reikia_atspeti:
                skaitliukas += 1
                print 'Likusiu spejimu skaicius:', spejimai-skaitliukas
                print HANGMANPICS[skaitliukas]

        if pasleptas_zodis == zodis_kuri_reikia_atspeti:
            print "Zaidimas laimetas"
            zodis_neatspetas = False
        elif spejimai-skaitliukas == 0:
            print "Zaidimas pralaimetas, zodis, kuri reikejo atspeti, buvo = ", zodis_kuri_reikia_atspeti
            zodis_neatspetas = False

print "Ar noretumete zaisti dar karta?"
print "Jei taip, rasykite 1, jei ne, rasykite 2"

dar_karta = str(raw_input("> "))
if dar_karta == '1':
 exec (open("./hangman.py").read())
else:
 print 'Bye!'
quit()