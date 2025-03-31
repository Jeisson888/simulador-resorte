def simular_resorte(L0, k, m, c):    
    dt = 0.01 # paso de tiempo (s)
    g = 9.81 # aceleración de la gravedad (m/s²)

    # condiciones iniciales
    t = 0.0 # tiempo inicial
    x = L0   # posicion inicial: resorte sin carga
    v = 0.0  # velocidad inicial

    resultados = []  # [tiempo, posicion]
    
    while True:
        # aceleracion
        a = (m * g - k * (x - L0) - c * v) / m
        
        # velocidad
        v = v + a * dt
        # posicion
        x_new = x + v * dt

        t = t + dt
        
        resultados.append((t, x_new))
        
        if round(x_new, 8) == round(x, 8):
            break
        
        x = x_new

    return resultados

def calcular_equilibrio(L0, k, m):
    g = 9.81  # aceleración de la gravedad (m/s²)
    x_equilibrio_teorico = L0 + (m * g) / k
    return x_equilibrio_teorico
