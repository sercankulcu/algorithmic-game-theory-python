"""Bölüm 4 · Gale–Shapley Kod İzleme

Öğrenci teklifli Gale–Shapley ertelenmiş kabul algoritmasıyla öğrencileri
projelere kararlı biçimde eşleştirir. Fonksiyon slayttaki kodun aynısıdır;
tercih listeleri ders notundaki örnektir (proj[p][s]: p'nin s'ye verdiği sıra, 0 = en iyi).
"""

def gale_shapley(ogr, proj):
  serbest, es = list(ogr), {}
  sira = {s: 0 for s in ogr}
  while serbest:
    s = serbest.pop(0)
    p = ogr[s][sira[s]]        # sıradaki
    sira[s] += 1
    r = es.get(p)              # p'deki aday
    if r is None or proj[p][s] < proj[p][r]:
      es[p] = s                # kabul
      if r: serbest.append(r)
    else: serbest.append(s)    # red
  return es


if __name__ == "__main__":
    ogr = {'A': ['X', 'Y', 'Z'],
           'B': ['X', 'Z', 'Y'],
           'C': ['Y', 'X', 'Z']}
    proj = {'X': {'B': 0, 'A': 1, 'C': 2},
            'Y': {'A': 0, 'C': 1, 'B': 2},
            'Z': {'A': 0, 'B': 1, 'C': 2}}
    print(gale_shapley(ogr, proj))


# Beklenen çıktı:
# {'X': 'B', 'Y': 'A', 'Z': 'C'}
