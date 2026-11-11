"""Bölüm 1 · Kod İzleme: bayes()

Bir hastalık testinin ardışık sonuçlarıyla ön olasılığı Bayes kuralına göre adım
adım günceller ve her adımdaki son olasılığı yazar. Fonksiyon slayttaki kodun
aynısıdır; örnek çağrı ders notundaki izlemedir.
"""

def bayes(p, duyarlilik, yp, testler):
  for sonuc in testler:
    if sonuc == "+":
      pay = duyarlilik * p
      payda = pay + yp * (1 - p)
    else:
      pay = (1 - duyarlilik) * p
      payda = pay + (1 - yp) * (1 - p)
    p = pay / payda
    print(sonuc, round(p, 4))
  return p


if __name__ == "__main__":
    son = bayes(0.01, 0.9, 0.09, ["+", "+", "-"])
    print("son olasılık:", round(son, 4))


# Beklenen çıktı:
# + 0.0917
# + 0.5025
# - 0.0999
# son olasılık: 0.0999
