import math as math
import numpy as np

### Sudut Refraksi Hukum Snell
print("Menghitung Sudut Refraksi dengan Hukum Snell (ya/tidak)")
jawab = input()
print('')

if jawab.lower() == ('ya'):
    print("Masukkan nilai: ")
    n1 = float(input("n1 = "))
    θ1 = float(input("θ1 = "))
    n2 = float(input("n2 = "))

θ2 = ((n1/n2)*math.sin(math.radians(θ1)))
arc_sin = np.arcsin(θ2)
degree_θ2 = math.degrees(arc_sin)
print("")

print("Besar sudutnya adalah:",round(degree_θ2,1),"\u00b0")
