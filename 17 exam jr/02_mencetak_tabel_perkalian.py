# program mencetak tabel perkalian
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j:2}", end="\t")
    print()  # New line after each row