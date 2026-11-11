"""Bölüm 9 · Kod İzleme: poa_pos

Yük dengeleme oyununda bütün atamaları tarar; en kötü ve en iyi saf Nash
dengesinin optimuma oranını, yani Anarşinin Bedelini (PoA) ve İstikrarın
Bedelini (PoS) döndürür. poa_pos ve son iki satır, "Kod İzleme: poa_pos"
slaytındaki kodun aynısıdır. Kullandığı nash_mi bu slaytta yoktur; bir önceki
slayttan ("Kod İzleme: nash_mi") olduğu gibi alınmıştır.
"""

def nash_mi(boy, atama, m):
  # Bu slaytta yok: "Kod İzleme: nash_mi" slaytından alındı
  yuk = [0] * m
  for j, k in enumerate(atama):
    yuk[k] += boy[j]
  for j, k in enumerate(atama):
    for h in range(m):
      if yuk[h] + boy[j] < yuk[k]:
        return False      # j kaçar
  return True             # kimse kaçmaz


from itertools import product
def poa_pos(boy, m):
  opt, dengeler = float("inf"), []
  for atama in product(range(m), repeat=len(boy)):
    yuk = [0] * m
    for j, k in enumerate(atama):
      yuk[k] += boy[j]
    opt = min(opt, max(yuk))
    if nash_mi(boy, atama, m):       # denge testi
      dengeler.append(max(yuk))
  return max(dengeler) / opt, min(dengeler) / opt
r = poa_pos([2, 2, 1, 1], 2)
print(round(r[0], 3), r[1])

# Beklenen çıktı:
# 1.333 1.0
