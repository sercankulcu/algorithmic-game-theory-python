"""Bölüm 0 · İzleme: Piyangonun Beklenen Değeri

Üç sonuçlu bir piyangonun beklenen ödülünü Σ ödül · olasılık toplamıyla hesaplar
ve 12 TL'lik bilet fiyatını düşerek net beklenen kazancı yazar. Slayttaki kodun aynısıdır.
"""

odul = [100, 20, 0]          # TL
olas = [0.05, 0.25, 0.70]
E = 0
for i in range(3):
    E = E + odul[i] * olas[i]
print("E =", E)
print("net =", E - 12)  # bilet 12 TL


# Beklenen çıktı:
# E = 10.0
# net = -2.0
