# aplikasi dengan fungsi bantu matematika
import math
#     """Mengkonversi derajat ke radian."""
def radiant(degree):
    return math.radians(degree)
convert = radiant(180)
print(f"180 derajat dalam radian = {convert}")

# fungsi hitung suhu
def hitung_suhu(suhu, satuan_asal, satuan_tujuan):
    """Mengkonversi suhu dari satu satuan ke satuan lainnya."""
    if satuan_asal == "C":
        if satuan_tujuan == "F":
            return (suhu * 9/5) + 32
        elif satuan_tujuan == "K":
            return suhu + 273.15
    elif satuan_asal == "F":
        if satuan_tujuan == "C":
            return (suhu - 32) * 5/9
        elif satuan_tujuan == "K":
            return (suhu - 32) * 5/9 + 273.15
    elif satuan_asal == "K":
        if satuan_tujuan == "C":
            return suhu - 273.15
        elif satuan_tujuan == "F":
            return (suhu - 273.15) * 9/5 + 32
    else:
        raise ValueError("Satuan tidak valid")
    
# Contoh penggunaan fungsi hitung_suhu
suhu_c = 25
suhu_f = hitung_suhu(suhu_c, "C", "F")
suhu_k = hitung_suhu(suhu_c, "C", "K")
print(f"{suhu_c}°C = {suhu_f}°F")