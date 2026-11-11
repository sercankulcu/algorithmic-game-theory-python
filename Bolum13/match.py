"""Bölüm 13 · Kod İzleme: match()

Tekrarlanan Mahkûmun İkilemi'nde iki stratejiyi T tur karşılaştırır
(S = işbirliği, İ = ihanet). Slayttaki kodun aynısıdır; örnek ders notundaki
match(tft, stft, 6) çağrısı ve on turluk TFT – Şüpheci TFT maçıdır.
"""

PAY = {"SS": (3, 3), "Sİ": (0, 5),
       "İS": (5, 0), "İİ": (1, 1)}
tft = lambda ben, rakip: rakip[-1] if rakip else "S"
stft = lambda ben, rakip: rakip[-1] if rakip else "İ"
def match(s1, s2, T):
    h1, h2, p1, p2 = [], [], 0, 0
    for t in range(T):
        a, b = s1(h1, h2), s2(h2, h1)
        u, v = PAY[a + b]
        h1.append(a); h2.append(b)
        p1, p2 = p1 + u, p2 + v
    return p1, p2


if __name__ == "__main__":
    print(match(tft, stft, 6))
    print(match(tft, stft, 10))

# Beklenen çıktı:
# (15, 15)
# (25, 25)
