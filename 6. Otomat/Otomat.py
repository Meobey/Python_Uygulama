def menu():
    dil = input("Select Language(tr/en):")
    if dil == "tr" or dil =="en" or dil == "TR" or dil =="EN":
        toplam_ucret = 0
        if dil == "en" or dil =="EN":
            print("""
  SNEAKS
-------------
 1- Burger (60₺)
 2- Doner (40₺)
 3- Hotdog (25₺)
 4- Pizza (30₺)
 5- Sandvich (20₺)
                
  DRINKS
-------------
 6- Coke (15₺)
 7- Ayran (10₺)
 8- Limonade (20₺)
 9- Orange Juice (25₺)
 10- Water (5₺)
        """)
            while True:
                secim=int(input("What would you like?\t\t=>"))
                adet= int(input("How many would you like?\t=>"))
                if secim == 1:
                    toplam_ucret += adet * 60
                elif secim == 2:
                    toplam_ucret += adet * 40
                elif secim == 3:
                    toplam_ucret += adet * 25
                elif secim == 4:
                    toplam_ucret += adet * 30
                elif secim == 5:
                    toplam_ucret += adet * 20
                elif secim == 6:
                    toplam_ucret += adet * 15
                elif secim == 7:
                    toplam_ucret += adet * 10
                elif secim == 8:
                    toplam_ucret += adet * 20
                elif secim == 9:
                    toplam_ucret += adet * 25
                elif secim == 10:
                    toplam_ucret += adet * 5
                sor=input("Anything else?(y/n)\t\t=>")
                if sor == "n":
                    a = input("Are you sure?(y/n)\t\t=>")
                    if a == "y":
                        print("Total Price:",toplam_ucret,"₺")
                        print("Have a nice meal. See you again. Bye :)")
                        break
                    else:
                        pass
        elif dil == "tr" or dil == "TR":
            print("""
  Atıştırmalıklar
-------------
 1- Burger (60₺)
 2- Döner (40₺)
 3- Hotdog (25₺)
 4- Pizza (30₺)
 5- Sandvich (20₺)
                
  DRINKS
-------------
 6- Kola (15₺)
 7- Ayran (10₺)
 8- Limonata (20₺)
 9- Portakal Suyu (25₺)
 10- Su (5₺)
        """)
            while True:
                secim=int(input("Ne istersiniz?\t\t\t=>"))
                adet= int(input("Kaç tane istersiniz?\t\t=>"))
                if secim == 1:
                    toplam_ucret += adet * 60
                elif secim == 2:
                    toplam_ucret += adet * 40
                elif secim == 3:
                    toplam_ucret += adet * 25
                elif secim == 4:
                    toplam_ucret += adet * 30
                elif secim == 5:
                    toplam_ucret += adet * 20
                elif secim == 6:
                    toplam_ucret += adet * 15
                elif secim == 7:
                    toplam_ucret += adet * 10
                elif secim == 8:
                    toplam_ucret += adet * 20
                elif secim == 9:
                    toplam_ucret += adet * 25
                elif secim == 10:
                    toplam_ucret += adet * 5
                sor=input("Başka bir şey?(y/n)\t\t=>")
                if sor == "n":
                    a = input("Emin misiniz? (y/n)\t\t=>")
                    if a == "y":
                        print("Toplam Ücret:",toplam_ucret,"₺")
                        print("Afiyet olsun. Tekrar görüşmek üzere. Bay bay :)")
                        break
                    else:
                        pass
                        
                    
                    
                        
                   
    else:
        print ("PLEASE SELECT TR OR EN !")     
        menu()

menu()
input()