"""Bölüm 13 · Kod İzleme: ε-açgözlü

Çok kollu haydutta ε-açgözlü algoritma: ε olasılıkla rastgele kol (keşif),
yoksa en büyük tahminli kol (sömürü). Slayttaki kodun aynısıdır; örnek ders
notundaki egreedy([0.3, 0.5, 0.7], 8, 0.2, random.Random(11)) çağrısıdır.
"""
import random


def egreedy(mu, T, eps, rng):
    N, Q = [0] * len(mu), [0.0] * len(mu)
    for t in range(1, T + 1):
        if rng.random() < eps:           # keşif
            a = rng.randrange(len(mu))
        else:                            # sömürü
            a = Q.index(max(Q))
        r = 1 if rng.random() < mu[a] else 0
        N[a] += 1
        Q[a] += (r - Q[a]) / N[a]
    return N, Q


if __name__ == "__main__":
    N, Q = egreedy([0.3, 0.5, 0.7], 8, 0.2, random.Random(11))
    print(N, [round(q, 2) for q in Q])

# Beklenen çıktı:
# [3, 0, 5] [0.0, 0.0, 0.8]
