"""Bölüm 12 · Kod İzleme: beklenti()

Beklenti kuramının değer fonksiyonuyla (α = 0,88, λ = 2,25) yarı yarıya
+G / −100 bahislerinin değerini hesaplar ve bahsin ne zaman kabul edileceğini
gösterir. Slayttaki kodun aynısıdır.
"""

def v(x):
    if x >= 0: return x ** 0.88
    return -2.25 * (-x) ** 0.88
def beklenti(G, K):      # ½: +G, ½: −K
    return 0.5 * v(G) + 0.5 * v(-K)
for G in [100, 200, 251, 300]:
    print(G, round(beklenti(G, 100), 1))

# Beklenen çıktı:
# 100 -36.0
# 200 -11.8
# 251 -0.1
# 300 10.9
