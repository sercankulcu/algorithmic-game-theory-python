"""Bölüm 10 · Kod İzleme: shapley() (1/2 ve 2/2)

Shapley değerini, bütün geliş sıralarındaki marjinal katkıların ortalaması
olarak hesaplar. İki slayttaki kodun (aynı fonksiyon) aynısıdır; slaytta
görünmeyen `from itertools import permutations` satırı eklenmiştir. Örnek,
ders notundaki v(A)=10, v(B)=20, v(C)=30, v(AB)=50, v(AC)=60, v(BC)=70,
v(ABC)=120 oyunudur.
"""
from itertools import permutations   # slaytta yok; kodun çalışması için eklendi


def shapley(N, v):
  phi = {i: 0 for i in N}
  siralar = list(permutations(N))
  for sira in siralar:
    S = frozenset()
    for i in sira:
      katki = v[S | {i}] - v[S]
      phi[i] += katki
      S = S | {i}
  return {i: phi[i] / len(siralar) for i in N}


if __name__ == "__main__":
  v = {
    frozenset(): 0,
    frozenset({"A"}): 10, frozenset({"B"}): 20, frozenset({"C"}): 30,
    frozenset({"A", "B"}): 50, frozenset({"A", "C"}): 60,
    frozenset({"B", "C"}): 70,
    frozenset({"A", "B", "C"}): 120,
  }
  print(shapley(["A", "B", "C"], v))

# Beklenen çıktı:
# {'A': 30.0, 'B': 40.0, 'C': 50.0}
