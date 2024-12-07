'use strict';

const snakeEyesBtn = document.getElementById('snake-eyes-btn');
const hiloBtn = document.getElementById('hilo-btn');
const startBlackjackBtn = document.getElementById('start-blackjack-btn');
const hitBtn = document.getElementById('hitBtn');
const standBtn = document.getElementById('standBtn');
const blackjackStatus = document.getElementById('blackjack-status');
let blackjackGameId=null;
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
    guessSection.style.display='none';
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
    guessSection.style.display='block';
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
    guessSection.style.display='none';
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

// Play Black Jack
startBlackjackBtn.addEventListener('click', () => {
    const bet = betInput.value;
    if (bet <= 0) return alert('Please enter a valid bet.');

    fetch('http://localhost:4000/casino/blackjack/start', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ bet: bet })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) return alert(data.error);

        blackjackGameId = data.game_id;
        blackjackStatus.innerHTML = `
            <p>Game started! Your hand: ${data.player_hand.join(', ')}</p>
            <p>Dealer's hand: ${data.dealer_hand[0]}, Hidden</p>
            <p>Your hand value: ${data.player_value}</p>
        `;
        hitBtn.style.display = 'inline-block';
        standBtn.style.display = 'inline-block';
    })
    .catch(error => console.error('Error starting Blackjack:', error));
});

hitBtn.addEventListener('click', () => {
    if (!blackjackGameId) return alert('Start a game first.');

    fetch('http://localhost:4000/casino/blackjack/play', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ game_id: blackjackGameId, action: 'hit' })
    })
    .then(response => response.json())
    .then(data => {
        if (data.result) { // Game finished
            blackjackStatus.innerHTML = `
                <p>${data.result}</p>
                <p>Your hand: ${data.player_hand.join(', ')}</p>
                <p>Balance: ${data.balance} EUR</p>
            `;
            hitBtn.style.display = 'none';
            standBtn.style.display = 'none';
        } else {
            blackjackStatus.innerHTML = `
                <p>Your hand: ${data.player_hand.join(', ')}</p>
                <p>Your hand value: ${data.player_value}</p>
                <p>Your move: hit or stand.</p>
            `;
        }
    })
    .catch(error => console.error('Error during hit:', error));
});

standBtn.addEventListener('click', () => {
    if (!blackjackGameId) return alert('Start a game first.');

    fetch('http://localhost:4000/casino/blackjack/play', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ game_id: blackjackGameId, action: 'stand' })
    })
    .then(response => response.json())
    .then(data => {
        blackjackStatus.innerHTML = `
            <p>${data.result}</p>
            <p>Your hand: ${data.player_hand.join(', ')}</p>
            <p>Dealer's hand: ${data.dealer_hand.join(', ')}</p>
            <p>Your hand value: ${data.player_value}</p>
            <p>Dealer's hand value: ${data.dealer_value}</p>
            <p>Balance: ${data.balance} EUR</p>
        `;
        hitBtn.style.display = 'none';
        standBtn.style.display = 'none';
    })
    .catch(error => console.error('Error during stand:', error));
});


// Initialize the balance on page load
window.onload = getBalance;