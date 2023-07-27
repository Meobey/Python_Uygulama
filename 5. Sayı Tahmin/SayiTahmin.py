from random import randint
def sayi_oyunu():
    rand=randint(1, 999)
    sayac=0
    sayi=0
    while True:
        sayac += 1
        if sayi == 0:
            sayi = int(input("\n1 İle 999 Arasında Değer Girin:"+" "))
        if sayi < rand:
            sayi = int(input("\nDaha Büyük Bir Sayı Girin:"+" "))
            continue
        elif sayi > rand:
            sayi = int(input("\nDaha Küçük Bir Sayı Girin:"+" "))
            continue
        else:
            print("Rastele Seçilen Sayı {0}!".format(rand))
            print("Tahmin sayınız {0}".format(sayac))
            break
    
def baslangic():
    a = input("Oynamak ister misiniz?")
    if a == "yes":
        sayi_oyunu()
    elif a == "no" or a == "exit":
        raise SystemExit
    else:
        pass

while True:
    baslangic()
    continue
 