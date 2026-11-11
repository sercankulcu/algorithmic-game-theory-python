"""Bölüm 2 · Yinelemeli Eleme Adım Adım

Ortalamanın 2/3'ünü Tahmin Et oyununda baskın stratejilerin yinelemeli elenmesini
izler: her turda anlamlı en büyük tahmin 2/3 ile çarpılır. Slayttaki kodun aynısıdır.
"""

ust = 90                # olası en büyük tahmin
for tur in range(1, 7):
    # ortalama ≤ ust  ⇒  hedef ≤ (2/3)·ust
    ust = ust * 2 / 3
    print(tur, round(ust, 1))
# ust = 90·(2/3)^k → 0 : tek denge herkes 0


# Beklenen çıktı:
# 1 60.0
# 2 40.0
# 3 26.7
# 4 17.8
# 5 11.9
# 6 7.9
