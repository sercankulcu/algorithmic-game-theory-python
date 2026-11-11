"""Bölüm 8 · Kod İzleme: maliyet (BFS)

Tek taraflı ağ oluşturma oyununda bir oyuncunun maliyetini hesaplar: aldığı
bağ sayısının alpha katı artı BFS ile bulunan uzaklıkların toplamı. maliyet,
"Kod İzleme: maliyet (BFS)" slaytındaki kodun aynısıdır. Kullandığı komsu
yardımcısı slaytta yoktur; ders notundaki tanıma göre eklenmiştir.
"""


def komsu(bag, u):
  # Slaytta yok: bağı kim alırsa alsın u'nun komşuları
  return [b if a == u else a for (a, b) in bag if u in (a, b)]


def maliyet(i, bag, alpha):
  uz = {i: 0}; kuyruk = [i]
  while kuyruk:
    u = kuyruk.pop(0)
    for v in komsu(bag, u):
      if v not in uz:
        uz[v] = uz[u] + 1
        kuyruk.append(v)
  aldigi = sum(1 for (a, b) in bag if a == i)
  return alpha * aldigi + sum(uz.values())


if __name__ == "__main__":
  # Ders notundaki örnek: yol ağı 1–2–3–4, alpha = 1,5
  yol = [(1, 2), (2, 3), (3, 4)]
  print(maliyet(1, yol, 1.5))
  # Sapma: oyuncu 1 ayrıca (1, 4) bağını alır
  sapma = yol + [(1, 4)]
  print(maliyet(1, sapma, 1.5))

# Beklenen çıktı:
# 7.5
# 7.0
