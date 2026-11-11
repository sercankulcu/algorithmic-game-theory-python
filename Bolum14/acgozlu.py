"""Bölüm 14 · Kod İzleme: acgozlu()

Kombinatoryal açık artırmada açgözlü kazanan belirleme: teklifler bir anahtara
göre sıralanır ve nesneleri çakışmayan paketler sırayla alınır. Değere göre ve
nesne başına değere göre iki sıralama karşılaştırılır. Slayttaki kodun
aynısıdır.
"""

def acgozlu(teklifler, anahtar):
    sirali = sorted(teklifler, key=anahtar, reverse=True)
    toplam, kullanilan = 0, set()
    for S, v in sirali:
        if not (S & kullanilan):  # çakışma yok
            toplam += v
            kullanilan |= S
    return toplam
T = [({'a','b','c'}, 10), ({'a'}, 4), ({'b'}, 4), ({'c'}, 3)]
print(acgozlu(T, lambda t: t[1]))
print(acgozlu(T, lambda t: t[1] / len(t[0])))

# Beklenen çıktı:
# 10
# 11
