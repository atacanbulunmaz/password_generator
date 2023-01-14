import random

uppercaseLetters = ("ABCDEFGHIJKLMNOPQRTSTUVWXYZ")
lowercaseLetters = uppercaseLetters.lower()
#print(lowercaseLetters)
digits = ("-_.,/*")
symbols = ("0123456789")

upper,lower,nums,syms = True, True, True, True

all =" "

if upper:
    all += uppercaseLetters
if lower:
    all += lowercaseLetters
if nums:
    all += digits
if syms:
    all += symbols


amount = int(input("Kac adet sifre olusturmak istiyorsunuz : "))
length = int(input("Ka karakterli sifre olusturmak istiyorsunuz : "))

for i in  range (amount):
    password = " ".join(random.sample(all,length))
    print(password)
    