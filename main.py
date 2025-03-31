from modelo import simular_resorte, calcular_equilibrio

def main():
    try:
        L0 = float(input("Ingrese la longitud sin carga del resorte (m): "))
        k = float(input("Ingrese la constante del resorte (N/m): "))
        m = float(input("Ingrese la masa (kg): "))
        c = float(input("Ingrese el coeficiente de amortiguamiento (N·s/m): "))
    except ValueError:
        print("Error: Por favor ingrese valores numericos validos.")
        return

    resultados = simular_resorte(L0, k, m, c)

    print("\nTiempo (s)\tPosicion (m)")
    for t, x in resultados:
        print("{:.2f}\t\t{:.4f}".format(t, x))

    x_equilibrio_teorico = calcular_equilibrio(L0, k, m)
    print("\nPunto de equilibrio teorico (m): {:.4f}".format(x_equilibrio_teorico))
    print("Punto de equilibrio simulacion (m): {:.4f}".format(resultados[-1][1]))

if __name__ == '__main__':
    main()

# datos de prueba
# L0 = 0.5
# k = 50
# m = 1
# c = 1
