"""Bölüm 11 · Kod İzleme: kes_noktasi()

Kes ve seç (cut-and-choose) bölüşümünde Ayşe'nin kesim noktasını, Robertson–Webb
değer sorgularıyla ikiye bölme (bisection) yaparak bulur. Slayttaki kodun
aynısıdır.
"""

def v_ayse(x):          # [0, x] parçasının değeri
  if x <= 0.5: return x / 2
  return 0.25 + 1.5 * (x - 0.5)
def kes_noktasi(v, hedef, adim):
  lo, hi = 0.0, 1.0
  for _ in range(adim):
    orta = (lo + hi) / 2
    if v(orta) < hedef: lo = orta
    else: hi = orta
  return (lo + hi) / 2
print(round(kes_noktasi(v_ayse, 0.5, 8), 3))

# Beklenen çıktı:
# 0.666
