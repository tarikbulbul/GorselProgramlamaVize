kelime = input("Herhangi birşey yazınız:")
aranan = input("Aramak istedğiniz ifadeyi yazınır.")

dizi = kelime.split(aranan)
if len(dizi[0]) > 0 and len(dizi[1]) > 0:
    print(dizi[0][-1]+aranan+dizi[1][0])

elif len(dizi[0]) > 0 and len(dizi[1]) == 0:
    print(dizi[0][-1]+aranan+dizi[1])

elif len(dizi[0]) == 0 and len(dizi[1]) > 0:
    print(dizi[0]+aranan+dizi[1][0])
