"""Bölüm 2 · Laboratuvardaki Arama

Laboratuvardaki derinlik sınırlı alfa-beta araması ve kökte en iyi hamleyi seçen
en_iyi_hamle. İki fonksiyon slayttaki kodun aynısıdır (slaytta Dörtlü Bağla için).
Çalıştırabilmek için küçük bir XOX (tic-tac-toe) durum sınıfı (bitti, fayda,
hamleler, oyna), basit bir E değerlendirmesi ve sirala eklenmiştir; bu düzenek
slaytta yoktur. fayda slayttaki gibi ±(1000 − k) ya da 0'dır (k: oynanmış hamle).
"""

from math import inf   # slaytta görünmez; inf için gerekli

def alfabeta(s, d, a, b, maks):
  if s.bitti():                # oyun sonu
    return s.fayda()           # ±(1000 − k) ya da 0
  if d == 0:
    return E(s)                # değerlendirme
  deger = -inf if maks else inf
  for m in sirala(s.hamleler()):
    v = alfabeta(s.oyna(m), d-1, a, b, not maks)
    if maks:
      deger = max(deger, v); a = max(a, deger)
    else:
      deger = min(deger, v); b = min(b, deger)
    if a >= b:
      break
  return deger


def en_iyi_hamle(s, d):     # kök: MAX
  a, en = -inf, None
  for m in sirala(s.hamleler()):
    v = alfabeta(s.oyna(m), d-1,
                 a, inf, False)
    if v > a:
      a, en = v, m
  return en


# ---------------------------------------------------------------------------
# Aşağısı slaytta yoktur: iki fonksiyonu küçük gerçek bir oyunda (XOX) çalıştırmak
# için eklenen en küçük düzenektir.
# ---------------------------------------------------------------------------

CIZGILER = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
            (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


class XOX:
    """Tahta 9 karakterlik bir dizgidir: 'X', 'O' ya da '.' (boş); kareler 0..8."""

    def __init__(self, tahta="........."):
        self.tahta = tahta

    def sira(self):
        return "X" if self.tahta.count("X") == self.tahta.count("O") else "O"

    def kazanan(self):
        for a, b, c in CIZGILER:
            if self.tahta[a] != "." and self.tahta[a] == self.tahta[b] == self.tahta[c]:
                return self.tahta[a]
        return None

    def bitti(self):
        return self.kazanan() is not None or "." not in self.tahta

    def fayda(self):
        k = 9 - self.tahta.count(".")   # oynanmış hamle sayısı
        w = self.kazanan()
        if w == "X":
            return 1000 - k
        if w == "O":
            return -(1000 - k)
        return 0

    def hamleler(self):
        return [i for i in range(9) if self.tahta[i] == "."]

    def oyna(self, m):
        t = self.tahta
        return XOX(t[:m] + self.sira() + t[m + 1:])


def E(s):
    # X'in hâlâ tamamlayabileceği çizgiler − O'nun tamamlayabileceği çizgiler
    x = sum(1 for c in CIZGILER if all(s.tahta[i] != "O" for i in c))
    o = sum(1 for c in CIZGILER if all(s.tahta[i] != "X" for i in c))
    return x - o


ONCELIK = [4, 0, 2, 6, 8, 1, 3, 5, 7]   # önce merkez, sonra köşeler, sonra kenarlar


def sirala(hamleler):
    return sorted(hamleler, key=ONCELIK.index)


if __name__ == "__main__":
    # Kökte sıra hep X'tedir (MAX); fayda X'in bakış açısındandır.
    for tahta, d in [(".........", 9), (".........", 2),
                     ("XX.OO....", 9), ("X...O...X", 9)]:
        s = XOX(tahta)
        if s.sira() == "O":          # kökte sıra X'te olsun diye O köşeye oynar
            s = s.oyna(2)
        print(s.tahta, "d =", d, "-> hamle", en_iyi_hamle(s, d),
              "değer", alfabeta(s, d, -inf, inf, True))


# Beklenen çıktı:
# ......... d = 9 -> hamle 4 değer 0
# ......... d = 2 -> hamle 4 değer 1
# XX.OO.... d = 9 -> hamle 2 değer 995
# X.O.O...X d = 9 -> hamle 6 değer 993
