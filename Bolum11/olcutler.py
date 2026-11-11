"""Bölüm 11 · Kod İzleme: olcutler()

Karışıklık matrisinden seçim oranı, TPR, FPR ve PPV'yi hesaplar ve A ile B
gruplarının adalet ölçütlerini yan yana yazdırır. Slayttaki kodun aynısıdır.
"""

def olcutler(TP, FP, FN, TN):
  n = TP + FP + FN + TN
  secim = (TP + FP) / n   # demografik eşitlik
  tpr = TP / (TP + FN)    # eşitlenmiş olasılıklar
  fpr = FP / (FP + TN)
  ppv = TP / (TP + FP)    # tahmin eşitliği
  return secim, tpr, fpr, ppv

A = olcutler(40, 10, 10, 40)
B = olcutler(16, 4, 16, 64)
ADLAR = ["seçim", "TPR", "FPR", "PPV"]
for i, ad in enumerate(ADLAR):
  print(ad, round(A[i], 3), round(B[i], 3))

# Beklenen çıktı:
# seçim 0.5 0.2
# TPR 0.8 0.5
# FPR 0.2 0.059
# PPV 0.8 0.8
