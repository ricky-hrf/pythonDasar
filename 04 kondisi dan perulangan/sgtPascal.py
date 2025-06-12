def pascal_triangle(n):
    for i in range(n):
        num = 1
        print(" " * (n - i), end="")
        for j in range(i + 1):
            print(f"{num} ", end="")
            num = num * (i - j) // (j + 1)
        print()

# Contoh pemanggilan
pascal_triangle(6)
