"""Bölüm 12 · Kod İzleme: selale()

İki torba modelinde bilgi şelalesi: her kişi öncekilerin tahminlerinden çıkan
a − b farkı 2'ye ulaşınca kendi sinyalini yok sayar. Slayttaki kodun aynısıdır;
örnek ders notundaki a, a, b, b, b, b sinyal dizisidir (gerçek torba B).
"""

def selale(sinyaller):
    f = 0                  # tahminlerden çıkan a − b
    tahmin = []
    for s in sinyaller:
        if f >= 2: t = 'A'     # A şelalesi
        elif f <= -2: t = 'B'  # B şelalesi
        else:
            t = 'A' if s == 'a' else 'B'
            f += 1 if s == 'a' else -1
        tahmin.append(t)
    return tahmin


if __name__ == "__main__":
    print(selale(['a', 'a', 'b', 'b', 'b', 'b']))

# Beklenen çıktı:
# ['A', 'A', 'A', 'A', 'A', 'A']
