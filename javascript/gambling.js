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
        const betAmount = parseFloat(document.getElementById('bet').value);
        const resultDiv = document.getElementById('snake-eyes-result');
        const balanceSpan = document.getElementById('balance'); // Ensure this ID exists

        if (isNaN(betAmount) || betAmount <= 0) {
            alert('Please enter a valid bet amount.');
            return;
        }

        fetch('http://localhost:4000/casino/snake-eyes', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ bet: betAmount })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                resultDiv.innerHTML = `<p>Error: ${data.error}</p>`;
            } else {
                resultDiv.innerHTML = `
                    <p>${data.message}</p>
                    <p>Dice Rolls: ${data.dice_rolls.join(', ')}</p>
                    <p>Your Balance: ${data.balance}€</p>
                `;

                // Update balance on the page
                balanceSpan.textContent = data.balance;
            }
        })
        .catch(error => {
            console.error('Error in Snake Eyes:', error);
            alert('An error occurred while playing Snake Eyes.');
        });
    };
}

// Initialize Hi-Lo logic
function initHiLo() {
    document.getElementById('hilo-container').innerHTML = `
        <button id="hilo-start">Start Game</button>
        <div id="hilo-first-card" style="display: none;"></div>
        <div id="hilo-guess" style="display: none;">
            <button id="hilo-hi">Guess Hi</button>
            <button id="hilo-lo">Guess Lo</button>
        </div>
        <div id="hilo-result"></div>
    `;

    const firstCardDiv = document.getElementById('hilo-first-card');
    const guessDiv = document.getElementById('hilo-guess');
    const resultDiv = document.getElementById('hilo-result');
    const balanceSpan = document.getElementById('balance'); // Ensure this ID exists

    document.getElementById('hilo-start').onclick = () => {
        const betAmount = parseFloat(document.getElementById('bet').value);

        if (isNaN(betAmount) || betAmount <= 0) {
            alert('Please enter a valid bet amount.');
            return;
        }

        fetch('http://localhost:4000/casino/hilo/start', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ bet: betAmount })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                resultDiv.innerHTML = `<p>Error: ${data.error}</p>`;
            } else {
                // Show the first card and enable guessing
                firstCardDiv.style.display = 'block';
                firstCardDiv.innerHTML = `<p>The first card is ${data.first_card}. Make your guess!</p>`;
                guessDiv.style.display = 'block';
                resultDiv.innerHTML = '';
                window.hiloState = { first_card: data.first_card, bet: betAmount }; // Store game state
            }
        })
        .catch(error => {
            console.error('Error starting Hi-Lo:', error);
            resultDiv.innerHTML = '<p>An error occurred while starting the game.</p>';
        });
    };

    document.getElementById('hilo-hi').onclick = () => makeHiLoGuess('HI');
    document.getElementById('hilo-lo').onclick = () => makeHiLoGuess('LO');

    function makeHiLoGuess(guess) {
        if (!window.hiloState || !window.hiloState.first_card) {
            alert('No active game. Start a new game first.');
            return;
        }

        fetch('http://localhost:4000/casino/hilo/guess', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ ...window.hiloState, guess: guess })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                resultDiv.innerHTML = `<p>Error: ${data.error}</p>`;
            } else {
                resultDiv.innerHTML = `
                    <p>${data.message}</p>
                    <p>Your Balance: ${data.balance}€</p>
                `;
                firstCardDiv.style.display = 'none';
                guessDiv.style.display = 'none';
                balanceSpan.textContent = data.balance; // Update the balance
                window.hiloState = {}; // Clear game state
            }
        })
        .catch(error => {
            console.error('Error making Hi-Lo guess:', error);
            resultDiv.innerHTML = '<p>An error occurred while making your guess.</p>';
        });
    }
}


// Initialize Horse Race logic
function initHorseRace() {
    document.getElementById('horse-race-container').innerHTML = `
        <button id="horse-race-start">Start Horse Race</button>
        <div id="horse-race-odds" style="display: none;">
            <h4>Odds:</h4>
            <ul id="horse-odds-list"></ul>
        </div>
        <div id="horse-selection" style="display: none;">
            <label for="horse-select">Choose a Horse:</label>
            <select id="horse-select"></select>
            <button id="place-bet">Place Bet</button>
        </div>
        <div id="horse-race-result"></div>
    `;

    const oddsDiv = document.getElementById('horse-race-odds');
    const oddsList = document.getElementById('horse-odds-list');
    const horseSelection = document.getElementById('horse-selection');
    const horseSelect = document.getElementById('horse-select');
    const resultDiv = document.getElementById('horse-race-result');

    document.getElementById('horse-race-start').onclick = () => {
        const betAmount = parseFloat(document.getElementById('bet').value);

        if (isNaN(betAmount) || betAmount <= 0) {
            alert('Please enter a valid bet amount.');
            return;
        }

        fetch('http://localhost:4000/casino/horse_race/start', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ bet: betAmount })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                resultDiv.innerHTML = `<p>Error: ${data.error}</p>`;
            } else {
                oddsDiv.style.display = 'block';
                horseSelection.style.display = 'block';
                resultDiv.innerHTML = '';

                // Display odds
                oddsList.innerHTML = '';
                horseSelect.innerHTML = '';
                for (const horse of data.horses) {
                    oddsList.innerHTML += `<li>${horse}: ${data.odds[horse]}x</li>`;
                    horseSelect.innerHTML += `<option value="${horse}">${horse}</option>`;
                }

                // Store state for later use
                window.horseRaceState = { odds: data.odds, bet: betAmount };
            }
        })
        .catch(error => {
            console.error('Error starting Horse Race:', error);
            resultDiv.innerHTML = '<p>An error occurred while starting the race.</p>';
        });
    };

    document.getElementById('place-bet').onclick = () => {
        const selectedHorse = horseSelect.value;

        if (!selectedHorse) {
            alert('Please select a horse.');
            return;
        }

        fetch('http://localhost:4000/casino/horse_race', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                horse: selectedHorse,
                bet: window.horseRaceState.bet
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                resultDiv.innerHTML = `<p>Error: ${data.error}</p>`;
            } else {
                resultDiv.innerHTML = `
                    <p>${data.message}</p>
                    <p>Your Balance: ${data.player_balance}€</p>
                    <h4>Race Results:</h4>
                    <ul>
                        ${Object.entries(data.race_results)
                            .map(([horse, speed]) => `<li>${horse}: ${speed} km/h</li>`)
                            .join('')}
                    </ul>
                `;
                document.getElementById('balance').textContent = data.player_balance; // Update balance
            }
        })
        .catch(error => {
            console.error('Error in Horse Race:', error);
            resultDiv.innerHTML = '<p>An error occurred while placing your bet.</p>';
        });
    };
}

// Initialize Blackjack logic
function initBlackjack() {
    let blackjackState = {}; // Store game state locally

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
    const balanceSpan = document.getElementById('balance'); // Ensure this ID exists

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
                blackjackState = { ...data }; // Store initial state
                blackjackResult.innerHTML = `
                    <p>Your hand: ${data.player_hand.join(', ')}</p>
                    <p>Dealer's hand: ${data.dealer_hand.join(', ')}</p>
                `;
                blackjackActions.style.display = 'block';
            }
        })
        .catch(error => console.error('Error starting Blackjack:', error));
    };

    document.getElementById('blackjack-hit').onclick = () => {
        fetch('http://localhost:4000/casino/blackjack/play', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ ...blackjackState, action: 'hit' })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                blackjackState = { ...blackjackState, ...data }; // Update state
                blackjackResult.innerHTML = `
                    <p>Your hand: ${data.player_hand.join(', ')}</p>
                    <p>Dealer's hand: ${data.dealer_hand.join(', ')}</p>
                    <p>${data.result || data.message}</p>
                `;
                if (data.balance !== undefined) {
                    balanceSpan.textContent = data.balance; // Update balance
                }
                if (data.amount !== undefined && data.finished) {
                    blackjackResult.innerHTML += `<p>You ${data.amount > 0 ? 'won' : 'lost'} ${Math.abs(data.amount)}€.</p>`;
                }
                if (data.finished) blackjackActions.style.display = 'none';
            }
        })
        .catch(error => console.error('Error hitting in Blackjack:', error));
    };

    document.getElementById('blackjack-stand').onclick = () => {
        fetch('http://localhost:4000/casino/blackjack/play', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ ...blackjackState, action: 'stand' })
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                blackjackState = { ...blackjackState, ...data }; // Update state
                blackjackResult.innerHTML = `
                    <p>Your hand: ${data.player_hand.join(', ')}</p>
                    <p>Dealer's hand: ${data.dealer_hand.join(', ')}</p>
                    <p>${data.result}</p>
                    <p>You ${data.amount > 0 ? 'won' : 'lost'} ${Math.abs(data.amount)}€.</p>
                `;
                if (data.balance !== undefined) {
                    balanceSpan.textContent = data.balance; // Update balance
                }
                blackjackActions.style.display = 'none';
            }
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

