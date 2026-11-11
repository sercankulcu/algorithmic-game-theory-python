"""Bölüm 12 · Kod İzleme: juri()

Condorcet jüri teoremi: her biri p olasılıkla doğru oy veren n bağımsız
seçmende çoğunluğun doğru olma olasılığını binom toplamıyla hesaplar.
Slayttaki kodun aynısıdır.
"""

from math import comb
def juri(n, p):
    toplam = 0
    for k in range(n // 2 + 1, n + 1):
        terim = comb(n, k) * p**k * (1 - p)**(n - k)
        toplam += terim
    return toplam
print(round(juri(5, 0.6), 4))

# Beklenen çıktı:
# 0.6826
