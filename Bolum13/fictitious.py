"""Bölüm 13 · Kod İzleme: fictitious()

Yazı-Tura Eşleştirme oyununda kurgusal oyun (fictitious play): her oyuncu
rakibinin geçmiş eylem frekanslarına en iyi tepkiyi verir; Y/T sayaçlarını
döndürür (0 = Y, 1 = T). Slayttaki kodun aynısıdır; örnek fictitious(6).
"""

def fictitious(T):
    ne, na = [0, 0], [0, 0]   # Y/T sayaçları
    a, b = 0, 0               # 1. tur: ikisi de Y
    for t in range(1, T + 1):
        ne[a] += 1            # eşleştirenin geçmişi
        na[b] += 1            # ayrıştıranın geçmişi
        # eşleştiren: ayrıştıranın çoğunluğunu eşle
        a = 0 if na[0] >= na[1] else 1
        # ayrıştıran: eşleştirenin çoğunluğundan ayrış
        b = 1 if ne[0] > ne[1] else 0
    return ne, na


if __name__ == "__main__":
    ne, na = fictitious(6)
    print(ne, na)
    print(round(ne[0] / 6, 2), round(na[0] / 6, 2))

# Beklenen çıktı:
# [3, 3] [1, 5]
# 0.5 0.17
