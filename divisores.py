from io import open
archivo_texto= open("Divisores.txt" , "a")

try:
    n = int(input("Ingrese un numero: "))
    archivo_texto.write("El numero ingresado fue: " + str(n) + " Y sus divisores son: ")
    for i in range (1,n+1):
        if n % i==0:
            print(i)
            archivo_texto.write(str(i) + ", ")
    archivo_texto.write("\n")
except ValueError as e:
    print("Caracter no permitido")

archivo_texto.close()
