# Diberikan dua tuple, lakukan operasi berikut:
# 1. Gabungkan kedua tuple secara bergantian (alternating)
# 2. Hapus duplikat tanpa mengubah urutan
# 3. Balik urutan setiap 3 elemen
# Constraint: Tidak boleh menggunakan struktur data tambahan selain tuple

a = (1, 3, 5, 7, 9)
b = (2, 4, 6, 8, 10)

# Expected Output:
# (6, 4, 2, 1, 3, 9, 7, 5, 10, 8)

# Mulai kode Anda di sini:
# 1. Alternating merge
merged = tuple(item for pair in zip(a, b) for item in pair) + a[len(b):] + b[len(a):]

# 2. Remove duplicates (while maintaining order)
unique = tuple()
for item in merged:
    if item not in unique:
        unique += (item,)

# 3. Reverse every 3 elements
result = tuple()
for i in range(0, len(unique), 3):
    chunk = unique[i:i+3]
    reversed_chunk = chunk[::-1]
    result += reversed_chunk

print(result)