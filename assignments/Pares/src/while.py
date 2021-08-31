def main():
    #escribe tu código abajo de esta línea
    c=0
    s=0

    while (s < 1000):
        n=int(input("Dame un numero: "))
        s=s+n
        c=c+1

    print(f"Suma= {s}")
    print(f"Cantidad de números= {c}")

if __name__=='__main__':
    main()
