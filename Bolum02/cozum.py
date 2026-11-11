"""Bölüm 2 · Kod İzleme: cozum()

Mükemmel bilgili sıralı bir oyunun ağacını geriye doğru çıkarımla çözer; her
düğümde seçilen dalı yazar ve alt oyun mükemmel dengenin kazanç vektörünü döndürür.
Slayttaki kodun aynısıdır.
"""

def cozum(d):
    if isinstance(d, tuple):         # yaprak: kazanç
        return d
    ad, oyuncu, dallar = d
    en_iyi = None
    for hamle, cocuk in dallar:
        v = cozum(cocuk)
        if en_iyi is None or v[oyuncu] > en_iyi[oyuncu]:
            en_iyi, secim = v, hamle
    print(ad, secim)
    return en_iyi
kok = ['kök', 0, [('Sol', ['x', 1, [('a', (3, 1)), ('b', (1, 2))]]),
                  ('Sağ', ['y', 1, [('c', (2, 1)), ('d', (0, 0))]])]]
print(cozum(kok))


# Beklenen çıktı:
# x b
# y c
# kök Sağ
# (2, 1)
