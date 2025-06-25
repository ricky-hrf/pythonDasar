# fungsi bantu matematika
import math

# ceil
x=10.4
a = 10
def ceil(x):
    """Mengembalikan nilai x dibulatkan ke atas."""
    return math.ceil(x)
hasil1 = ceil(x)
print(f"ceil({x}) = {hasil1}")

# floor
def floor(x):
    """Mengembalikan nilai x dibulatkan ke bawah."""
    return math.floor(x)
# round
def round(a):
    """Mengembalikan nilai x dibulatkan ke bilangan bulat terdekat."""
    return round(a)
hasil3 = round(a)
print(f"round({a}) = {hasil3}")

# exponentiation
def exponentiation(x, y):
    """Mengembalikan nilai x pangkat y."""
    return math.pow(x, y)

# log
def log(x, base=10):
    """Mengembalikan logaritma x dengan basis tertentu."""
    return math.log(x, base)

# akar kuadrat
def akar_kuadrat(x):
    """Mengembalikan akar kuadrat dari x."""
    return math.sqrt(x)

# pow
def pow(x, y):
    """Mengembalikan nilai x pangkat y."""
    return math.pow(x, y)

# cos
def cos(x):
    """Mengembalikan nilai cosinus dari x (dalam radian)."""
    return math.cos(x)

# sin
def sin(x):
    """Mengembalikan nilai sinus dari x (dalam radian)."""
    return math.sin(x)

# tan
def tan(x):
    """Mengembalikan nilai tangen dari x (dalam radian)."""
    return math.tan(x)

# radiant
def radiant(degree):
    """Mengkonversi derajat ke radian."""
    return math.radians(degree)

# mod
def mod(x, y):
    """Mengembalikan sisa bagi dari x dibagi y."""
    return x % y

# log10
def log10(x):
    """Mengembalikan logaritma x dengan basis 10."""
    return math.log10(x)


hasil2 = floor(x)
print(f"floor({x}) = {hasil2}")

hasil4 = exponentiation(2, 3)
print(f"exponentiation(2, 3) = {hasil4}")
hasil5 = log(100, 10)
print(f"log(100, 10) = {hasil5}")
hasil6 = akar_kuadrat(16)
print(f"akar_kuadrat(16) = {hasil6}")
hasil7 = pow(2, 3)
print(f"pow(2, 3) = {hasil7}")
hasil8 = cos(radiant(60))
print(f"cos(60 derajat) = {hasil8}")
hasil9 = sin(radiant(30))
print(f"sin(30 derajat) = {hasil9}")
hasil10 = tan(radiant(45))
print(f"tan(45 derajat) = {hasil10}")
hasil11 = radiant(180)
print(f"radian(180 derajat) = {hasil11}")
hasil12 = mod(10, 3)
print(f"mod(10, 3) = {hasil12}")
hasil13 = log10(1000)
print(f"log10(1000) = {hasil13}")
