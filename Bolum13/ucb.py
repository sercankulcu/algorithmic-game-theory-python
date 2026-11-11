"""Bölüm 13 · Kod İzleme: UCB

Çok kollu haydutta UCB1: her tur Q + √(2 ln t / N) puanı en büyük kol çekilir;
hiç çekilmemiş kolun puanı sonsuzdur. Slayttaki kodun aynısıdır; slaytta
görünmeyen `import math` satırı eklenmiştir. Örnek ders notundaki
ucb([0.3, 0.5, 0.7], 8, random.Random(3)) çağrısıdır.
"""
import math     # slaytta yok; kodun çalışması için eklendi
import random


def ucb(mu, T, rng):
    K = len(mu)
    N, Q = [0] * K, [0.0] * K
    for t in range(1, T + 1):
        b = [math.inf if n == 0 else
             math.sqrt(2*math.log(t)/n) for n in N]
        a = max(range(K), key=lambda i: Q[i] + b[i])
        r = 1 if rng.random() < mu[a] else 0
        N[a] += 1
        Q[a] += (r - Q[a]) / N[a]
    return N, Q


if __name__ == "__main__":
    N, Q = ucb([0.3, 0.5, 0.7], 8, random.Random(3))
    print(N, [round(q, 2) for q in Q])

# Beklenen çıktı:
# [2, 2, 4] [0.5, 0.0, 1.0]
