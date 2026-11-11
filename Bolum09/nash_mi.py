"""Bölüm 9 · Kod İzleme: nash_mi

Yük dengeleme oyununda bir iş atamasının saf Nash dengesi olup olmadığını
denetler: hiçbir iş başka bir makineye geçerek daha erken bitmiyorsa True
döndürür. Fonksiyon, "Kod İzleme: nash_mi" slaytındaki kodun aynısıdır.
"""


def nash_mi(boy, atama, m):
  yuk = [0] * m
  for j, k in enumerate(atama):
    yuk[k] += boy[j]
  for j, k in enumerate(atama):
    for h in range(m):
      if yuk[h] + boy[j] < yuk[k]:
        return False      # j kaçar
  return True             # kimse kaçmaz


if __name__ == "__main__":
  # Ders notundaki örnek: işler {2, 2, 1, 1}, iki makine
  boy = [2, 2, 1, 1]
  print(nash_mi(boy, (0, 0, 1, 1), 2))   # {2, 2} | {1, 1}
  print(nash_mi(boy, (0, 0, 0, 1), 2))   # {2, 2, 1} | {1}

# Beklenen çıktı:
# True
# False
