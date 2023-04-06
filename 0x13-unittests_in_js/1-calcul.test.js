const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {
    describe('when type is SUM', function() {
        it('should return the sum of two rounded numbers', function() {
            assert.equal(calculateNumber('SUM', 2.6, 3.8), 7);
            assert.equal(calculateNumber('SUM', 2.4, 3.1), 6);
            assert.equal(calculateNumber('SUM', 5.5, 4.2), 10);
            assert.equal(calculateNumber('SUM', 7.9, 1.1), 9);
        });
    });

    describe('when type is SUBTRACT', function() {
        it('should return the difference between two rounded numbers', function() {
            assert.equal(calculateNumber('SUBTRACT', 5.5, 4.2), 1);
            assert.equal(calculateNumber('SUBTRACT', 7.9, 1.1), 7);
            assert.equal(calculateNumber('SUBTRACT', 3.5, 3.1), 0);
        });
    });

    describe('when type is DIVIDE', function() {
        it('should return the rounded quotient of two rounded numbers', function() {
            assert.equal(calculateNumber('DIVIDE', 5.5, 4.2), 1);
            assert.equal(calculateNumber('DIVIDE', 7.9, 1.1), 7);
            assert.equal(calculateNumber('DIVIDE', 3.5, 3.1), 1);
            assert.equal(calculateNumber('DIVIDE', 3.5, 0), 'Error');
        });
    });

    describe('when type is invalid', function() {
        it('should return Error', function() {
            assert.equal(calculateNumber('INVALID', 2.6, 3.8), 'Error');
        });
    });
});