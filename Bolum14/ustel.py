"""Bölüm 14 · Kod İzleme: ustel()

Diferansiyel mahremiyette üstel mekanizma: her aday fiyat, deneysel gelir
puanıyla orantılı exp(ε·R/2) ağırlıkla seçilir; bir alıcı çıkarılınca
olasılıkların ne kadar değiştiğini gösterir. Slayttaki kodun aynısıdır.
"""

import math
def ustel(v, fiyatlar, eps):
    R = [p * sum(x >= p for x in v) for p in fiyatlar]
    w = [math.exp(eps * r / 2) for r in R]   # Δ = 1
    W = sum(w)
    return [x / W for x in w]
v = [0.62, 0.15, 0.91, 0.47, 0.33, 0.78, 0.55, 0.08]
P = [0.2, 0.4, 0.6, 0.8]
q = ustel(v, P, 2)
print([round(x, 3) for x in q])
q = ustel(v[1:], P, 2)          # 0.62 çıkarıldı
print([round(x, 3) for x in q])

# Beklenen çıktı:
# [0.175, 0.389, 0.319, 0.117]
# [0.206, 0.375, 0.251, 0.168]
