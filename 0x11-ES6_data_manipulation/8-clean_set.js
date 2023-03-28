export default function cleanSet(set, startString) {
  if (startString === undefined) {
    return '';
  }

  const filteredValues = Array.from(set).filter((value) => typeof value === 'string' && value.startsWith(startString));

  const cleanedValues = filteredValues.map((value) => value.slice(startString.length));

  return cleanedValues.join('-');
}
