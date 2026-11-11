"""Bölüm 8 · Kod İzleme: denge_bul

İki paralel yollu bir ağda Wardrop dengesini ikiye bölme (bisection) yöntemiyle
arar: Yol 1'deki araç sayısını, iki yolun gecikmesi eşitlenene kadar daraltır.
Fonksiyon, "Kod İzleme: denge_bul" slaytındaki kodun aynısıdır.
"""


def denge_bul(l1, l2, r, eps=50):
  lo, hi = 0, r
  while hi - lo > eps:
    x = (lo + hi) / 2
    if l1(x) < l2(r - x):
      lo = x      # Yol 1 hâlâ hızlı: artır
    else:
      hi = x      # Yol 1 yavaş: azalt
  return (lo + hi) / 2


if __name__ == "__main__":
  # Ders notundaki örnek: 3.000 araç, l1 = 5 + x/100, l2 = 20 + x/200
  yol1 = lambda x: 5 + x / 100
  yol2 = lambda x: 20 + x / 200
  print(round(denge_bul(yol1, yol2, 3000), 2))
  # Örnek 8.7: 6.000 araç, l1 = 10 + x/200, l2 = 25 + x/100
  yol1 = lambda x: 10 + x / 200
  yol2 = lambda x: 25 + x / 100
  print(round(denge_bul(yol1, yol2, 6000), 2))

# Beklenen çıktı:
# 1992.19
# 4992.19
