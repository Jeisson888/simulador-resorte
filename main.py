from modelo import simular_resorte

def main():
    try:
        L0 = float(input("Ingrese la longitud sin carga del resorte (m): "))
        k = float(input("Ingrese la constante del resorte (N/m): "))
        m = float(input("Ingrese la masa (kg): "))
        c = float(input("Ingrese el coeficiente de amortiguamiento (N·s/m): "))
    except ValueError:
        print("Error: Por favor ingrese valores numericos validos.")
        return

    simular_resorte(L0, k, m, c)

if __name__ == '__main__':
    main()

# datos de prueba
# L0 = 0.5
# k = 50
# m = 1
# c = 1
