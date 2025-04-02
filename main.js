const { simularResorte, calcularEquilibrio } = require('./modelo');
const readline = require('readline');

function main() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question("Ingrese la longitud sin carga del resorte (m): ", (L0Input) => {
        rl.question("Ingrese la constante del resorte (N/m): ", (kInput) => {
            rl.question("Ingrese la masa (kg): ", (mInput) => {
                rl.question("Ingrese el coeficiente de amortiguamiento (N·s/m): ", (cInput) => {
                    const L0 = parseFloat(L0Input);
                    const k = parseFloat(kInput);
                    const m = parseFloat(mInput);
                    const c = parseFloat(cInput);

                    if (isNaN(L0) || isNaN(k) || isNaN(m) || isNaN(c)) {
                        console.log("Error: Por favor ingrese valores numéricos válidos.");
                        rl.close();
                        return;
                    }

                    const resultados = simularResorte(L0, k, m, c);

                    console.log("\nTiempo (s)\tPosición (m)");
                    resultados.forEach(([t, x]) => {
                        console.log(`${t.toFixed(2)}\t\t${x.toFixed(4)}`);
                    });

                    const xEquilibrioTeorico = calcularEquilibrio(L0, k, m);
                    console.log(`\nPunto de equilibrio teórico (m): ${xEquilibrioTeorico.toFixed(4)}`);
                    console.log(`Punto de equilibrio simulación (m): ${resultados[resultados.length - 1][1].toFixed(4)}`);

                    rl.close();
                });
            });
        });
    });
}

main();

// datos de prueba
// L0 = 0.5
// k = 50
// m = 1
// c = 1