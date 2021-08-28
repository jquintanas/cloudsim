mapa = {}
file = open("/home/jquintana/Desktop/LR/cpuConsumo2LR.txt", "r")
file.readline()
for linea in file:
    if linea != "tiempo,host,cpuP,cpuA\n":
        array = linea.strip().split(",")
        if mapa.get(array[0]) is None:
            host = {int(array[1])}
            cpuP = float(array[2])
            cpuA = float(array[3])
            value = [host, cpuP, cpuA]
            mapa.setdefault(array[0], value)
        else:
            data = mapa.get(array[0])
            host = data[0].add(int(array[1]))
            cpuP = float(array[2]) + data[1]
            cpuA = float(array[3]) + data[2]
            value = [host, cpuP, cpuA]
            mapa.setdefault(array[0], value)
file.close()
dicSalida = {}
for key in mapa:
    data = mapa.get(key)
    host = len(data[0])
    cpuP = data[1]
    cpuA = data[2]
    value = [host, cpuP, cpuA]
    dicSalida.setdefault(key, value)
fileSalida = open("cpuConsumo2LR.csv", "w")
fileSalida.write("tiempo;totalHost;cpuP;cpuA\n")
for key in dicSalida:
    data = dicSalida.get(key)
    linea = "{0};{1};{2};{3}\n".format(key,data[0], data[1], data[2])
    fileSalida.write(linea)
fileSalida.close()