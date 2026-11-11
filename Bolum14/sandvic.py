"""Bölüm 14 · Kod İzleme: sandvic()

xy = k otomatik piyasa yapıcıda sandviç saldırısı: saldırgan kullanıcının
işleminin önüne geçip arkasından satar; kullanıcının kayma sınırı (min_out)
aşılırsa işlem iptal olur. Saldırganın kârını yazdırır. Slayttaki kodun
aynısıdır.
"""

cikti = lambda x, y, dx: y - x * y / (x + dx)  # xy=k
def sandvic(x, y, a, u, min_out):
    b1 = cikti(x, y, a)          # öne geç: a A sat
    x, y = x + a, y - b1
    b2 = cikti(x, y, u)          # kullanıcı: u A sat
    if b2 < min_out:
        return None              # işlem iptal
    x, y = x + u, y - b2
    a2 = cikti(y, x, b1)         # arkadan: b1 B sat
    return round(a2 - a, 2)
for a in [20, 50, 80]:
    print(a, sandvic(1000, 1000, a, 100, 82))

# Beklenen çıktı:
# 20 4.07
# 50 9.71
# 80 None
