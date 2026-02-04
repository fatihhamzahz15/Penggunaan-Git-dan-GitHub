cars = ["Ford", "Volvo", "BMW"]
print(cars[0])

x = len(cars)
print(x)

for x in cars:
  print(x)

cars.append("Honda")#append untuk menambahkan ke paling akhir
print(cars)

cars.pop(1)
print(cars)

cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")# sama seperti pop
print(cars)