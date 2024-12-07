'use strict';

const snakeEyesBtn = document.getElementById('snake-eyes-btn');
const hiloBtn = document.getElementById('hilo-btn');
const blackjackBtn = document.getElementById('blackjack-btn');
const horseRaceBtn = document.getElementById('horse-race-btn');
const betInput = document.getElementById('bet');
const guessInput = document.getElementById('guess');
const balanceSpan = document.getElementById('balance');
const gameResultDiv = document.getElementById('game-result');
const guessSection = document.getElementById('guess-section');

// Get initial balance from the backend
function getBalance() {
    fetch('http://localhost:4000/casino/menu', {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        balanceSpan.innerText = data.balance;
    })
    .catch(error => console.error('Error fetching balance:', error));
}

// Play Snake Eyes
snakeEyesBtn.addEventListener('click', () => {
    const bet = betInput.value;
    if (bet <= 0) return alert('Please enter a valid bet.');

    fetch('http://localhost:4000/casino/snake-eyes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ bet: bet })
    })
    .then(response => response.json())
    .then(data => {
        gameResultDiv.innerHTML = `${data.message}. Your rolls: ${data.rolls.join(', ')}. Winnings: ${data.winnings} EUR.`;
        balanceSpan.innerText = data.balance;
    })
    .catch(error => console.error('Error playing Snake Eyes:', error));
});

// Play Hi-Lo
hiloBtn.addEventListener('click', () => {
    const bet = betInput.value;
    const guess = guessInput.value.toUpperCase();
    if (bet <= 0 || (guess !== 'HI' && guess !== 'LO')) return alert('Please enter a valid bet and guess.');

    fetch('http://localhost:4000/casino/hilo', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ bet: bet, guess: guess })
    })
    .then(response => response.json())
    .then(data => {
        gameResultDiv.innerHTML = `${data.message}. First card: ${data.first_card}, Second card: ${data.second_card}. Winnings: ${data.winnings} EUR.`;
        balanceSpan.innerText = data.balance;
    })
    .catch(error => console.error('Error playing Hi-Lo:', error));
});

// Play Horse Race
horseRaceBtn.addEventListener('click', () => {
    const bet = betInput.value;
    const horse = prompt("Enter your bet horse (Diddy, Kolovastaava, Sakke, Rinne, Uusitalo):");
    if (bet <= 0 || !horse) return alert('Please enter a valid bet and select a horse.');

    fetch('http://localhost:4000/casino/horse_race', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ bet: bet, horse: horse })
    })
    .then(response => response.json())
    .then(data => {
        gameResultDiv.innerHTML = `${data.result} Race results: ${JSON.stringify(data.race_results)}. Odds: ${JSON.stringify(data.odds)}.`;
        balanceSpan.innerText = data.player_balance;
    })
    .catch(error => console.error('Error playing Horse Race:', error));
});

// Initialize the balance on page load
window.onload = getBalance;