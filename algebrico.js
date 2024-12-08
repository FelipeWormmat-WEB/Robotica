const readline = require("readline");

function askQuestion(query) {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout,
    });

    return new Promise((resolve) => rl.question(query, (ans) => {
        rl.close();
        resolve(ans);
    }));
}

async function main() {
    const l1 = parseFloat(await askQuestion("Digite o valor de l1: "));
    const l2 = parseFloat(await askQuestion("Digite o valor de l2: "));
    const l3 = parseFloat(await askQuestion("Digite o valor de l3: "));
    const phiDegrees = parseFloat(await askQuestion("Digite o valor de φ (em graus): "));
    const hasClaw = (await askQuestion("A estrutura tem garra? (sim/não): ")).toLowerCase() === "sim";

    let x, y;

    if (hasClaw) {
        const xPrime = parseFloat(await askQuestion("Digite o valor de x': "));
        const yPrime = parseFloat(await askQuestion("Digite o valor de y': "));
        x = xPrime - l3 * Math.cos(phiDegrees * (Math.PI / 180));
        y = yPrime - l3 * Math.sin(phiDegrees * (Math.PI / 180));
    } else {
        x = parseFloat(await askQuestion("Digite o valor de x: "));
        y = parseFloat(await askQuestion("Digite o valor de y: "));
    }

    const results = {};

    console.log("\nEtapa 1: Conversão do ângulo φ de graus para radianos");
    const phi = phiDegrees * (Math.PI / 180);
    console.log(`φ (graus): ${phiDegrees}°`);
    console.log(`φ (radianos): ${phi.toFixed(4)} rad\n`);

    setTimeout(() => {
        console.log("Etapa 2: Calcular x² e y²");
        const xSquared = x ** 2;
        const ySquared = y ** 2;
        const xySum = xSquared + ySquared;
        const xyRoot = Math.sqrt(xySum);

        console.log(`x² = ${xSquared.toFixed(4)}`);
        console.log(`y² = ${ySquared.toFixed(4)}`);
        console.log(`x² + y² = ${xySum.toFixed(4)}`);
        console.log(`√(x² + y²) = ${xyRoot.toFixed(4)}\n`);

        setTimeout(() => {
            console.log("Etapa 3: Calcular θ1");
            const cosTheta1Part = (xySum + l1 ** 2 - l2 ** 2) / (2 * l1 * xyRoot);
            if (cosTheta1Part >= -1 && cosTheta1Part <= 1) {
                const theta1 = Math.atan2(y, x) + Math.acos(cosTheta1Part);
                const theta1_ = Math.atan2(y, x) - Math.acos(cosTheta1Part);

                results.theta1 = theta1 * (180 / Math.PI);
                results.theta1_ = theta1_ * (180 / Math.PI);

                console.log(`θ1 = ${(results.theta1).toFixed(2)}°`);
                console.log(`θ1' = ${(results.theta1_).toFixed(2)}°\n`);
            } else {
                console.error("Erro: o valor do cosseno para θ1 está fora do intervalo [-1, 1].");
            }

            setTimeout(() => {
                console.log("Etapa 4: Calcular θ2");
                const cosTheta2Part = (xySum - l1 ** 2 - l2 ** 2) / (2 * l1 * l2);
                if (cosTheta2Part >= -1 && cosTheta2Part <= 1) {
                    const theta2 = -Math.acos(cosTheta2Part);
                    const theta2_ = Math.acos(cosTheta2Part);

                    results.theta2 = theta2 * (180 / Math.PI);
                    results.theta2_ = theta2_ * (180 / Math.PI);

                    console.log(`θ2 = ${(results.theta2).toFixed(2)}°`);
                    console.log(`θ2' = ${(results.theta2_).toFixed(2)}°\n`);
                } else {
                    console.error("Erro: o valor do cosseno para θ2 está fora do intervalo [-1, 1].");
                }

                setTimeout(() => {
                    console.log("Etapa 5: Calcular θ3");
                    if (results.theta1 !== undefined && results.theta2 !== undefined) {
                        results.theta3 = phiDegrees - (results.theta1 + results.theta2);
                        results.theta3_ = phiDegrees - (results.theta1_ + results.theta2_);

                        console.log(`θ3 = φ - (θ1 + θ2) = ${(results.theta3).toFixed(2)}°`);
                        console.log(`θ3' = φ - (θ1' + θ2') = ${(results.theta3_).toFixed(2)}°\n`);

                        console.log("Resultados finais:");
                        console.log(`Theta1: ${(results.theta1).toFixed(2)}°`);
                        console.log(`Theta1': ${(results.theta1_).toFixed(2)}°`);
                        console.log(`Theta2: ${(results.theta2).toFixed(2)}°`);
                        console.log(`Theta2': ${(results.theta2_).toFixed(2)}°`);
                        console.log(`Theta3: ${(results.theta3).toFixed(2)}°`);
                        console.log(`Theta3': ${(results.theta3_).toFixed(2)}°`);
                    } else {
                        console.error("Erro: Não foi possível calcular θ3 devido a valores indefinidos.");
                    }
                }, 2000);
            }, 2000);
        }, 2000);
    }, 2000);
}

main();
