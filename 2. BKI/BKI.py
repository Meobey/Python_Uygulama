#Boy Kilo İndeks Hesaplayici
print(" Vücut Kitle İndeksi Hesaplama")
anahtar=1
while anahtar==1:
    print("\n***************************************\n")
    isim = str(input("Adınız: "))
    boy = float(input("Boyunuz(cm): "))
    kilo = float(input("Kilonuz(kg): "))
    boy = boy /100
    indeks = kilo / (boy*boy)
    indeks = round(indeks,2)
    print("VKI Değeriniz: ",indeks)
    if indeks<=18.5:
        print("Normal Kilonun Altındasınız.")
    elif indeks<=24.99:
        print("Normal Kilodasınız.")
    elif indeks<=29.99:
        print("Fazla Kilolusunuz.")
    elif indeks>=30.00:
        print("Aşırı Fazla Kilolusunuz.")
pass