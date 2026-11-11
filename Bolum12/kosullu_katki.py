"""Bölüm 12 · Kod İzleme: kosullu_katki()

Kamu malı oyununda bir beleşçi (O1) ve üç koşullu işbirlikçiyle (diğerlerinin
önceki turdaki ortalaması kadar katan) katkıların tur tur erimesini izler.
Slayttaki kodun aynısıdır; örnek ders notundaki kosullu_katki([0, 10, 10, 10], 5)
çağrısıdır. Kazanç u = 10 − k + 0,4·Σk ana blokta hesaplanır (slaytta yok).
"""

def kosullu_katki(c, tur):
  gecmis = [c]
  for t in range(tur):
    yeni = [0]                  # O1 hep beleşçi
    for i in range(1, len(c)):
      digerleri = sum(c) - c[i]
      yeni.append(digerleri / (len(c) - 1))
    c = yeni
    gecmis.append(c)
  return gecmis


if __name__ == "__main__":
  for t, c in enumerate(kosullu_katki([0, 10, 10, 10], 5)):
    u = [10 - k + 0.4 * sum(c) for k in c]
    print(t, [round(k, 1) for k in c], round(u[0], 1), round(u[1], 1))

# Beklenen çıktı:
# 0 [0, 10, 10, 10] 22.0 12.0
# 1 [0, 6.7, 6.7, 6.7] 18.0 11.3
# 2 [0, 4.4, 4.4, 4.4] 15.3 10.9
# 3 [0, 3.0, 3.0, 3.0] 13.6 10.6
# 4 [0, 2.0, 2.0, 2.0] 12.4 10.4
# 5 [0, 1.3, 1.3, 1.3] 11.6 10.3
