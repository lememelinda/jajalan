import matematika as m

#luasPersegi
print('Kalkulator luas persegi\n')
s=int(input("Masukkan s ="))
print("Luas Persegi = ", m.luasPersegi(s))
print('\n')

#luasPersegiPanjang
print('Kalkulator luas persegi panjang\n')
p=int(input("Masukkan panjang ="))
l=int(input("Masukkan lebar ="))
print("Luas Persegi Panjang = ", m.luasPersegip(p,l))
print('\n')

#luasSegitiga
print('Kalkulator luas Segitiga\n')
a=int(input("Masukkan alas ="))
t=int(input("Masukkan tinggi ="))
print("Luas Segitiga = ", m.luasSegitiga(a,t))
print('\n')

#luastrapesium
print('Kalkulator luas Trapesium\n')
sisi1=int(input("Masukkan Sisi 1 ="))
sisi2=int(input("Masukkan Sisi 2 ="))
t=int(input("Masukkan Tinggi ="))
print("Luas Trapesium= ", m.trapesium(sisi1,sisi2,t))
print('\n')

#luasJajargenjang
print('Kalkulator luas Jajar Genjang\n')
l=int(input("Masukkan Lebar ="))
t=int(input("Masukkan Tinggi ="))
print("Luas Jajar Genjang = ", m.jajargenjang(l,t))



