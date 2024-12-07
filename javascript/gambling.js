'use strict';

// Button elements
const snakeEyesBtn = document.getElementById('snake-eyes-btn');
const hiloBtn = document.getElementById('hilo-btn');
const horseRaceBtn = document.getElementById('horse-race-btn');
const startBlackjackBtn = document.getElementById('start-blackjack-btn');
const hitBtn = document.getElementById('hitBtn');
const standBtn = document.getElementById('standBtn');
const balanceSpan = document.getElementById('balance');
const betInput = document.getElementById('bet');
const gameResultDiv = document.getElementById('game-result');

// Fetch initial balance from the backend
function getBalance() {
    fetch('http://localhost:4000/casino/menu', {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        balanceSpan.textContent = data.balance;
    })
    .catch(error => {
        console.error('Error fetching balance:', error);
        balanceSpan.textContent = 'Error';
    });
}

// Helper to handle bets
function placeBet(game) {
    const betAmount = parseFloat(betInput.value);

    if (isNaN(betAmount) || betAmount <= 0) {
        alert('Please enter a valid bet amount.');
        return;
    }

    fetch(`http://localhost:4000/casino/${game}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ bet: betAmount })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            balanceSpan.textContent = data.new_balance;
            gameResultDiv.textContent = data.message;
        } else {
            alert(data.error || 'Something went wrong!');
        }
    })
    .catch(error => {
        console.error('Error placing bet:', error);
        alert('An error occurred while placing the bet.');
    });
}

// Event listeners for game buttons
snakeEyesBtn.addEventListener('click', () => placeBet('snake-eyes'));
hiloBtn.addEventListener('click', () => placeBet('hilo'));
horseRaceBtn.addEventListener('click', () => placeBet('horse-race'));

startBlackjackBtn.addEventListener('click', () => {
    fetch('http://localhost:4000/casino/blackjack/start', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            gameResultDiv.textContent = 'Blackjack started. Your move!';
            hitBtn.style.display = 'inline';
            standBtn.style.display = 'inline';
        } else {
            alert(data.error || 'Could not start Blackjack.');
        }
    })
    .catch(error => {
        console.error('Error starting Blackjack:', error);
        alert('An error occurred while starting Blackjack.');
    });
});

hitBtn.addEventListener('click', () => {
    fetch('http://localhost:4000/casino/blackjack/hit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            gameResultDiv.textContent = data.message;
            if (data.game_over) {
                hitBtn.style.display = 'none';
                standBtn.style.display = 'none';
            }
        } else {
            alert(data.error || 'Error during Blackjack move.');
        }
    })
    .catch(error => {
        console.error('Error hitting in Blackjack:', error);
    });
});

standBtn.addEventListener('click', () => {
    fetch('http://localhost:4000/casino/blackjack/stand', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            gameResultDiv.textContent = data.message;
            hitBtn.style.display = 'none';
            standBtn.style.display = 'none';
        } else {
            alert(data.error || 'Error during Blackjack move.');
        }
    })
    .catch(error => {
        console.error('Error standing in Blackjack:', error);
    });
});

// Initialize balance on page load
getBalance();
