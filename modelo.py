def simular_resorte(L0, k, m, c):
    print("Simulacion de un resorte\n")
    
    dt = 0.01 # paso de tiempo (s)
    g = 9.81 # aceleración de la gravedad (m/s²)

    # condiciones iniciales
    t = 0.0 # tiempo inicial
    x = L0   # posicion inicial: resorte sin carga
    v = 0.0  # velocidad inicial

    print("\nTiempo (s)\tPosicion (m)\tVelocidad (m/s)\tAceleracion (m/s²)")
    
    while True:
        a = (m * g - k * (x - L0) - c * v) / m
        
        v = v + a * dt
        x_new = x + v * dt
        t = t + dt
        
        print("{:.2f}\t\t{:.4f}\t\t{:.4f}\t\t{:.4f}".format(t, x_new, v, a))
        
        if round(x_new, 8) == round(x, 8):
            break
        
        x = x_new

    x_equilibrio_teorico = L0 + (m * g) / k
    print("\nPunto de equilibrio teorico (m): {:.4f}".format(x_equilibrio_teorico))
    print("Punto de equilibrio simulacion (m): {:.4f}".format(x_new))
