import random

allcaracter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

long = int(input("Şifre uzunluğu"))

password = ""

for i in range(long):
    password += random.choice(allcaracter)


print(password)
