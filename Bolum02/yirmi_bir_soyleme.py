"""Bölüm 2 · Kod İzleme: 21'i Söyleme

21'i Söyleme oyununda geriye doğru etiketlemeyle her sayının kazanan mı kaybeden
mi olduğunu bulur ve kontrol sayılarını (kaybeden durumları) yazar. Slayttaki
kodun aynısıdır.
"""

HEDEF = 21
kazanir = {HEDEF - 1: False}   # c=20: kayıp
for c in range(HEDEF - 2, -1, -1):
    kazanir[c] = any(not kazanir[c + k]
        for k in (1, 2, 3) if c + k < HEDEF)
kontrol = [c for c in kazanir if not kazanir[c]]
print(sorted(kontrol))


# Beklenen çıktı:
# [0, 4, 8, 12, 16, 20]
