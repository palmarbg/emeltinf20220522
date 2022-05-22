def foglalt(x, y):
    return not tabla[int(x)-1][int(y)-1]=='0'

def sorfoglalt(y, szam):
    for i in tabla[int(y)-1]:
        if szam==i:
            return True
    return False

def oszlopfoglalt(x, szam):
    for i in tabla:
        if szam==i[int(x)-1]:
            return True
    return False

def reszfoglalt(y, x, szam):
    for i in range((( (int(y)-1) //3 )*3), (( (int(y)-1) //3 )*3+3)):
        for j in range((( (int(x)-1) //3 )*3), (( (int(x)-1) //3 )*3+3)):
            if szam==tabla[i][j]:
                return True
    return False

#1. és 2. feladat
print("1. feladat")
filename=input("Adja meg a bemeneti fájl nevét! ")
sor=int(input("Adja meg egy sor számát! "))
oszlop=int(input("Adja meg egy oszlop számát! "))
bemenet = open(filename)
tabla=[]
tomb=[]
z=0
for i in bemenet:
    if z<9:
        tabla.append(i.strip().split())
        
    else:
        tomb.append(i.strip().split())
    z+=1
bemenet.close()
print(tabla)
print(tomb)

print("\n3. feladat")
print(f'Az adott helyen szereplő szám: {tabla[sor-1][oszlop-1]}')
print(f'A hely a(z) {((sor-1)//3)*3+(oszlop-1)//3+1} résztáblához tartozik.')

print("\n4. feladat")
a=sum([row.count("0") for row in tabla])/81*100
print("Az üres helyek aránya: {:.1f}%".format(round(a, 1)))

print("\n5. feladat")
for i in tomb:
    print(f'A kiválasztott sor: {i[1]} oszlop: {i[2]} a szám: {i[0]}')
    if foglalt(i[1], i[2]):
        print("A helyet már kitöltötték.\n")
    elif sorfoglalt(i[1], i[0]):
        print("Az adott sorban már szerepel a szám.\n")
    elif oszlopfoglalt(i[2], i[0]):
        print("Az adott oszlopban már szerepel a szám.\n")
    elif reszfoglalt(i[1], i[2], i[0]):
        print("Az adott résztáblázatban már szerepel a szám.\n")
    else:
        print("A lépés megtehető.\n")
