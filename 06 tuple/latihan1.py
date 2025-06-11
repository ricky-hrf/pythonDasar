data = ((1, 2, 'a'), (3, 'b', 'c'), (4, 5, 'd'))

total = 0
strings = []

for sub_tuple in data:
    for item in sub_tuple:
        if isinstance(item, int):
            total += item
        elif isinstance(item, str):
            strings.append(item)

print(f"Jumlah numerik: {total}")
print(f"String gabungan: {'-'.join(strings)}")