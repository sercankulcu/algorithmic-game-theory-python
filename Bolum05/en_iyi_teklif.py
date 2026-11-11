"""Bölüm 5 · Kırpma Kod İzleme

Birinci fiyat açık artırmasında, rakipler değerlerinin (n - 1)/n katını teklif
ederken beklenen faydayı en büyük yapan teklifi bir ızgarada kaba kuvvetle arar.
Fonksiyon, "Kırpma Kod İzleme" slaytındaki kodun aynısıdır.
"""


def en_iyi_teklif(v, n, adim=0.1):
  beta = (n - 1) / n        # rakipler beta*v
  en, b_en = -1, 0
  b = 0.0
  while b <= v:
    p = min(1, b / beta) ** (n - 1)  # P(kazan)
    eu = (v - b) * p
    if eu > en:
      en, b_en = eu, b
    b = round(b + adim, 10)
  return b_en, en


if __name__ == "__main__":
  # Ders notundaki örnek: değer v = 0,8, iki teklifçi
  teklif, fayda = en_iyi_teklif(0.8, 2)
  print(teklif, round(fayda, 3))

# Beklenen çıktı:
# 0.4 0.32
