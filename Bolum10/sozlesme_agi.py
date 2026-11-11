"""Bölüm 10 · Kod İzleme: sozlesme_agi()

Sözleşme ağı (contract net) protokolüyle görevleri sırayla ihaleye çıkarır;
her görevi boştaki robotlardan en düşük teklifi verene atar. Slayttaki kodun
aynısıdır; alttaki örnek, ders notundaki 3 robot / 3 görev maliyet tablosudur.
"""


def sozlesme_agi(gorevler, maliyet):
  bos = set(maliyet)
  atama, toplam = {}, 0
  for g in gorevler:
    teklif = {r: maliyet[r][g] for r in bos}
    kazanan = min(teklif, key=teklif.get)
    atama[g] = kazanan
    toplam += teklif[kazanan]
    bos.remove(kazanan)
  return atama, toplam


if __name__ == "__main__":
  maliyet = {
    "R1": {"G1": 2, "G2": 3, "G3": 5},
    "R2": {"G1": 3, "G2": 7, "G3": 4},
    "R3": {"G1": 6, "G2": 8, "G3": 9},
  }
  atama, toplam = sozlesme_agi(["G1", "G2", "G3"], maliyet)
  print(atama, toplam)

# Beklenen çıktı:
# {'G1': 'R1', 'G2': 'R2', 'G3': 'R3'} 18
