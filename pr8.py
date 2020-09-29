"""Se introduc de la tastatură trei cifre. Afişaţi pe aceeaşi linie 5 numere formate cu
aceste cifre luate o singură dată. """
a=int(input("Introduceti 1 nr:"))
b=int(input('Introduceti 2 nr:'))
c=int(input("Introduceti 3 nr:"))
print(str(a)+str(b)+str(c), str(b)+str(c)+str(a), str(c)+str(b)+str(a), str(b)+str(a)+str(c), str(a)+str(c)+str(b))