'use strict';

// Get references to the buttons and result display area
const button_1 = document.getElementById('button_1');
const button_2 = document.getElementById('button_2');
const button_3 = document.getElementById('button_3');
const button_4 = document.getElementById('button_4');
const button_5 = document.getElementById('button_5');
const button_6 = document.getElementById('button_6');
const lollipop_result = document.getElementById('lollipop_result');

// List of available lollipop options
const lollipop_brands = [
    "RINGPOP", 
    "MOOMIN", 
    "JOLLY RANCHER", 
    "JOHN'S SPECIAL", 
    "SALVIA POP", 
    "CHUPACHUPS"
];

// Utility function to make an API call and return the data
async function getData(url) {
    try {
        const response = await fetch(url);
        const data = await response.json();
        console.log('Response from API:', data);
        return data;
    } catch (error) {
        console.error('Error fetching data from API:', error);
        return { status: 'error', message: 'Unable to reach the server.' };
    }
}

// Utility function to send POST request with JSON data
async function postData(url, data) {
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        const result = await response.json();
        console.log('Response from API:', result);
        return result;
    } catch (error) {
        console.error('Error posting data to API:', error);
        return { status: 'error', message: 'Unable to reach the server.' };
    }
}

// Populate buttons with lollipop options
function populateButtons() {
    button_1.innerHTML = `Lollipop: ${lollipop_brands[0]}`;
    button_2.innerHTML = `Lollipop: ${lollipop_brands[1]}`;
    button_3.innerHTML = `Lollipop: ${lollipop_brands[2]}`;
    button_4.innerHTML = `Lollipop: ${lollipop_brands[3]}`;
    button_5.innerHTML = `Lollipop: ${lollipop_brands[4]}`;
    button_6.innerHTML = `Lollipop: ${lollipop_brands[5]}`;

    // Attach the lollipop names as attributes
    button_1.value = lollipop_brands[0];
    button_2.value = lollipop_brands[1];
    button_3.value = lollipop_brands[2];
    button_4.value = lollipop_brands[3];
    button_5.value = lollipop_brands[4];
    button_6.value = lollipop_brands[5];
}

// Event listener for button clicks
async function handleLollipopClick(lollipop) {
    const data = { lollipop: lollipop };
    const result = await postData('http://127.0.0.1:4000/lollipop/select', data);
    
    if (result.status === 'success') {
        lollipop_result.innerText = result.message;
    } else if (result.status === 'fail') {
        lollipop_result.innerText = `Failure: ${result.message}`;
    } else {
        lollipop_result.innerText = `Error: ${result.message}`;
    }
}

// Attach event listeners to each button
button_1.addEventListener('click', () => handleLollipopClick(button_1.value));
button_2.addEventListener('click', () => handleLollipopClick(button_2.value));
button_3.addEventListener('click', () => handleLollipopClick(button_3.value));
button_4.addEventListener('click', () => handleLollipopClick(button_4.value));
button_5.addEventListener('click', () => handleLollipopClick(button_5.value));
button_6.addEventListener('click', () => handleLollipopClick(button_6.value));

// Call this to set up the lollipop button options on page load
populateButtons();
