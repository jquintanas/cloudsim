file = open("energiaConsumoDataCenter.csv", "r")
total = 0
for linea in file:
    data = linea.strip().split(";")
    total += float(data[1])
print(total)