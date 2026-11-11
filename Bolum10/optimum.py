"""Bölüm 10 · Kod İzleme: optimum()

Tüm maliyetleri bilen merkezin, robotların bütün sıralamalarını deneyerek en
ucuz atamayı bulmasıdır. Slayttaki kodun aynısıdır; slaytta görünmeyen
`from itertools import permutations` satırı eklenmiştir.
"""
from itertools import permutations   # slaytta yok; kodun çalışması için eklendi


def optimum(gorevler, maliyet):
  en_iyi = None
  for p in permutations(maliyet):
    t = sum(maliyet[r][g]
            for g, r in zip(gorevler, p))
    if en_iyi is None or t < en_iyi[0]:
      en_iyi = (t, p)
  return en_iyi


if __name__ == "__main__":
  maliyet = {
    "R1": {"G1": 2, "G2": 3, "G3": 5},
    "R2": {"G1": 3, "G2": 7, "G3": 4},
    "R3": {"G1": 6, "G2": 8, "G3": 9},
  }
  print(optimum(["G1", "G2", "G3"], maliyet))

# Beklenen çıktı:
# (13, ('R3', 'R1', 'R2'))
