"""Bölüm 2 · Kod İzleme: Minimaks

Üç dallı iki katlı bir oyun ağacında minimaks değerini özyinelemeyle hesaplar.
Oyunlar ve Temsiller destesindeki kodun aynısıdır (Minimaks destesindeki
minimaks.py'den farklı bir ağaç kullanır).
"""

T = {"A": ["B", "C", "D"], "B": [3, 12, 8],
     "C": [2, 4, 6], "D": [14, 5, 2]}
def minimax(n, maxi):
  if isinstance(n, int):         # yaprak
    return n
  best = -99 if maxi else 99
  for c in T[n]:
    v = minimax(c, not maxi)
    best = max(best, v) if maxi else min(best, v)
  return best
print(minimax("A", True))


# Beklenen çıktı:
# 3
