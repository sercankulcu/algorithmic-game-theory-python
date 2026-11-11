"""Bölüm 3 · Yaklaşık Denge ve Araçlar

İşçi–müdür denetim oyununun Nash dengesini nashpy kütüphanesinin destek sayımı
(support enumeration) ile bulur. Slayttaki kodun aynısıdır.

Gerekli paket: pip install nashpy
"""

import nashpy as nash
A = [[2, 2], [0, 4]]    # işçi: Çalış / Kaytar
B = [[1, 2], [-1, -4]]  # müdür: Denetle / Denetleme
oyun = nash.Game(A, B)
for x, y in oyun.support_enumeration():
    print(x, y)  # [0.75 0.25] [0.5 0.5]


# Beklenen çıktı:
# [0.75 0.25] [0.5 0.5]
