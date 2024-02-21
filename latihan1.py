filtered_numbers = [i for i in range(1, 100) if (i >= 10 and i <= 20 and i % 2 == 0) or (i >= 90 and i <= 100 and i % 2 != 0)]

print("<<<      LATIHAN     >>>")
print("Berikut akan tampil list dengan kondisi:")
print("1. range(1,100)")
print("Hanya value/item : genap (i >=10 dan i <=20)")
print("Hanya value/item : ganjil (i >=90 dan i <=100)\n")

print(tuple(filtered_numbers))