# program mencari total dan rata-rata dari sebuah list
print("======PROGRAM MENCARI TOTAL DAN RATA-RATA DARI SEBUAH LIST======")
nilai = []

def total_rata_rata(nilai_list):
    total = sum(nilai_list)
    rata_rata = total / len(nilai_list)
    return total, rata_rata
total, rata_rata = total_rata_rata(nilai)
print(f"Total: {total}, Rata-rata: {rata_rata}")