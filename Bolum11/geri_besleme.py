"""Bölüm 11 · Kod İzleme: Geri Besleme

Kendini doğrulayan veri: devriye her gün kaydı fazla olan bölgeye gider ve
yalnız orada olay kaydedilir; gerçek olay sayıları eşitken bölge 0'ın kayıt
payı her gün büyür. Slayttaki kodun aynısıdır.
"""

kayit = [6, 5]     # geçmiş kayıtlar (bölge 0, 1)
gercek = [3, 3]    # gerçek günlük olay: eşit!
for gun in range(1, 5):
  hedef = 0 if kayit[0] >= kayit[1] else 1
  kayit[hedef] += gercek[hedef]  # yalnız orada
  pay = kayit[0] / sum(kayit)
  print(gun, hedef, kayit, round(pay, 2))

# Beklenen çıktı:
# 1 0 [9, 5] 0.64
# 2 0 [12, 5] 0.71
# 3 0 [15, 5] 0.75
# 4 0 [18, 5] 0.78
