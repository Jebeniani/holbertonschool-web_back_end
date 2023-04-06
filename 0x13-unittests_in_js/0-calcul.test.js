/* eslint-disable no-restricted-globals */
/* eslint-disable jest/expect-expect */
/* eslint-disable jest/prefer-expect-assertions */
/* eslint-disable indent */
const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
    // eslint-disable-next-line jest/prefer-expect-assertions, jest/expect-expect
    it('checks the output', () => {
        assert.strictEqual(calculateNumber(1, 3), 4);
        assert.strictEqual(calculateNumber(1, 3.7), 5);
        assert.strictEqual(calculateNumber(1.2, 3.7), 5);
        assert.strictEqual(calculateNumber(1.5, 3.7), 6);
        assert.strictEqual(calculateNumber(3.7, 1), 5);
        assert.strictEqual(calculateNumber(3.7, 1.2), 5);
    });
    it('negative numbers', () => {
        assert.strictEqual(calculateNumber(-1, 1), 0);
        assert.strictEqual(calculateNumber(1, -1), 0);
        assert.strictEqual(calculateNumber(-1, -1), -2);
        // eslint-disable-next-line indent
        // eslint-disable-next-line indent
    });
    it('checks arguments', () => {
        assert.strictEqual(isNaN(calculateNumber(1)), true);
        assert.strictEqual(isNaN(calculateNumber()), true);
        // eslint-disable-next-line indent
    });
});
