"""Bölüm 14 · Kod İzleme: gelir()

İki tipli (L değer 1, H değer 3) tek alıcıya otomatik mekanizma tasarımı:
L'ye satış olasılığı xL için IR ve IC kısıtları sıkıyken satıcının beklenen
gelirini hesaplar. Slayttaki kodun aynısıdır.
"""

def gelir(xL, qL, vL=1, vH=3):
    pL = xL * vL                 # L'nin IR kısıtı sıkı
    pH = pL + vH * (1 - xL)      # H'nin IC kısıtı sıkı
    return qL * pL + (1 - qL) * pH
for qL in [0.5, 0.75]:
    G = [gelir(x, qL) for x in [0, 0.5, 1]]
    print(qL, G)

# Beklenen çıktı:
# 0.5 [1.5, 1.25, 1.0]
# 0.75 [0.75, 0.875, 1.0]
