"""Bölüm 11 · Kod İzleme: b_grubu(q)

B grubunda 0,2 puanlı başvuranları q olasılıkla onaylayarak fırsat eşitliğini
rastgeleleştirmeyle sağlamayı dener; her q için TPR, FPR ve doğruluğu yazdırır.
Slayttaki kodun aynısıdır.
"""

def b_grubu(q):   # 0,2 puanlıyı q ile onayla
  TP = 16 + 16 * q
  FP = 4 + 64 * q
  tpr = TP / 32
  fpr = FP / 68
  dogru = TP + (68 - FP)   # TP + TN
  return tpr, fpr, round(dogru / 100, 3)

for q in [0, 0.2, 0.4, 0.6]:
  tpr, fpr, d = b_grubu(q)
  print(q, round(tpr, 2), round(fpr, 2), d)

# Beklenen çıktı:
# 0 0.5 0.06 0.8
# 0.2 0.6 0.25 0.704
# 0.4 0.7 0.44 0.608
# 0.6 0.8 0.62 0.512
