"""Bölüm 2 · Kod İzleme: Minimaks

Sözlükle verilen iki katlı küçük bir oyun ağacında (A → B, C, D) minimaks değerini
özyinelemeyle hesaplar. Minimaks ve Budama destesindeki kodun aynısıdır.
"""

from math import inf
T = {"A": ["B", "C", "D"], "B": [3, 5],
     "C": [2, 9], "D": [6, 4]}
def minimaks(n, maks):
  if isinstance(n, int):        # yaprak
    return n
  deger = -inf if maks else inf
  for c in T[n]:
    v = minimaks(c, not maks)
    if maks:
      deger = max(deger, v)
    else:
      deger = min(deger, v)
  return deger
print(minimaks("A", True))


# Beklenen çıktı:
# 4
