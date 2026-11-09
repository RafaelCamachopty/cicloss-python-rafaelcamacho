s=0
c=0
n=float(input("nota(-1 para terminar):"))
while n != -1:
    s+=n
    c+= 1
    n=float(input("nota(-1par terminar )"))
if c > 0:
    print("promedio",s/c)
else:
    print("nota no dada")