#konversi satuan temperatur
#program konversi celcius ke satuan lain

print("\n==PROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('Masukan suhu dalam celcius: '))
print("Suhu adalah", celcius, "Celcius" )

#reamur
reamur = (4/5)*celcius
print("Suhu adalah", reamur, "Reamur" )

#fahrenheit
fahrenheit = ((9/5)*celcius)+32
print("Suhu adalah", fahrenheit, "Fahrenheit" )

#kelvin
kelvin = celcius + 273
print("Suhu adalah", kelvin, "Kelvin" )
