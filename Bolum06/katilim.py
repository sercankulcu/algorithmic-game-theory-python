"""Bölüm 6 · Kod İzleme: katilim

İki taraflı bir platformda fiyatlar sabitken alıcıların ve satıcıların
birbirine sırayla tepki vermesini taklit eder ve birkaç tur sonraki katılımları
(bin kişi) döndürür. Fonksiyon, "Kod İzleme: katilim" slaytındaki kodun aynısıdır.
"""


def katilim(pA, pB, tur=8):
  nA, nB = 0, 0
  for t in range(tur):
    nA = 20 + 0.25 * nB - pA   # alıcılar
    nB = 80 + 0.75 * nA - pB   # satıcılar
  return nA, nB


if __name__ == "__main__":
  # Ders notundaki örnek: optimum fiyatlar pA = -5, pB = 50
  nA, nB = katilim(-5, 50)
  print(round(nA, 1), round(nB, 1))
  print("kâr:", round(-5 * nA + 50 * nB, 1))

# Beklenen çıktı:
# 40.0 60.0
# kâr: 2800.0
