"""Bölüm 2 · Kod İzleme: Nim XOR

Nim oyununda yığınların nim toplamını (XOR) hesaplar ve toplamı 0 yapan kazandıran
hamleyi bulup uygular. Slayttaki kodun aynısıdır.
"""

yiginlar = [3, 4, 5]
x = 0
for h in yiginlar:
    x ^= h            # nim toplamı (XOR)
for i, h in enumerate(yiginlar):
    if h ^ x < h:     # küçültülebilir mi?
        yiginlar[i] = h ^ x
        print("yığın", i, ":", h, "->", h ^ x)
        break
print(yiginlar)


# Beklenen çıktı:
# yığın 0 : 3 -> 1
# [1, 4, 5]
