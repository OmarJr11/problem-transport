def main():
    with open("/content/input.txt") as input:
        input = list(input.readlines())
    print(input)

    info = list()
    for i in input:
        cad = i.replace("\n", "")
        print(cad)
        info.append(cad)

    algoritmo = info[0]
    del info[0]
    A = list()
    b = list()
    c = list()
    variables = list()
    indexMayor = '0'
    isX = False
    pos = ''
    band = ''
    for i in info:
        if (band == 'A' and i != 'b' and i != 'variables' and i != 'c'):
            for j in i:
                if (isX):
                    pos += j
                if (j == 'x'):
                    isX = True
                if (j == ' '):
                    isX = False
                    indexMayor = (indexMayor, pos)[int(pos) > int(indexMayor)]
                    pos = ''
                isX = False
                indexMayor = (indexMayor, pos)[int(pos) > int(indexMayor)]
                pos = ''
                A.append(i.split(" "))
        elif (band == 'b' and i != 'A' and i != 'variables' and i != 'c'):
            b.append(int(i))
        elif (band == 'variables' and i != 'A' and i != 'b' and i != 'c'):
            variables.append(i.split(" "))
        elif (band == 'c' and i != 'A' and i != 'b' and i != 'variables'):
            for l in i.split(" "):
                c.append(int(l))
        if (i == 'A'):
            band = 'A'
        if (i == 'b'):
            band = 'b'
        if (i == 'c'):
            band = 'c'
        if (i == 'variables'):
            band = 'variables'

    print("A: ", A)
    print("b: ", b)
    print("c: ", c)
    print("variables: ", variables)

    for ai in range(int(indexMayor[0])):
        for aj in range(int(indexMayor[1])):
