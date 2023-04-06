function calculateNumber(type, a, b) {
  const numA = Number(a);
  const numB = Number(b);

  if (Number.isNaN(numA) || Number.isNaN(numB)) throw TypeError;

  if (type === 'SUM') {
    return (Math.round(numA) + Math.round(numB));
  } if (type === 'SUBTRACT') {
    return (Math.round(numA) - Math.round(numB));
  } if (type === 'DIVIDE') {
    if (Math.round(numB) === 0) {
      return ('Error');
    }
    return (Math.round(numA) / Math.round(numB));
  }
  throw TypeError;
}

module.exports = calculateNumber;
