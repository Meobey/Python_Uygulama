import math
while True:

    def kitap_satis(adet, kitap_turu, sayfa_sayisi):


        if kitap_turu == "A" or kitap_turu == "a":
            kitap_alis_fiyati = 80
        elif kitap_turu == "B" or kitap_turu == "b":
            kitap_alis_fiyati = 65
        elif kitap_turu == "C" or kitap_turu == "c":
            kitap_alis_fiyati = 50
        else:
            kitap_alis_fiyati = 35
    
        if adet < 101 and adet > 20:
            nadirlik_payi = 1.1
        elif adet <= 20 and adet > 0:
            nadirlik_payi = 1.2
        elif adet == 0:
            print("Maalesef Stoklarımızda Kalmadı.")
        else:
            nadirlik_payi = 1
        
        if sayfa >= 100:
            t = math.sqrt(sayfa)
        else:
            t = 0

        kdv = 1.2
        kar_payi = 1.25

        kitap_satis_fiyati = (kitap_alis_fiyati * kdv * kar_payi * nadirlik_payi) + t 
        dekont(kitap_satis_fiyati)

    def dekont(tutar):
        tutar = int(tutar)
        print("\nÖdenecek Tutar: ", tutar, "TL")

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    isim = input("Kitap Adını Giriniz: ")
    kitap_adeti = input ("Stoktaki Kitap Sayısı: ")
    adet = int(kitap_adeti)
    tur = input ("Kitap Türünü Giriniz: ")
    sayfa_sayisi = input("Sayfa Sayısını Giriniz: ")
    sayfa = int(sayfa_sayisi)
    kitap_satis(adet, tur, sayfa)
pass