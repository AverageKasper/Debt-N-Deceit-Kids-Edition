'use strict';

const usernameInput = document.getElementById('username');
const submitButton = document.getElementById('submit-username');
const difficultyButtons = document.getElementById('difficulty-buttons');
const usernameContainer = document.getElementById('username-container');


submitButton.addEventListener('click', () => {
    const username = usernameInput.value.trim();
    if (username) {
        alert(`Welcome, ${username}! Please select your difficulty.`);
        usernameContainer.style.display = 'none';
        difficultyButtons.style.display = 'flex';
    } else {
        alert('Please enter a valid username.');
    }
});

// Handle difficulty selection
document.querySelectorAll('.difficulty-button').forEach(button => {
    button.addEventListener('click', () => {
        const difficulty = button.dataset.difficulty;
        alert(`You selected ${difficulty} difficulty. Get ready!`);
        // Redirect or start game logic here
    });
});