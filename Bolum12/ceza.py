"""Bölüm 12 · Kod İzleme: ceza()

Cezalı kamu malı oyununda katkılar ve ceza puanları verildiğinde kazançları
hesaplar (puan veren 1 öder, cezalı 3 kaybeder). Slayttaki kodun aynısıdır;
örnekler ders notundaki üç ceza düzenidir (Tablo 12.13): kimse ceza vermez,
O2–O4 O1'e 2'şer puan verir, yalnız O2 ve O3 verir.
"""

def ceza(c, p):         # p[i][j]: i'nin j'ye puanı
    n = len(c)
    pay = 1.6 * sum(c) / n
    u = [10 - c[i] + pay for i in range(n)]
    for i in range(n):
        for j in range(n):
            u[i] -= p[i][j]       # puan başı 1 öder
            u[j] -= 3 * p[i][j]   # cezalı 3 kaybeder
    return u


if __name__ == "__main__":
    c = [0, 10, 10, 10]
    for verenler in [[], [1, 2, 3], [1, 2]]:
        p = [[0] * 4 for _ in range(4)]
        for i in verenler:
            p[i][0] = 2
        print(verenler, ceza(c, p))

# Beklenen çıktı:
# [] [22.0, 12.0, 12.0, 12.0]
# [1, 2, 3] [4.0, 10.0, 10.0, 10.0]
# [1, 2] [10.0, 10.0, 10.0, 12.0]
