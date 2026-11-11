"""Bölüm 4 · VCG Kod İzleme / VCG Tek Nesne İzleme

VCG mekanizması: toplam refahı en büyük yapan sonucu seçer ve her oyuncuya
ötekilere yüklediği dışsallık kadar ödeme yazar. Fonksiyon iki slaytta da aynıdır
(VCG Kod İzleme ve VCG Tek Nesne İzleme); alt blok iki örneği de çalıştırır:
kamu projesi ve tek nesne (VCG = Vickrey ikinci fiyat açık artırması).
"""

def vcg(v, A):
  N = list(v)            # oyuncular
  def w(a, S):           # S'nin a'daki refahı
    return sum(v[i][a] for i in S)
  x = max(A, key=lambda a: w(a, N))
  p = {}
  for i in N:
    D = [j for j in N if j != i]
    yok = max(w(a, D) for a in A)  # i yokken
    var = w(x, D)                  # i varken
    p[i] = yok - var
  return x, p


if __name__ == "__main__":
    # 1) Kamu projesi: P = Park, K = Kütüphane, S = Spor salonu
    v = {'Ayşe': {'P': 40, 'K': 5, 'S': 0},
         'Bora': {'P': 0, 'K': 30, 'S': 20},
         'Cem': {'P': 10, 'K': 20, 'S': 45}}
    A = ['P', 'K', 'S']
    x, p = vcg(v, A)
    print(x, p, "toplam", sum(p.values()))

    # 2) Tek nesne: sonuç = nesneyi kimin aldığı
    degerler = {'Ayşe': 70, 'Bora': 55, 'Cem': 85}
    v = {i: {a: (degerler[i] if a == i else 0) for a in degerler}
         for i in degerler}
    A = list(degerler)
    x, p = vcg(v, A)
    print(x, p)


# Beklenen çıktı:
# S {'Ayşe': 0, 'Bora': 5, 'Cem': 20} toplam 25
# Cem {'Ayşe': 0, 'Bora': 0, 'Cem': 70}
