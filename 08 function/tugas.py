print("======PROGRAM MENGHITUNG NILAI SUKU FIBONACI======")
def fibonacci(n):
    if n < 0:
        raise ValueError("n tidak boleh negatif")
    elif n == 0:
        return 0
    elif n == 1: 
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Masukkan nilai n: "))
print(f"F({n}) = {fibonacci(n)}")