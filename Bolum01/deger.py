"""Bölüm 1 · Kod İzleme: deger()

Karar ağacını özyinelemeyle çözer: karar düğümünde en büyük değeri, şans
düğümünde beklenen değeri alır. Fonksiyon slayttaki kodun aynısıdır; lansman
ağacı (agac) ders notundan alınmıştır.
"""

def deger(n):
    if not isinstance(n, tuple):    # yaprak
        return n
    tur, dallar = n
    if tur == "S":                  # şans düğümü
        return sum(p * deger(c) for p, c in dallar)
    return max(deger(c) for ad, c in dallar)  # karar


if __name__ == "__main__":
    # "K": karar düğümü, "S": şans düğümü
    agac = ("K", [
        ("Araştır", ("S", [
            (0.38, ("K", [("Sür", ("S", [(16/19, 480), (3/19, -220)])),
                          ("Sürme", -20)])),
            (0.62, ("K", [("Sür", ("S", [(4/31, 480), (27/31, -220)])),
                          ("Sürme", -20)]))])),
        ("Doğrudan", ("K", [("Sür", ("S", [(0.4, 500), (0.6, -200)])),
                            ("Sürme", 0)]))])
    print(deger(agac))


# Beklenen çıktı:
# 128.0
