"""Bölüm 3 · Kod İzleme: saf_nash()

İki oyunculu bir matris oyununun bütün saf Nash dengelerini, her hücrede iki
oyuncunun da en iyi tepkide olup olmadığına bakarak bulur. Fonksiyon slayttaki
kodun aynısıdır; örnek 3 × 3 oyun ders notundandır.
"""

def saf_nash(U1, U2):
    m, n, denge = len(U1), len(U1[0]), []
    for i in range(m):
        for j in range(n):
            br1 = max(U1[k][j] for k in range(m))
            br2 = max(U2[i][l] for l in range(n))
            if U1[i][j] == br1 and U2[i][j] == br2:
                denge.append((i, j))
    return denge


if __name__ == "__main__":
    # satırlar A, B, C; sütunlar X, Y, Z
    U1 = [[4, 0, 1], [2, 3, 0], [1, 2, 3]]
    U2 = [[3, 2, 1], [1, 3, 2], [4, 0, 2]]
    print(saf_nash(U1, U2))


# Beklenen çıktı:
# [(0, 0), (1, 1)]
