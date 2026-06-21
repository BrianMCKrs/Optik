#Kekuatan Lensa

print("Menghitung kekuatan lensa (Ya/Tidak)")
jawab = input()
print('')

if jawab.lower() == ('ya'):
    print("Menghitung kekuatan lensa(P) atau fokus(f)")
    jawab2 = input()
    print('')
    
    #Menghitung kekuatan lensa dari fokus
    if jawab2.lower() == ('p'):
        print("Masukkan nilai: ")
        f1 = float(input("f = (cm)"))
        p1 = 100/f1
        print("Kekuatan lensanya adalah:",round(f1,2))
    elif jawab2.lower() == ('f'):
        print("Masukkan nilai: ")
        p2 = float(input("p = "))
        f2 = 100/p2
        print("Titik fokusnya adalah:",round(f2,2))
    else:
        print("Anda tidak sedang menghitung!")
else:
    print("Anda tidak sedang menghitung!")    