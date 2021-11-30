#istenen önce direnç değeri al R SEMBOLÜ
# gerilim için v
#ürün için i

v = float(input("gerilim degeri gir"))
r = float(input("direnç değerini gir"))

#kullanıcı dirence 0 girerse işlem tanımsız olur biliyoruz ki işlemlerde 0a bölünce tanımsız oluyor
#bunu bir while ve if else bloklarıyla halledebiliriz

while True:
    if r ==0:
        r = float(input(" direnç 0 olamaz tekrar direnç değerini gir"))
    else:
        break

i = v/r
print("akım değeri :{}".format(i))

