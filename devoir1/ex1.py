age=int(input("entrer ton age : "))

if age < 0:
    print("age invalide")
elif age <= 12:
    print("tu es enfant")
elif age <= 17:
    print("tu es adolescent")
elif age <= 64:
    print("tu es adulte ")
else:
    print("tu es senior")