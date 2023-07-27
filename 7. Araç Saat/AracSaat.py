#Araç-Saat Ayarlayıcı

import random
import math

saat = []
sayim = 0

for i in range(0,6000,1):
        a = 6 + ((i/6000)/(5/3))
        saat.append(a)
for i in range(0,6000,1):
        a = 7 + ((i/6000)/(5/3))
        saat.append(a)
for i in range(0,2000,1):
        a = 8 + ((i/2000)/(5/3))
        saat.append(a)
for i in range(0,2000,1):
        a = 9 + ((i/2000)/(5/3))
        saat.append(a)


for i in range(1,16001,1):
    
        rastgeledeger=random.choice(saat)
        saat.remove(rastgeledeger)
        rastgeledeger1=random.choice(saat)
        saat.remove(rastgeledeger1)
        rastgeledeger2=random.choice(saat)
        saat.remove(rastgeledeger2)
        rastgeledeger3=random.choice(saat)
        saat.remove(rastgeledeger3)
        rastgeledeger4=random.choice(saat)
        saat.remove(rastgeledeger4)

        a = rastgeledeger % 1
        b = rastgeledeger1 % 1
        c = rastgeledeger2 % 1
        d = rastgeledeger3 % 1
        e = rastgeledeger4 % 1

        ana = (a * (5/3) + b * (5/3) + c * (5/3) + d * (5/3) + e * (5/3) )
        aslan=math.trunc(ana)
        kaplan=ana-aslan
        kaypak=kaplan*(3/5)
        abi=kaypak+aslan
        abi=round(abi,2)
       
        aa=math.trunc(rastgeledeger)
        ab=math.trunc(rastgeledeger1)
        ac=math.trunc(rastgeledeger2)
        ad=math.trunc(rastgeledeger3)
        ae=math.trunc(rastgeledeger4)

        baba = aa + ab + ac + ad + ae + abi
        total = baba - (35) 
        if total<0: 
            if kaypak>0:
                total = baba + 0.4 - 35
        
        if total < 0.2 and total > -0.2:
            sayim = sayim + 1
            print("\n{:03d} Numaralı Araç = Pazartesi: {:4.2f}   Salı: {:4.2f}   Çarşamba: {:4.2f}   Perşembe: {:4.2f}   Cuma: {:4.2f} Total: {:5.2f}\n".format(sayim,rastgeledeger,rastgeledeger1,rastgeledeger2,rastgeledeger3,rastgeledeger4,total))     
        if sayim >= 100:
            break        
while True:
    pass
