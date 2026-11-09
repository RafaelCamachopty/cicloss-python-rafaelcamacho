secreto=7
i= int(input("adicina el numero(1 al 10):"))
while i != secreto:
    if i < secreto:
        print("muy bajo")
    else:
        print("alto")
    i=int(input("intenta de nuevo: "))
print("la pegaste")