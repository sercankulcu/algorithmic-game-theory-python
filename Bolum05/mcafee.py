"""Bölüm 5 · McAfee Kod İzleme

Çift taraflı açık artırmada McAfee kuralını uygular: dışarıda kalan ilk çiftin
ortalaması uygunsa bütün işlemler tek fiyattan yapılır, değilse son çift çıkarılır
ve iki ayrı fiyat kullanılır. Fonksiyon, "McAfee Kod İzleme" slaytındaki kodun
aynısıdır.
"""


def mcafee(alis, satis):
  b = sorted(alis, reverse=True) + [0]
  s = sorted(satis) + [float('inf')]
  k = 0
  while b[k] >= s[k]:
    k += 1                 # verimli işlem
  if k == 0: return 0, None, None
  p0 = (b[k] + s[k]) / 2   # dışarıdaki çift
  if s[k-1] <= p0 <= b[k-1]:
    return k, p0, p0       # tek fiyat
  return k - 1, b[k-1], s[k-1]  # iki fiyat


if __name__ == "__main__":
  # Ders notundaki iki örnek: önce tek fiyat, sonra iki fiyat durumu
  print(mcafee([70, 40, 90, 55, 80], [60, 85, 35, 75, 50]))
  print(mcafee([90, 80, 70, 40], [30, 50, 65, 85]))

# Beklenen çıktı:
# (3, 65.0, 65.0)
# (2, 70, 65)
