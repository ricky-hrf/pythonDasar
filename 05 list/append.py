# append untuk menambahkan bilangan
print("===== Method append (menambahkan bilangan di akhir list) =====")
bilangan = [1,2,3]
bilangan.append(4)
print(bilangan)

print("===== menambahkan beberapa data sekaligus) =====")
hewan = ["kucing", "singa", "harimau"]
hewan.append("jaguar")
hewan.append("Heina")
hewan.append("cheetah")
print(hewan)

print("===== menambahkan list lain sebagai elemen =====")
hewan.append(bilangan)
print(hewan)

print("===== Method extend (menambahkan beberapa elemen di akhir list) =====")
hewan.extend(bilangan)
print(hewan)
