"""Bölüm 2 · Kod İzleme: Alfa-Beta

Aynı küçük ağaçta alfa-beta budamalı minimaks araması yapar; C'nin ikinci yaprağı
budanır, sonuç minimaksla aynıdır. Minimaks ve Budama destesindeki kodun aynısıdır.
"""

from math import inf
T = {"A": ["B", "C", "D"], "B": [3, 5],
     "C": [2, 9], "D": [6, 4]}
def alfabeta(n, a, b, maks):
  if isinstance(n, int):        # yaprak
    return n
  deger = -inf if maks else inf
  for c in T[n]:
    v = alfabeta(c, a, b, not maks)
    if maks:
      deger = max(deger, v); a = max(a, deger)
    else:
      deger = min(deger, v); b = min(b, deger)
    if a >= b:
      break                  # budama
  return deger
print(alfabeta("A", -inf, inf, True))


# Beklenen çıktı:
# 4
