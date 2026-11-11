"""Bölüm 6 · GSP/VCG Kod İzleme

Sponsorlu arama açık artırmasında aynı teklifler için her yuvanın toplam GSP
ve VCG ödemelerini hesaplar. Fonksiyon, "GSP/VCG Kod İzleme" slaytındaki kodun
aynısıdır.
"""


def gsp_vcg(bids, ctr):
  m = len(ctr)
  b = sorted(bids, reverse=True) + [0]*m
  a = ctr + [0]     # sanal yuva: 0 tık
  gsp, vcg = [0]*m, [0]*(m + 1)
  for j in range(m):
    gsp[j] = a[j] * b[j+1]   # alttaki
  for j in range(m-1, -1, -1):  # alttan
    ek = (a[j] - a[j+1]) * b[j+1]
    vcg[j] = vcg[j+1] + ek
  return gsp, vcg[:m]


if __name__ == "__main__":
  # Ders notundaki örnek: dört reklamveren, üç yuva
  gsp, vcg = gsp_vcg([10, 8, 5, 2], [300, 200, 100])
  print("GSP:", gsp, "toplam", sum(gsp))
  print("VCG:", vcg, "toplam", sum(vcg))
  # Tek yuvalı çağrı: iki kural çakışır
  print(gsp_vcg([10, 8, 5], [100]))

# Beklenen çıktı:
# GSP: [2400, 1000, 200] toplam 3600
# VCG: [1500, 700, 200] toplam 2400
# ([800], [800])
