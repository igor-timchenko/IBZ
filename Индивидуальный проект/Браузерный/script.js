let randomNumber;
let attempts = 0;

document.getElementById('difficulty').addEventListener('change', function() {
   const max = parseInt(this.value);
   randomNumber = Math.floor(Math.random() * max) + 1;
   attempts = 0;
   document.getElementById('result').textContent = '';
});

document.getElementById('submit').addEventListener('click', function() {
   const guess = parseInt(document.getElementById('guess').value);
   attempts++;
   if (guess === randomNumber) {
      document.getElementById('result').textContent = Поздравляем! Вы угадали число ${randomNumber} за ${attempts} попыток.;
   } else if (guess < randomNumber) {
      document.getElementById('result').textContent = 'Слишком маленькое число!';
   } else {
      document.getElementById('result').textContent = 'Слишком большое число!';
   }
});
