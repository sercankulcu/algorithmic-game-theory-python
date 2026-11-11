"""Bölüm 8 · Kod İzleme: en_iyi_alt_ag

Ağdan tek tek kenar silmeyi dener ve Wardrop dengesindeki yolculuk süresini
en çok kısaltan kenarı (Braess paradoksu) bulur. en_iyi_alt_ag, "Kod İzleme:
en_iyi_alt_ag" slaytındaki kodun aynısıdır. Kullandığı denge_suresi yardımcısı
slaytta yoktur; burada en kısa yollar arasında akış kaydırarak (Beckmann
potansiyelini en aza indiren) basit bir yöntemle eklenmiştir.
"""


def denge_suresi(ag, r):
  # Slaytta yok. Kenar: (u, v, a, b), gecikme b + a * x.
  # s'den t'ye bütün yolları bul; akışı, kullanılan en yavaş yoldan
  # en hızlı yola, iki yolun süresi eşitlenecek kadar kaydır.
  yollar = []
  def ara(u, yol, gorulen):
    if u == "t":
      yollar.append(yol)
      return
    for k in ag:
      if k[0] == u and k[1] not in gorulen:
        ara(k[1], yol + [k], gorulen | {k[1]})
  ara("s", [], {"s"})
  if not yollar:
    return float("inf")   # yol yoksa inf
  akis = [r] + [0] * (len(yollar) - 1)
  def sureler():
    yuk = {k: 0 for k in ag}
    for f, yol in zip(akis, yollar):
      for k in yol:
        yuk[k] += f
    return [sum(k[3] + k[2] * yuk[k] for k in yol) for yol in yollar]
  for _ in range(1000):
    c = sureler()
    kullanilan = [i for i in range(len(yollar)) if akis[i] > 1e-9]
    yavas = max(kullanilan, key=lambda i: c[i])
    hizli = min(range(len(yollar)), key=lambda i: c[i])
    if c[yavas] - c[hizli] < 1e-9:
      break
    fark = [k for k in yollar[yavas] if k not in yollar[hizli]] + \
           [k for k in yollar[hizli] if k not in yollar[yavas]]
    egim = sum(k[2] for k in fark)
    d = akis[yavas] if egim == 0 else min(akis[yavas], (c[yavas] - c[hizli]) / egim)
    akis[yavas] -= d
    akis[hizli] += d
  c = sureler()
  return max(c[i] for i in range(len(yollar)) if akis[i] > 1e-9)


def en_iyi_alt_ag(ag, r):
  eniyi, sil = denge_suresi(ag, r), None
  for e in ag:
    alt = [k for k in ag if k != e]
    d = denge_suresi(alt, r)   # yol yoksa inf
    if d < eniyi:
      eniyi, sil = d, e
  return sil, eniyi


if __name__ == "__main__":
  # Ders notundaki Braess ağı, 4.000 araç: (başlangıç, bitiş, a, b)
  braess = [("s", "A", 1 / 100, 0),   # x/100
            ("A", "t", 0, 45),        # 45
            ("s", "B", 0, 45),        # 45
            ("B", "t", 1 / 100, 0),   # x/100
            ("A", "B", 0, 0)]         # kestirme, 0
  print("başlangıç:", round(denge_suresi(braess, 4000), 2))
  for e in braess:
    alt = [k for k in braess if k != e]
    print(e[0] + "→" + e[1], "silinince:", round(denge_suresi(alt, 4000), 2))
  sil, eniyi = en_iyi_alt_ag(braess, 4000)
  print("sil:", sil[0] + "→" + sil[1], "süre:", round(eniyi, 2))

# Beklenen çıktı:
# başlangıç: 80.0
# s→A silinince: 85.0
# A→t silinince: 80.0
# s→B silinince: 80.0
# B→t silinince: 85.0
# A→B silinince: 65.0
# sil: A→B süre: 65.0
