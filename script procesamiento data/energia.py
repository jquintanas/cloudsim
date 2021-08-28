mapa = {}
file = open("/home/jquintana/Desktop/LR/energiaConsumoLR.txt", "r")
file.readline()
for linea in file:
    if linea != "tiempo,host,consumoEnergia  W*sec\n":
        array = linea.strip().split(",")
        if mapa.get(array[0]) is None:
            host = {int(array[1])}
            consumo = float(array[2])
            value = [host, consumo]
            mapa.setdefault(array[0], value)
        else:
            data = mapa.get(array[0])
            host = data[0].add(int(array[1]))
            consumo = float(array[2]) + data[1]
            value = [host, consumo]
            mapa.setdefault(array[0], value)
file.close()
dicSalida = {}
ene = 0
for key in mapa:
    data = mapa.get(key)
    host = len(data[0])
    consumo = data[1]
    value = [host, consumo]
    dicSalida.setdefault(key, value)
fileSalida = open("energiaConsumoLR.csv", "w")
fileSalida.write("tiempo;host;consumoEnergia  W*sec\n")
for key in dicSalida:
    data = dicSalida.get(key)
    ene += data[1]
    linea = "{0};{1};{2}\n".format(key,data[0], data[1])
    fileSalida.write(linea)
fileSalida.close()
print(ene)