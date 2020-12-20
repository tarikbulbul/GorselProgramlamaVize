            # ÖRNEK DEĞERLERDEN BİRİNİ GİRİNİZ
# örnek deger : receive-23-1-0\n
# örnek deger : send-181-3-0-1\nreceive-170-3-0\n 
# örnek deger : receive-150-0-1\n0-4-5-6-\n 


deger = input("Deger yazınız: \n")
degerler = deger.split("\\n")[:-1] 




for deger in degerler: 
    parts = deger.split('-')
    if parts[0] not in ['receive', 'send']: 
        print ("Error: send yada receive bulunmuyor ")
        continue
    if int(parts[1]) not in range(0, 256): 
        print ("Error: birinci bolum hatali ")
        continue
    if int(parts[2]) not in [1,2,3,4]: 
        print ("Error: ikinci bolum hatali ")
        continue
    if int(parts[3]) not in [0,1]: 
        print ("Error: ucuncu bolum hatali ")
        continue
    if parts[0] == 'send' and int(parts[4]) not in [0,1]: 
        print ("Error: dorduncu bolum hatali ")
        continue
    
    if parts[0] == 'receive': 
        print ("Kod Tipi : receive - Gelen")
    elif parts[0] == 'send': 
        print ("Kod Tipi : send - Giden")
    
    if int(parts[1]) >= 0 and int(parts[1]) <= 50: 
        print ("Sinyal Gucu :", parts[1], "- Cok Zayif")
    elif int(parts[1]) > 50 and int(parts[1]) <= 100: 
        print ("Sinyal Gucu :", parts[1], "- Zayif")
    elif int(parts[1]) > 100 and int(parts[1]) <= 150: 
        print ("Sinyal Gucu :", parts[1], "- Orta")
    elif int(parts[1]) > 150 and int(parts[1]) <= 200: 
        print ("Sinyal Gucu :", parts[1], "- Guclu")
    elif int(parts[1]) > 200 and int(parts[1]) <= 255: 
        print ("Sinyal Gucu :", parts[1], "- Cok Guclu")
        
    if int(parts[2]) == 1: 
        print ("Cihaz :", parts[2], "- Camasir Makinesi")
    elif int(parts[2]) == 2: 
        print ("Cihaz :", parts[2], "- Firin")
    elif int(parts[2]) == 3: 
        print ("Cihaz :", parts[2], "- Buzdolabi")
    elif int(parts[2]) == 4: 
        print ("Cihaz :", parts[2], "- Televizyon")
        
    if int(parts[3]) == 0: 
        print ("Durumu :", parts[3], "- Off")
    elif int(parts[3]) == 1: 
        print ("Durumu :", parts[3], "- On")
    
    if parts[0] == 'send': 
        if int(parts[4]) == 0: 
            print ("Cevap :", parts[4], "- Istenmiyor")
        elif int(parts[4]) == 1: 
            print ("Cevap :", parts[4], "- Isteniyor")
        
