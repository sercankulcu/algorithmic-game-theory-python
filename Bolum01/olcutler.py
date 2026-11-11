"""Bölüm 1 · Kod İzleme: Belirsizlik Ölçütleri

Olasılıkların bilinmediği bir karar tablosunda maksimin, maksimaks, Laplace ve
Savage (minimaks pişmanlık) ölçütlerine göre seçilen eylemlerin indislerini döndürür.
Fonksiyon slayttaki kodun aynısıdır; alttaki örnek yatırım tablosu ders notundandır.
"""

def olcutler(U):
    A, m = range(len(U)), len(U[0])
    mm = max(A, key=lambda i: min(U[i]))      # maximin
    mx = max(A, key=lambda i: max(U[i]))      # maximax
    lp = max(A, key=lambda i: sum(U[i]) / m)  # Laplace
    enb = [max(r[j] for r in U) for j in range(m)]
    pis = [max(enb[j] - r[j] for j in range(m))
           for r in U]            # en büyük pişmanlık
    sv = pis.index(min(pis))                  # Savage
    return mm, mx, lp, sv


if __name__ == "__main__":
    # satırlar: 0 Büyük yatırım, 1 Küçük yatırım, 2 Yatırım yok
    # sütunlar: İyi, Orta, Kötü
    U = [[200, 50, -120],
         [90, 40, -20],
         [0, 0, 0]]
    print(olcutler(U))


# Beklenen çıktı:
# (2, 0, 0, 1)
