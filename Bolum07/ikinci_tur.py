"""Bölüm 7 · Kod İzleme: ikinci_tur()

Anında ikinci tur (IRV) sayımını yapar: çoğunluğu alan aday çıkana kadar her
turda en az oylu adayı eler ve oyları aktarır. Fonksiyon, "Kod İzleme:
ikinci_tur()" slaytındaki kodun aynısıdır.
"""


def ikinci_tur(oylar, adaylar):
  kalan = set(adaylar)
  while True:
    say = {a: 0 for a in kalan}
    for adet, sira in oylar:
      ilk = next(a for a in sira if a in kalan)
      say[ilk] += adet
    lider = max(say, key=say.get)
    if 2 * say[lider] > sum(say.values()):
      return lider
    kaybeden = min(say, key=say.get)
    kalan.remove(kaybeden)


if __name__ == "__main__":
  # Ders notundaki ana profil: 13 seçmen, 4 aday
  oylar = [(4, "ADBC"), (4, "CBDA"), (3, "DBCA"), (2, "ABCD")]
  print(ikinci_tur(oylar, ["A", "B", "C", "D"]))

# Beklenen çıktı:
# C
