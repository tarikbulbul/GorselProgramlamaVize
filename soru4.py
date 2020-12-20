sayac = 0

for i in range(100, 1000):
    sayi = str(i)
    if sayi[0] == sayi[1]:
        print(sayi, "Bu sayının rakamları farklı değil")
    elif sayi[0] == sayi[2]:
        print(sayi, "Bu sayının rakamları farklı değil")
    elif sayi[1] == sayi[2]:
        print(sayi, "Bu sayının rakamları farklı değil")
    else:
        sayac += 1
        print(i)

print("Rakamları farklı olan toplam sayı:",sayac)