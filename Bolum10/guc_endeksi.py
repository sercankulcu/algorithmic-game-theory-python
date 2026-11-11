"""Bölüm 10 · Kod İzleme: guc_endeksi()

Ağırlıklı oylama oyununda Shapley–Shubik güç endeksini, her geliş sırasında
kotayı geçiren (kilit) oyuncuyu sayarak hesaplar. Slayttaki kodun aynısıdır;
slaytta görünmeyen `from itertools import permutations` satırı eklenmiştir.
Örnekler: ders notundaki meclis [51; 50, 49, 1] ve 1958 AET Bakanlar Konseyi
[12; 4, 4, 4, 2, 2, 1].
"""
from itertools import permutations   # slaytta yok; kodun çalışması için eklendi


def guc_endeksi(N, w, q):
  kilit = {i: 0 for i in N}
  siralar = list(permutations(N))
  for sira in siralar:
    toplam = 0
    for i in sira:
      toplam += w[i]
      if toplam >= q:
        kilit[i] += 1
        break
  return {i: kilit[i] / len(siralar) for i in N}


if __name__ == "__main__":
  print(guc_endeksi(["A", "B", "C"], {"A": 50, "B": 49, "C": 1}, 51))
  aet = {"FR": 4, "DE": 4, "IT": 4, "BE": 2, "NL": 2, "LU": 1}
  g = guc_endeksi(list(aet), aet, 12)
  print({i: round(x, 4) for i, x in g.items()})

# Beklenen çıktı:
# {'A': 0.6666666666666666, 'B': 0.16666666666666666, 'C': 0.16666666666666666}
# {'FR': 0.2333, 'DE': 0.2333, 'IT': 0.2333, 'BE': 0.15, 'NL': 0.15, 'LU': 0.0}
