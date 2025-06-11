odd_squares = tuple(x**2 for x in range(1, 51) if x % 2 != 0)
capital_chars = tuple(chr(ord('A') + i) for i in range(0, 26, 3))
checksum = 0
for num in odd_squares:
    checksum ^= num
result = (odd_squares, capital_chars, checksum)
print(result)