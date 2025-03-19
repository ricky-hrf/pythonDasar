print("perulangan dengan nested")
for i in range(3):  
    for j in range(3):  
        print(f"i={i}, j={j}")

for i in range(1, 6):  
    for j in range(i):  
        print("*", end="")  
    print() 

    for a in range(1, 6):  
        for b in range(1, 6):  
            print(a * b, end="\t") 
    print() 

    jam = 1

while jam <= 2:  
    menit = 0
    while menit < 60:  
        print(f"Jam {jam}, Menit {menit}")
        menit += 30  
    jam += 1


