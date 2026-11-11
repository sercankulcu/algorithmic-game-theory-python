"""Bölüm 13 · Kod İzleme: Q-öğrenme

Dört hücreli koridorda (s3 hedef, r = 1) kaydedilmiş epizotlardan Q-öğrenme
güncellemesi yapar. Slayttaki kodun aynısıdır; örnek ders notundaki üç epizot
ve q_learn(ep, 0.5, 0.9) çağrısıdır. Eylem 0 = sol, 1 = sağ.
"""

def q_learn(episodes, alpha, gamma):
    Q = [[0.0, 0.0] for s in range(4)]  # [sol, sağ]
    for ep in episodes:
        for s, a, r, s2 in ep:
            best = 0 if s2 == 3 else max(Q[s2])
            hedef = r + gamma * best
            Q[s][a] += alpha * (hedef - Q[s][a])
    return Q


if __name__ == "__main__":
    sag = [(0, 1, 0, 1), (1, 1, 0, 2), (2, 1, 1, 3)]
    sapma = [(0, 1, 0, 1), (1, 0, 0, 0), (0, 1, 0, 1), (1, 1, 0, 2), (2, 1, 1, 3)]
    ep = [sag, sag, sapma]
    Q = q_learn(ep, 0.5, 0.9)
    for s in range(3):
        print("s%d" % s, [round(x, 3) for x in Q[s]])

# Beklenen çıktı:
# s0 [0.0, 0.152]
# s1 [0.046, 0.45]
# s2 [0.0, 0.875]
