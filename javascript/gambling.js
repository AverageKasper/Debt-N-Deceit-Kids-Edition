'use strict';

const balanceSpan = document.getElementById('balance');
const betInput = document.getElementById('bet');
const gameResultDiv = document.getElementById('game-result');
const gameContainers = document.querySelectorAll('.game-container');

// Fetch initial balance from the backend
async function getBalance() {
    await fetch('http://localhost:4000/casino/menu', {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' }
    })
    .then(response => response.json())
    .then(data => {
        if (data.balance !== undefined) {
            balanceSpan.textContent = data.balance;
        } else {
            gameResultDiv.textContent = data.message || 'Error fetching games.';
        }
    })
    .catch(error => {
        console.error('Error fetching balance:', error);
        balanceSpan.textContent = 'Error';
    });
}

// Show a specific game and hide others
function showGame(gameId) {
    gameContainers.forEach(container => {
        if (container.id === gameId) {
            container.classList.add('active');
        } else {
            container.classList.remove('active');
        }
    });
}

// Function to handle bets
function placeBet(gameId, extraData = {}) {
    const betAmount = parseFloat(betInput.value);

    if (isNaN(betAmount) || betAmount <= 0) {
        alert('Please enter a valid bet amount.');
        return;
    }

    const requestBody = { bet: betAmount, ...extraData };

    fetch(`http://localhost:4000/casino/${gameId}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(requestBody)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            balanceSpan.textContent = data.balance || data.player_balance;
            gameResultDiv.textContent = data.message || 'Game completed.';
            if (data.race_results) {
                console.log('Race Results:', data.race_results);
            }
        }
    })
    .catch(error => {
        console.error(`Error playing ${gameId}:`, error);
        alert('An error occurred while playing the game.');
    });
}

// Initialize Snake Eyes logic
function initSnakeEyes() {
    document.getElementById('snake-eyes-container').innerHTML = `
        <button id="snake-eyes-play">Roll Dice</button>
        <div id="snake-eyes-result"></div>
    `;

    document.getElementById('snake-eyes-play').onclick = () => {
        placeBet('snake-eyes');
    };
}

// Initialize Hi-Lo logic
function initHiLo() {
    document.getElementById('hilo-container').innerHTML = `
        <button id="hilo-hi">Guess Hi</button>
        <button id="hilo-lo">Guess Lo</button>
        <div id="hilo-result"></div>
    `;

    document.getElementById('hilo-hi').onclick = () => {
        placeBet('hilo', { guess: 'HI' });
    };

    document.getElementById('hilo-lo').onclick = () => {
        placeBet('hilo', { guess: 'LO' });
    };
}

// Initialize Horse Race logic
function initHorseRace() {
    document.getElementById('horse-race-container').innerHTML = `
        <select id="horse-select">
            <option value="Diddy">Diddy</option>
            <option value="Kolovastaava">Kolovastaava</option>
            <option value="Sakke">Sakke</option>
            <option value="Rinne">Rinne</option>
            <option value="Uusitalo">Uusitalo</option>
        </select>
        <button id="horse-race-play">Start Race</button>
        <div id="horse-race-result"></div>
    `;

    document.getElementById('horse-race-play').onclick = () => {
        const selectedHorse = document.getElementById('horse-select').value;
        placeBet('horse_race', { horse: selectedHorse });
    };
}

// Initialize Blackjack logic
function initBlackjack() {
    document.getElementById('blackjack-container').innerHTML = `
        <button id="blackjack-start">Start Blackjack</button>
        <div id="blackjack-result"></div>
        <div id="blackjack-actions" style="display: none;">
            <button id="blackjack-hit">Hit</button>
            <button id="blackjack-stand">Stand</button>
        </div>
    `;

    const blackjackResult = document.getElementById('blackjack-result');
    const blackjackActions = document.getElementById('blackjack-actions');

    document.getElementById('blackjack-start').onclick = () => {
        const betAmount = parseFloat(document.getElementById('bet').value);

        if (isNaN(betAmount) || betAmount <= 0) {
            alert('Please enter a valid bet amount.');
            return;
        }

        fetch('http://localhost:4000/casino/blackjack/start', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ bet: betAmount })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                console.log("Start Response:", data);  // Debug response
                blackjackResult.innerHTML = `
                    <p>Your hand: ${data.player_hand.join(', ')}</p>
                    <p>Dealer's hand: ${data.dealer_hand.join(', ')}</p>
                `;
                blackjackActions.style.display = 'block';
                blackjackActions.dataset.gameId = data.game_id;
            }
        })
        .catch(error => console.error('Error starting Blackjack:', error));
    };

    document.getElementById('blackjack-hit').onclick = () => {
        const gameId = blackjackActions.dataset.gameId;
        console.log("Game ID:", blackjackActions.dataset.gameId); // Add this to the Hit and Stand button click handlers

        fetch('http://localhost:4000/casino/blackjack/play', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ game_id: gameId, action: 'hit' })
        })
        .then(response => response.json())
        .then(data => {
            console.log("Hit Response:", data);  // Debug response
            blackjackResult.innerHTML = `
                <p>Your hand: ${data.player_hand.join(', ')}</p>
                <p>Dealer's hand: ${data.dealer_hand.join(', ')}</p>
                <p>${data.result || data.message}</p>
            `;
            if (data.finished) blackjackActions.style.display = 'none';
        })
        .catch(error => console.error('Error hitting in Blackjack:', error));
    };

    document.getElementById('blackjack-stand').onclick = () => {
        const gameId = blackjackActions.dataset.gameId;
        console.log("Game ID:", blackjackActions.dataset.gameId); // Add this to the Hit and Stand button click handlers

        fetch('http://localhost:4000/casino/blackjack/play', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ game_id: gameId, action: 'stand' })
        })
        .then(response => response.json())
        .then(data => {
            console.log("Stand Response:", data);  // Debug response
            blackjackResult.innerHTML = `
                <p>Your hand: ${data.player_hand.join(', ')}</p>
                <p>Dealer's hand: ${data.dealer_hand.join(', ')}</p>
                <p>${data.result}</p>
            `;
            blackjackActions.style.display = 'none';
        })
        .catch(error => console.error('Error standing in Blackjack:', error));
    };
}


// Initialize balance on page load
getBalance();

// Initialize games based on selected game
document.querySelector('button[onclick*="snake-eyes"]').onclick = () => {
    showGame('snake-eyes');
    initSnakeEyes();
};

document.querySelector('button[onclick*="hilo"]').onclick = () => {
    showGame('hilo');
    initHiLo();
};

document.querySelector('button[onclick*="horse-race"]').onclick = () => {
    showGame('horse-race');
    initHorseRace();
};

document.querySelector('button[onclick*="blackjack"]').onclick = () => {
    showGame('blackjack');
    initBlackjack();
};
