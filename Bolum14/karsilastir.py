"""Bölüm 14 · Kod İzleme: karsilastir()

Algoritmik danışıklılıkta tetik stratejisi: her dönem 50 ile işbirliği yolunu,
s. dönemde fiyat kırıp 100 alan ve sonra 0 kazanan sapma yoluyla iskontolu
toplamlar üzerinden karşılaştırır. Slayttaki kodun aynısıdır.
"""

def karsilastir(delta, s, T):
    ib, sp = 0.0, 0.0            # işbirliği / sapma yolu
    for t in range(T):
        ib += delta**t * 50
        if t < s:
            sp += delta**t * 50
        elif t == s:
            sp += delta**t * 100   # A fiyat kırar
        # t > s: tetik devrede, kâr 0
    return round(ib, 2), round(sp, 2)
print(karsilastir(0.6, 2, 6))
print(karsilastir(0.4, 2, 6))

# Beklenen çıktı:
# (119.17, 116.0)
# (82.99, 86.0)
