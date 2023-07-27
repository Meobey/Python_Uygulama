anahtar = 1
while anahtar == 1 :
    def maas_hesaplama(calisan_ismi, calisma_saati, robot_sektor):
        if robot_sektor == "A":
            saatlik_maas = 20
        elif robot_sektor == "B":
            saatlik_maas = 17
        elif robot_sektor == "C":
            saatlik_maas = 14
        else:
            saatlik_maas = 11
        if calisma_saati >= 160: 
            bonus = 500
        elif calisma_saati >= 140:
            bonus = 150
        else:
            bonus = 0
        maas = (calisma_saati * saatlik_maas) + bonus
        print (calisan_ismi, "Maasiniz: ", maas, "TL")

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    isim = input("Robot Adını Giriniz: ")
    saat = input ("Robot Çalışma Saati: ")
    saat = int(saat)
    sektor = input ("Robotun Çalıştığı Sektör: (A,B,C)")
    maas_hesaplama(isim, saat, sektor)
pass