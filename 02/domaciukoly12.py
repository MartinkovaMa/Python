#V učebních materiálech jsme spolu vytvářeli program, který píše různé nesmysly podle uživatelem zadaného věku.
#
#Zkus napsat program, který píše hlášky podle zadané rychlosti chůze, váhy ulovené ryby, počtu tykadel, teploty vody nebo třeba vzdálenosti od rovníku.

#(Pošli ten nejzdařilejší; kdyby ses chtěla pochlubit několika verzemi, dej je všechny do jedné odpovědi.)
rychlost_chuze = float(input('Zadej rychlost chuze v km za hodinu:'))
cislo_je_spravne = rychlost_chuze >= 4
if cislo_je_spravne:
    print('Rychlost je optimální.')
else:
    print('Seš jak šnek.')
#odstup

vaha_ryby = float(input('Zadej váhu ryby v kilogramech:'))
císlo_je_spravne = vaha_ryby >= 2
if cislo_je_spravne:
    print("Super váha.")
else:
    print('Příště vylov prosím větší kousek.')
  #next task
pocet_tykadel = float(input('Zadej počet tykadel:'))
císlo_je_spravne = pocet_tykadel >= 2

if cislo_je_spravne:
    if pocet_tykadel == 2:
        print('To bude asi vosa.')
    if pocet_tykadel == 4:
        print('To bude asi chrobák.')
    else:
        print('To nevím, co je za hmyz.')
