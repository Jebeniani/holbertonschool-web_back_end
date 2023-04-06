function calculateNumber(type, a, b) {
    const roundedA = Math.round(a);
    const roundedB = Math.round(b);

    switch (type) {
        case 'SUM':
            return roundedA + roundedB;
        case 'SUBTRACT':
            return roundedA - roundedB;
        case 'DIVIDE':
            if (roundedB === 0) {
                return 'Error';
            }
            return Math.round(roundedA / roundedB);
        default:
            return 'Error';
    }
}

module.exports = calculateNumber;