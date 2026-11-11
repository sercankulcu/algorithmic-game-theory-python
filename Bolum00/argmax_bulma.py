"""Bölüm 0 · İzleme: argmax Bulma

Dört eylemin kazançları arasında döngüyle en büyüğü (max) ve onu veren
eylemi (argmax) bulur; eşitlikte ilk bulunanı tutar. Slayttaki kodun aynısıdır.
"""

eylem  = ["A", "B", "C", "D"]
kazanc = [3, 7, 2, 7]
en_iyi = 0             # en iyinin indisi
for i in range(1, 4):
    if kazanc[i] > kazanc[en_iyi]:
        en_iyi = i
print(kazanc[en_iyi], eylem[en_iyi])


# Beklenen çıktı:
# 7 B
