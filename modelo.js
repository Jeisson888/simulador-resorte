function simularResorte(L0, k, m, c) {
    const dt = 0.01; // paso de tiempo (s)
    const g = 9.81; // aceleración de la gravedad (m/s²)

    // condiciones iniciales
    let t = 0.0; // tiempo inicial
    let x = L0;  // posicion inicial: resorte sin carga
    let v = 0.0; // velocidad inicial

    const resultados = []; // [tiempo, posicion]

    while (true) {
        // aceleracion
        const a = (m * g - k * (x - L0) - c * v) / m;

        // velocidad
        v = v + a * dt;
        // posicion
        const x_new = x + v * dt;

        t = t + dt;

        resultados.push([t, x_new]);

        if (Math.round(x_new * 1e8) === Math.round(x * 1e8)) {
            break;
        }

        x = x_new;
    }

    return resultados;
}

function calcularEquilibrio(L0, k, m) {
    const g = 9.81; // aceleración de la gravedad (m/s²)
    const xEquilibrioTeorico = L0 + (m * g) / k;
    return xEquilibrioTeorico;
}

module.exports = { simularResorte, calcularEquilibrio };
