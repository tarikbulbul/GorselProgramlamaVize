email = input("Email adresinizi giriniz. ")
is_email = False
for char in email: 
    if char == "@":
        is_email = True
if is_email: 
    print ("Email Adresi Doğru")
else: 
    print ("Email Adresi Yanlış")