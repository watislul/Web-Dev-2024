alert( extractCurrencyValue('$120') === 120 ); // true

function extractCurrencyValue(str) {
    return +str.slice(1);
}