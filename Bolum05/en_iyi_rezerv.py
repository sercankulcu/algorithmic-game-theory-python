"""Bölüm 5 · Rezerv Kod İzleme

İki teklifçili, değerleri U[0, 1] olan ikinci fiyat açık artırmasında rezerv
fiyatın beklenen gelirini bir ızgarada hesaplar (gelir) ve r = 0; 0,1; ...; 1
arasından en iyi rezervi seçer (en_iyi_rezerv). İki fonksiyon da "Rezerv Kod
İzleme" slaytındaki kodun aynısıdır.
"""


def gelir(r, m=100):      # 2 teklifçi, U[0,1]
  v = [(i + .5) / m for i in range(m)]
  top = sum(max(min(a, c), r) for a in v
            for c in v if max(a, c) >= r)
  return top / m**2       # ortalama ödeme
def en_iyi_rezerv(adim=0.1):
  en, r_en = -1, None
  for k in range(round(1/adim) + 1):
    R = gelir(k * adim)
    if R > en: en, r_en = R, k * adim
  return r_en, en


if __name__ == "__main__":
  # Ders notundaki tablo: her rezerv için gelir, sonra en iyi rezerv
  for k in range(11):
    print(round(k * 0.1, 1), round(gelir(k * 0.1), 3))
  rezerv, en_gelir = en_iyi_rezerv()
  print("en iyi:", rezerv, round(en_gelir, 3))

# Beklenen çıktı:
# 0.0 0.333
# 0.1 0.342
# 0.2 0.363
# 0.3 0.387
# 0.4 0.408
# 0.5 0.417
# 0.6 0.405
# 0.7 0.366
# 0.8 0.291
# 0.9 0.171
# 1.0 0.0
# en iyi: 0.5 0.417
