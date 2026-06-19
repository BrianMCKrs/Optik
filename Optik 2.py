import math as math
import numpy as np

#Cermin Cekung
print("Menghitung Jarak Benda pada Cermin Cekung? (ya/tidak)")
jawab = input()
print('')

if jawab.lower() == ('ya'):
    print("Fokus(fo) atau Perbesaran(M+)")
    jawab2 = input()
    print('')
    ### Menghitung Fokus, Jarak Benda dan Bayangan ke Cermin
    if jawab2.lower() == ('fo'):
        print("Menghitung fokus(f) berdasarkan jari-jari lengkungan (1) atau jarak benda (2)?")
        rumus1 = input()
        ### Menghitung Fokus (f)
        if rumus1 == ('1'):
            print("Masukkan nilai:")
            r1 = float(input("r = "))
            f1 = 1/2*r1
            print("Titik fokusnya adalah:",round(f1,2))
        elif rumus1 == ('2'):
            print("Menghitung fokus (f), jarak benda (s), atau jarak bayangan (s')?")
            rumus2 = input()
            if rumus2.lower() == ('f'):
                print("Masukkan nilai:")
                s2 = float(input("s = "))
                s_2= float(input("s' = "))
                f2 = 1/(1/s2 + 1/s_2)
                print("Titik fokusnya adalah:", round(f2,2))
            elif rumus2.lower() == ('s'):
                print("Masukkan nilai:")
                f3 = float(input("f = "))
                s_3= float(input("s' = "))
                s3 = 1/(1/f3 - 1/s_3)
                print("Jarak benda ke cermin adalah:",round(s3,2))
            elif rumus2.lower == ("s'"):
                print("Masukkan nilai:")
                f4 = float(input("f = "))
                s4 = float(input("s = "))
                s_4= 1/(1/f4 - 1/s4)
                print("Jarak bayangan ke cermin adalah:",round(s_4,2))
            else:
                print("Anda tidak sedang menghitung!")
        else:
            print("Anda tidak sedang menghitung!")
    ### Menghitung Perbesaran (M)
    elif jawab2.lower() == ('m+'):
        print("Menghitung perbesaran bayangan (M), jarak bayangan (s') atau tinggi bayangan (y'), dan jarak benda (s) atau tinggi benda (y)")
        rumus3 = input()
        if rumus3.lower() == ('M'):
            print("Masukkan nilai:")
            s_5= float(input("s' = "))
            s5 = float(input("s = "))
            m1 = abs(s_5/s5)
            print("Perbesaran bayangannya adalah:", round(m1,2))
        elif rumus3.lower() in ['y', 's']:
            print("Masukkan nilai:")
            m2 = float(input("M = "))
            y1 = float(input("y atau s = "))
            y_1 = m2 * y1
            print("Jarak/tinggi bayangan yang terbentuk adalah:", round(y_1,2))
        elif rumus3.lower() in ["y'", "s'"]:
            print("Masukkan Nilai:")
            m3 = float(input("M = "))
            y_2 = float(input("y' atau s' = "))
            y2 = m3 * y_2
            print("Jarak/tinggi benda adalah:", round(y2,2))
        else:
            print("Anda tidak sedang menghitung!")
    else:
        print("Anda tidak sedang menghitung!")
else:
    print("Anda tidak sedang menghitung!")