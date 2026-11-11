"""Bölüm 4 · TTC Kod İzleme

Top Trading Cycles (en üst takas döngüleri): herkes en sevdiği kalan odanın
sahibini gösterir, bulunan döngüdekiler takas edip çıkar. atama[k], k'nin aldığı
odanın sahibidir. Fonksiyon slayttaki kodun aynısıdır; tercihler slayttaki örnektir.
"""

def ttc(pref):
  kalan, atama = list(pref), {}
  while kalan:
    g = {i: next(j for j in pref[i]
             if j in kalan) for i in kalan}
    i, yol = kalan[0], []
    while i not in yol:          # okları izle
      yol.append(i); i = g[i]
    dongu = yol[yol.index(i):]
    for k in dongu:              # takas
      atama[k] = g[k]; kalan.remove(k)
  return atama


if __name__ == "__main__":
    pref = {'A': ['C', 'A', 'B'],
            'B': ['A', 'D', 'B'],
            'C': ['B', 'A', 'C'],
            'D': ['C', 'E', 'B', 'D'],
            'E': ['A', 'D', 'E']}
    print(ttc(pref))


# Beklenen çıktı:
# {'A': 'C', 'C': 'B', 'B': 'A', 'D': 'E', 'E': 'D'}
