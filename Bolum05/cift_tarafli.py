"""Bölüm 5 · Çift Taraflı Kod İzleme

Çift taraflı açık artırmada alış ve satış emirlerini sıralayıp eşleştirir,
işlem sayısını ve orta nokta kuralıyla bulunan fiyatı döndürür. Fonksiyon,
"Çift Taraflı Kod İzleme" slaytındaki kodun aynısıdır.
"""


def cift_tarafli(alis, satis):
  b = sorted(alis, reverse=True)  # alıcı
  s = sorted(satis)               # satıcı
  k, n = 0, min(len(b), len(s))
  while k < n and b[k] >= s[k]:
    k += 1                   # çift eşleşti
  if k == 0:
    return 0, None
  lo = max([s[k-1]] + b[k:k+1])
  hi = min([b[k-1]] + s[k:k+1])
  return k, (lo + hi) / 2


if __name__ == "__main__":
  # Ders notundaki örnek: beş alıcı, beş satıcı
  alis = [70, 40, 90, 55, 80]
  satis = [60, 85, 35, 75, 50]
  print(cift_tarafli(alis, satis))

# Beklenen çıktı:
# (3, 65.0)
