"""Bölüm 14 · Veriden Fiyat Öğrenme

Geçmişte gözlenen alıcı değerlerinden deneysel geliri en büyük yapan rezerv
fiyatını seçer (aday fiyatlar örnek değerlerin kendisidir). Slayttaki kodun
aynısıdır; örnek ders notundaki 8 alıcı değeridir.
"""

def en_iyi_fiyat(orn):
  v = sorted(orn, reverse=True)
  n = len(v)
  fiyat, gelir = 0, 0
  for k in range(1, n + 1):
    p = v[k - 1]        # k. en yüksek
    g = p * k / n       # k alıcı alır
    if g > gelir:
      fiyat, gelir = p, g
  return fiyat, gelir


if __name__ == "__main__":
  orn = [0.62, 0.15, 0.91, 0.47, 0.33, 0.78, 0.55, 0.08]
  fiyat, gelir = en_iyi_fiyat(orn)
  print(fiyat, round(gelir, 3))

# Beklenen çıktı:
# 0.47 0.294
