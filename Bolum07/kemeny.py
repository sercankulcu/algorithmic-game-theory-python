"""Bölüm 7 · Kod İzleme: kemeny()

Adayların bütün sıralamalarını dener ve seçmenlerle uyum skoru en büyük olan
Kemeny sıralamasını döndürür. Kod, "Kod İzleme: kemeny()" slaytındaki kodun
aynısıdır.
"""

from itertools import permutations
def kemeny(oylar, adaylar):
  en_iyi, en_skor = None, -1
  for sira in permutations(adaylar):
    skor = 0
    for i, x in enumerate(sira):
      for y in sira[i + 1:]:
        skor += sum(n for n, oy in oylar
                    if oy.index(x) < oy.index(y))
    if skor > en_skor:
      en_iyi, en_skor = sira, skor
  return en_iyi, en_skor


if __name__ == "__main__":
  # Ders notundaki döngü profili: 9 seçmen, 3 aday
  dongu = [(4, "ABC"), (3, "BCA"), (2, "CAB")]
  print(kemeny(dongu, "ABC"))
  # Ana profil: 13 seçmen, 4 aday
  oylar = [(4, "ADBC"), (4, "CBDA"), (3, "DBCA"), (2, "ABCD")]
  print(kemeny(oylar, "ABCD"))

# Beklenen çıktı:
# (('A', 'B', 'C'), 17)
# (('D', 'B', 'C', 'A'), 44)
