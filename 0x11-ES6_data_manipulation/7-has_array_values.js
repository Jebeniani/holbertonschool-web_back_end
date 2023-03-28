export default function hasValuesFromArray(set, array) {
  // eslint-disable-next-line no-plusplus
  for (let i = 0; i < array.length; i++) {
    if (!set.has(array[i])) {
      return false;
    }
  }
  return true;
}
