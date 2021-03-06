buka = open("file.txt")
baca = buka.read()
hitung=dict()
kalimat = baca
word = kalimat.split()
for jumlah in word:
	hitung[jumlah] = hitung.get(jumlah,0) + 1
print()
print("Hasil Perhitungan frekuensi :", hitung)