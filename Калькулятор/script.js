document.getElementById('convertButton').addEventListener('click', function() {
    const numberInput = document.getElementById('numberInput').value.trim();
    const fromBase = parseInt(document.getElementById('fromBase').value);
    const toBase = parseInt(document.getElementById('toBase').value);
    
    if (!isValidInput(numberInput, fromBase)) {
        alert('Ошибка ввода. Проверьте число и систему счисления.');
        return;
    }

    try {
        // Конвертация в десятичную систему
        const decimalNumber = parseInt(numberInput, fromBase);
        // Конвертация из десятичной системы в нужную
        const convertedNumber = decimalNumber.toString(toBase).toUpperCase();
        
        document.getElementById('result').innerText = Результат: ${convertedNumber};
    } catch (error) {
        alert('Произошла ошибка при конвертации.');
    }
});

function isValidInput(number, base) {
    const validChars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'.slice(0, base);
    return [...number.toUpperCase()].every(char => validChars.includes(char));
}
