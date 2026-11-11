"""Bölüm 2 · Kod İzleme: Seviye-k Tahmini

Ortalamanın 2/3'ünü Tahmin Et oyununda seviye-k oyuncuların tahminlerini hesaplar,
seviye 0-1-2 karışımı bir nüfus için hedefi bulur ve her seviyenin hedefe uzaklığını
yazar. Slayttaki kodun aynısıdır.
"""

def tahmin(k, L0=45):     # seviye-k
    g = L0
    for _ in range(k):
        g = g * 2 / 3
    return g
pay = {0: 0.3, 1: 0.4, 2: 0.3}   # inanç
ort = sum(p * tahmin(k) for k, p in pay.items())
hedef = ort * 2 / 3
for k in range(5):
    print(k, round(tahmin(k), 1),
          round(abs(tahmin(k) - hedef), 1))


# Beklenen çıktı:
# 0 45 24.0
# 1 30.0 9.0
# 2 20.0 1.0
# 3 13.3 7.7
# 4 8.9 12.1
