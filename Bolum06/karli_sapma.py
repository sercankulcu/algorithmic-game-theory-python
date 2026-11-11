"""Bölüm 6 · Kod İzleme: karli_sapma

GSP açık artırmasında bir reklamveren için aday teklifleri sırayla dener ve
faydasını artıran ilk sapmayı (yoksa None) döndürür. karli_sapma, "Kod İzleme:
karli_sapma" slaytındaki kodun aynısıdır. Kullandığı gsp_fayda yardımcısı
slaytta yoktur; ders notundaki tanıma göre eklenmiştir.
"""


def gsp_fayda(i, b, v, ctr):
  # Slaytta yok: teklifler sıralanır; i, j. yuvadaysa
  # ctr[j] * (v[i] - bir alttaki teklif), yuva dışındaysa 0
  sira = sorted(range(len(b)), key=lambda k: -b[k])
  j = sira.index(i)
  if j >= len(ctr):
    return 0
  alt = b[sira[j + 1]] if j + 1 < len(sira) else 0
  return ctr[j] * (v[i] - alt)


def karli_sapma(i, b, v, ctr, adaylar):
  eski = gsp_fayda(i, b, v, ctr)
  for x in adaylar:
    b2 = b[:]; b2[i] = x   # yalnız i değişir
    u = gsp_fayda(i, b2, v, ctr)
    if u > eski:
      return x, u   # kârlı sapma
  return None     # sapma yok


if __name__ == "__main__":
  # Ders notundaki örnek: A (i = 0) için iki profil
  v = [10, 8, 5, 2]
  ctr = [300, 200, 100]
  adaylar = [9, 6, 4, 3, 1]
  print(karli_sapma(0, [10, 8, 5, 2], v, ctr, adaylar))    # dürüst profil
  print(karli_sapma(0, [10, 5, 3.5, 2], v, ctr, adaylar))  # denge profili

# Beklenen çıktı:
# (6, 1000)
# None
