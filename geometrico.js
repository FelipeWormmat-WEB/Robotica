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

async function calculateAngles(l1, l2, l3, phiDegrees, x, y) {
    return new Promise((resolve) => {
        let results = {};

        const phi = phiDegrees * (Math.PI / 180);
        console.log(`\nEtapa 1: Conversão do ângulo φ de graus para radianos`);
        console.log(`φ (graus): ${phiDegrees}°`);
        console.log(`φ (radianos): ${phi.toFixed(4)} rad\n`);

        setTimeout(() => {
            const xSquared = x ** 2;
            const ySquared = y ** 2;
            console.log(`Etapa 2: Calcular x² e y²`);
            console.log(`x² = ${xSquared.toFixed(4)}`);
            console.log(`y² = ${ySquared.toFixed(4)}\n`);
        }, 1000);

        setTimeout(() => {
            const xySum = x ** 2 + y ** 2;
            console.log(`Etapa 3: Soma dos quadrados x² + y²`);
            console.log(`x² + y² = ${xySum.toFixed(4)}\n`);
        }, 2000);

        setTimeout(() => {
            const xyRoot = Math.sqrt(x ** 2 + y ** 2);
            console.log(`Etapa 4: Raiz quadrada de x² + y²`);
            console.log(`√(x² + y²) = ${xyRoot.toFixed(4)}\n`);
        }, 3000);

        setTimeout(() => {
            const cosTheta1Part = (x ** 2 + y ** 2 + l1 ** 2 - l2 ** 2) / (2 * l1 * Math.sqrt(x ** 2 + y ** 2));
            console.log(`Etapa 5: Calcular a parte do cosseno para θ1`);
            console.log(`(x² + y² + l1² - l2²) / (2 * l1 * √(x² + y²)) = ${cosTheta1Part.toFixed(4)}\n`);
        }, 4000);

        setTimeout(() => {
            const theta1 = Math.atan2(y, x) + Math.acos((x ** 2 + y ** 2 + l1 ** 2 - l2 ** 2) / (2 * l1 * Math.sqrt(x ** 2 + y ** 2)));
            results.theta1 = theta1 * (180 / Math.PI);
            console.log(`Etapa 6: Calcular θ1`);
            console.log(`θ1 = ${(results.theta1).toFixed(2)}°\n`);
        }, 5000);

        setTimeout(() => {
            const theta1_ = Math.atan2(y, x) - Math.acos((x ** 2 + y ** 2 + l1 ** 2 - l2 ** 2) / (2 * l1 * Math.sqrt(x ** 2 + y ** 2)));
            results.theta1_ = theta1_ * (180 / Math.PI);
            console.log(`Etapa 7: Calcular θ1'`);
            console.log(`θ1' = ${(results.theta1_).toFixed(2)}°\n`);
        }, 6000);

        setTimeout(() => {
            const cosTheta2Part = (x ** 2 + y ** 2 - l1 ** 2 - l2 ** 2) / (2 * l1 * l2);
            console.log(`Etapa 8: Calcular a parte do cosseno para θ2`);
            console.log(`(x² + y² - l1² - l2²) / (2 * l1 * l2) = ${cosTheta2Part.toFixed(4)}\n`);
        }, 7000);

        setTimeout(() => {
            const theta2 = -Math.acos((x ** 2 + y ** 2 - l1 ** 2 - l2 ** 2) / (2 * l1 * l2));
            results.theta2 = theta2 * (180 / Math.PI);
            console.log(`Etapa 9: Calcular θ2`);
            console.log(`θ2 = ${(results.theta2).toFixed(2)}°\n`);
        }, 8000);

        setTimeout(() => {
            const theta2_ = Math.acos((x ** 2 + y ** 2 - l1 ** 2 - l2 ** 2) / (2 * l1 * l2));
            results.theta2_ = theta2_ * (180 / Math.PI);
            console.log(`Etapa 10: Calcular θ2'`);
            console.log(`θ2' = ${(results.theta2_).toFixed(2)}°\n`);
        }, 9000);

        setTimeout(() => {
            const theta3 = phiDegrees - (results.theta1 + results.theta2);
            results.theta3 = theta3;
            console.log(`Etapa 11: Calcular θ3`);
            console.log(`θ3 = φ - (θ1 + θ2) = ${(results.theta3).toFixed(2)}°\n`);
        }, 10000);

        setTimeout(() => {
            const theta3_ = phiDegrees - (results.theta1_ + results.theta2_);
            results.theta3_ = theta3_;
            console.log(`Etapa 12: Calcular θ3'`);
            console.log(`θ3' = φ - (θ1' + θ2') = ${(results.theta3_).toFixed(2)}°\n`);
        }, 11000);

        setTimeout(() => {
            resolve(results);
            console.log("\nCálculos concluídos.");
        }, 12000);
    });
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

        console.log(`\nCálculo de x e y com garra:`);
        console.log(`x = x' - L3 * cos(φ) = ${x.toFixed(4)}`);
        console.log(`y = y' - L3 * sin(φ) = ${y.toFixed(4)}\n`);
    } else {
        x = parseFloat(await askQuestion("Digite o valor de x: "));
        y = parseFloat(await askQuestion("Digite o valor de y: "));
    }

    console.log("\nValores recebidos:");
    console.log(`l1 = ${l1}, l2 = ${l2}, l3 = ${l3}, φ = ${phiDegrees}°, x = ${x}, y = ${y}\n`);

    const results = await calculateAngles(l1, l2, l3, phiDegrees, x, y);

    if (results) {
        console.log("\nResultados finais:");
        console.log(`Theta1: ${(results.theta1).toFixed(2)}°`);
        console.log(`Theta1': ${(results.theta1_).toFixed(2)}°`);
        console.log(`Theta2: ${(results.theta2).toFixed(2)}°`);
        console.log(`Theta2': ${(results.theta2_).toFixed(2)}°`);
        console.log(`Theta3: ${(results.theta3).toFixed(2)}°`);
        console.log(`Theta3': ${(results.theta3_).toFixed(2)}°`);
    }

    await askQuestion("Pressione Enter para fechar...");
}

main();
