"""Bölüm 13 · Kod İzleme: hedge()

Hedge (çarpımsal ağırlıklar) algoritması: her eylemin ağırlığı e^(η·kazanç)
ile çarpılır, eylemler ağırlıkla orantılı olasılıkla seçilir; toplam beklenen
kazancı döndürür. Slayttaki kodun aynısıdır; örnek ders notundaki üç uzmanlı,
beş turluk dizidir (η = 0,5).
"""

import math
def hedge(G, eta):
    w = [1.0] * len(G[0])
    top = 0.0
    for g in G:                       # her tur
        W = sum(w)
        p = [x / W for x in w]
        top += sum(pi * gi for pi, gi in zip(p, g))
        w = [x*math.exp(eta*gi) for x, gi in zip(w, g)]
    return top


if __name__ == "__main__":
    G = [[1, 0, 0.5]] * 2 + [[0, 1, 0.5]] * 3
    top = hedge(G, 0.5)
    print(round(top, 2))
    print("pişmanlık:", round(3 - top, 2))

# Beklenen çıktı:
# 2.34
# pişmanlık: 0.66
