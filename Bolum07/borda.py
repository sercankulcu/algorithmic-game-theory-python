"""Bölüm 7 · Kod İzleme: borda()

Seçmen gruplarının sıralamalarından Borda puanlarını toplar ve en yüksek
puanlı adayı döndürür. Fonksiyon, "Kod İzleme: borda()" slaytındaki kodun
aynısıdır.
"""


def borda(oylar):
  puan = {}
  for adet, sira in oylar:
    m = len(sira)
    for k, aday in enumerate(sira):
      p = adet * (m - 1 - k)
      puan[aday] = puan.get(aday, 0) + p
  kazanan = max(puan, key=puan.get)
  return kazanan, puan


if __name__ == "__main__":
  # Ders notundaki ana profil: 13 seçmen, 4 aday
  oylar = [(4, "ADBC"), (4, "CBDA"), (3, "DBCA"), (2, "ABCD")]
  print(borda(oylar))

# Beklenen çıktı:
# ('B', {'A': 18, 'D': 21, 'B': 22, 'C': 17})
