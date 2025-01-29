let secretNumber;
let attempts = 0;

document.getElementById('startButton').onclick = function() {
    const difficulty = document.getElementById('difficulty').value;
    switch (difficulty) {
        case 'easy':
            secretNumber = Math.floor(Math.random() * 10) + 1;
            break;
        case 'medium':
            secretNumber = Math.floor(Math.random() * 50) + 1;
            break;
        case 'hard':
            secretNumber = Math.floor(Math.random() * 100) + 1;
            break;
    }
    
    attempts = 0;
    document.getElementById('game').style.display = 'block';
    document.getElementById('message').textContent = '';
};

document.getElementById('guessButton').onclick = function() {
    const guess = Number(document.getElementById('guessInput').value);
    attempts++;
    
    if (guess === secretNumber) {
        document.getElementById('message').textContent = Поздравляем! Вы угадали число ${secretNumber} за ${attempts} попыток.;
        document.getElementById('guessInput').value = '';
        document.getElementById('game').style.display = 'none';
    } else if (guess < secretNumber) {
        document.getElementById('message').textContent = 'Слишком низкое число!';
    } else {
        document.getElementById('message').textContent = 'Слишком высокое число!';
    }
};
