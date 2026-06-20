import matplotlib.pyplot as plt

#Cermin Cekung

#Diagram Sinar
def diagram_sinar(f,s,s_aksen,m_perbesaran,h = 3):
    if s_aksen > 0:
        h_titik = -m_perbesaran * h
    else:
        h_titik = m_perbesaran * h
    
    plt.figure(figsize=(10, 6))
    plt.title("Diagram Sinar", fontsize=14, fontweight='bold')
    plt.xlabel("Sumbu X (Jarak)")
    plt.ylabel("Sumbu Y (Tinggi)")
    plt.axhline(0, color='black', linewidth=1, linestyle='--')
    plt.axvline(0, color='gray', linewidth=5, label='Cermin Cekung')
    ### Titik Fokus & Kelengkungan 
    plt.plot(-f, 0, 'ro', label=f'Fokus (F = -{f:.2f})')
    plt.plot(-2*f, 0, 'bo', label=f'Pusat Kelengkungan (R = -{2*f:.2f})')
    ### Anak Panah
    plt.arrow(-s, 0, 0, h, head_width=0.3, head_length=0.3, fc='green', ec='green', length_includes_head=True, label=f'Benda (s={s:.2f})')
    plt.arrow(-s_aksen, 0, 0, h_titik, head_width=0.3, head_length=0.3, fc='red', ec='red', length_includes_head=True, label=f"Bayangan (s'={s_aksen:.2f})")
    ### Sinar Istimewa 1
    plt.plot([-s, 0], [h, h], color='orange', linestyle='-', linewidth=1.5)
    plt.plot([0, -s_aksen], [h, h_titik], color='orange', linestyle='-', linewidth=1.5, label='Sinar 1 (Sejajar -> Fokus)')
    ### SInar Istimewa 2
    plt.plot([-s, 0], [h, h_titik], color='purple', linestyle='-', linewidth=1.5)
    plt.plot([0, -s_aksen], [h_titik, h_titik], color='purple', linestyle='-', linewidth=1.5, label='Sinar 2 (Fokus -> Sejajar)')
    plt.grid(True, which='both', linestyle=':', alpha=0.5)
    plt.legend(loc='upper left')
    plt.show()

#Menghitung Cermin Cekung
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
            print(" ")
            print("Jika ingin menampilkan gambar, jarak diketahui (Ya/Tidak)")
            tampil_gambar1 = input()
            if tampil_gambar1.lower() == ("ya"):
                print("Masukkan jarak benda (s)")
                s_input1 = float(input("s = "))
                s_aksen_hitung1 = 1 / (1/f1 - 1/s_input1)
                m_hitung1 = abs(s_aksen_hitung1 / s_input1)
                diagram_sinar(f1, s_input1, s_aksen_hitung1, m_hitung1)
            else:
                print("")
        elif rumus1 == ('2'):
            print("Menghitung fokus (f), jarak benda (s), atau jarak bayangan (s')?")
            rumus2 = input()
            if rumus2.lower() == ('f'):
                print("Masukkan nilai:")
                s2 = float(input("s = "))
                s_2= float(input("s' = "))
                f2 = 1/(1/s2 + 1/s_2)
                print("Titik fokusnya adalah:", round(f2,2))
                print(" ")
                print("Ingin menampilkan gambar? (Ya/Tidak)")
                tampil_gambar2 = input()
                if tampil_gambar2.lower() == ("ya"):
                   m_hitung2 = abs(s_2 / s2)
                   diagram_sinar(f2, s2, s_2, m_hitung2)
                else:
                    print("Terima kasih")
            elif rumus2.lower() == ('s'):
                print("Masukkan nilai:")
                f3 = float(input("f = "))
                s_3= float(input("s' = "))
                s3 = 1/(1/f3 - 1/s_3)
                print("Jarak benda ke cermin adalah:",round(s3,2))
                print(" ")
                print("Ingin menampilkan gambar? (Ya/Tidak)")
                tampil_gambar3 = input()
                if tampil_gambar3.lower() == ("ya"):
                   m_hitung3 = abs(s_3 / s3)
                   diagram_sinar(f3, s3, s_3, m_hitung3)
                else:
                    print("Terima kasih")
            elif rumus2.lower() == ("s'"):
                print("Masukkan nilai:")
                f4 = float(input("f = "))
                s4 = float(input("s = "))
                s_4= 1/(1/f4 - 1/s4)
                print("Jarak bayangan ke cermin adalah:",round(s_4,2))
                print(" ")
                print("Ingin menampilkan gambar? (Ya/Tidak)")
                tampil_gambar4 = input()
                if tampil_gambar4.lower() == ("ya"):
                   m_hitung4 = abs(s_4 / s4)
                   diagram_sinar(f4, s4, s_4, m_hitung4)
                else:
                    print("Terima kasih")
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
            print(" ")
            print("Ingin menampilkan gambar? (Ya/Tidak)")
            tampil_gambar5 = input()
            if tampil_gambar5.lower() == ("ya"):
               f_hitung1 = 1 / (1 / s5 + 1 / s_5)
               diagram_sinar(f_hitung1, s5, s_5, m1)
            else:
                print("Terima kasih")
        elif rumus3.lower() in ['y', 's']:
            print("Masukkan nilai:")
            m2 = float(input("M = "))
            y1 = float(input("y atau s = "))
            y_1 = m2 * y1
            print("Jarak/tinggi bayangan yang terbentuk adalah:", round(y_1,2))
            print(" ")
            print("Jika ingin menampilkan gambar, jarak diketahui (Ya/Tidak)")
            tampil_gambar6 = input()
            if tampil_gambar6.lower() == ("ya"):
                print("Masukkan fokus (f)")
                f_hitung2 = float(input("f = "))
                diagram_sinar(f_hitung2, y1, y_1, m2)
            else:
                print("Terima kasih")
        elif rumus3.lower() in ["y'", "s'"]:
            print("Masukkan Nilai:")
            m3 = float(input("M = "))
            y_2 = float(input("y' atau s' = "))
            y2 = y_2/m3
            print("Jarak/tinggi benda adalah:", round(y2,2))
            print(" ")
            print("Jika ingin menampilkan gambar, jarak diketahui (Ya/Tidak)")
            tampil_gambar6 = input()
            if tampil_gambar6.lower() == ("ya"):
                print("Masukkan fokus (f)")
                f_hitung3 = float(input("f = "))
                diagram_sinar(f_hitung3, y2, y_2, m2)
            else:
                print("Terima kasih")
        else:
            print("Anda tidak sedang menghitung!")
    else:
        print("Anda tidak sedang menghitung!")
else:
    print("Anda tidak sedang menghitung!")