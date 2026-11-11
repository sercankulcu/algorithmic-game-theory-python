"""Bölüm 3 · Kod İzleme: ele()

3 × 3 bir oyunda kesin baskılanan satır ve sütunları yinelemeli olarak eler ve
kalan satır ile sütun indislerini döndürür. Fonksiyon slayttaki kodun aynısıdır;
örnek oyun slayttaki ve notlardaki 3 × 3 eleme örneğidir.
"""

def ele(U1, U2):
    R, S = [0, 1, 2], [0, 1, 2]   # kalanlar
    while True:
        x = [r for r in R for k in R if
             all(U1[k][c] > U1[r][c] for c in S)]
        y = [c for c in S for d in S if
             all(U2[r][d] > U2[r][c] for r in R)]
        if x: R.remove(x[0])      # satır elenir
        elif y: S.remove(y[0])    # sütun elenir
        else: return R, S


if __name__ == "__main__":
    # satırlar A, B, C; sütunlar X, Y, Z
    U1 = [[3, 3, 1], [3, 0, 5], [2, 2, 6]]
    U2 = [[2, 3, 4], [2, 4, 3], [1, 0, 6]]
    print(ele(U1, U2))


# Beklenen çıktı:
# ([2], [2])
