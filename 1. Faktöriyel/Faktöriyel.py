anahtar =1
while anahtar == 1:
   sayi = int(input("Faktöriyeli hesaplanicak değeri girin: "))
   if sayi =="q":
      anahtar=0
   toplam = 1
   for i in range(1,sayi):
      toplam *= i
   print("\n",sayi,"! =",toplam,"\n")
pass

   


   