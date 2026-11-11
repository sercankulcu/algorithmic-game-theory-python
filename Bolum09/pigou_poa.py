"""Bölüm 9 · Kod İzleme: pigou_poa(p)

Üst yolu x**p, alt yolu 1 gecikmeli Pigou ağında Anarşinin Bedelini (denge
maliyeti / optimum maliyet) hesaplar ve p = 1, 2, 4, 8, 16 için yazar. Kod,
"Kod İzleme: pigou_poa(p)" slaytındaki kodun aynısıdır.
"""

def pigou_poa(p):          # üst yol x**p, alt yol 1
  x = (p + 1) ** (-1 / p)  # C'(x) = 0 noktası
  opt = x ** (p + 1) + (1 - x)
  return 1 / opt           # denge maliyeti 1

for p in [1, 2, 4, 8, 16]:
  print(p, round(pigou_poa(p), 3))

# Beklenen çıktı:
# 1 1.333
# 2 1.626
# 4 2.151
# 8 3.081
# 16 4.727
