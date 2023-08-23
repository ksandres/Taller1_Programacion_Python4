a = float(input())
b = float(input())
c = float(input())

if a == b and b == c and a == c:
    print("El triángulo es equilátero")
elif (a == b and b != c) or (a != b and b == c) or (a == c and b != c):
    print("El triángulo es isósceles")
elif a != b and b != c and a != c:
    print("El triángulo es escaleno")
else:
    print("No es un triángulo válido")