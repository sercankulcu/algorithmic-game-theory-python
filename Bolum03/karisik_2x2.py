"""Bölüm 3 · Kod İzleme: karisik_2x2()

2 × 2 bir oyunun iç karışık Nash dengesini kayıtsızlık ilkesiyle tam kesirlerle
hesaplar: satır olasılığı p, sütun olasılığı q ve satır oyuncusunun kazancı.
Fonksiyon slayttaki kodun aynısıdır; örnekler ders notundandır.
"""

from fractions import Fraction as F
def karisik_2x2(A, B):
    da = A[0][0] - A[0][1] - A[1][0] + A[1][1]
    if da == 0: return None     # denklem yok
    q = F(A[1][1] - A[0][1], da)  # satır kayıtsız
    db = B[0][0] - B[0][1] - B[1][0] + B[1][1]
    if db == 0: return None
    p = F(B[1][1] - B[1][0], db)  # sütun kayıtsız
    if not (0 < p < 1 and 0 < q < 1):
        return None               # iç denge yok
    u1 = A[0][0] * q + A[0][1] * (1 - q)
    return p, q, u1


if __name__ == "__main__":
    # Cinsiyetler Savaşı: 0 = Opera, 1 = Futbol
    p, q, u1 = karisik_2x2([[3, 0], [0, 2]], [[2, 0], [0, 3]])
    print(p, q, u1)
    # Bedava Para: iç denge yok
    print(karisik_2x2([[1, 0], [0, 0]], [[1, 0], [0, 0]]))
    # Mahkûmun İkilemi: da = 0
    print(karisik_2x2([[-1, -3], [0, -2]], [[-1, 0], [-3, -2]]))


# Beklenen çıktı:
# 3/5 2/5 6/5
# None
# None
