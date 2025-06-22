# konsep rekursif
def rekursif(n):
  if n == 0:
    return 1
  else:
    return rekursif(n - 1)
  
x = rekursif(5)
print(x)