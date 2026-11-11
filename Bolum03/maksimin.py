"""Bölüm 3 · Kod İzleme: maksimin()

2 × n bir sıfır toplamlı oyunda satır oyuncusunun maksimin karışık stratejisini,
doğruların kesişim noktalarını aday alarak tam kesirlerle bulur. Fonksiyon slayttaki
kodun aynısıdır; örnek matris ders notundandır.
"""

from fractions import Fraction as F
def maksimin(A):                  # A: 2 x n
    n, aday = len(A[0]), [F(0), F(1)]
    for j in range(n):
        for k in range(j + 1, n):
            d = A[0][j] - A[1][j] - A[0][k] + A[1][k]
            if d != 0:
                aday.append(F(A[1][k] - A[1][j], d))
    g = lambda p: min(p*a+(1-p)*b for a, b in zip(*A))
    p = max((c for c in aday if 0 <= c <= 1), key=g)
    return p, g(p)


if __name__ == "__main__":
    # sütunlar X, Y, Z
    A = [[4, 1, 3], [0, 3, 2]]
    p, v = maksimin(A)
    print(p, v)


# Beklenen çıktı:
# 1/2 2
