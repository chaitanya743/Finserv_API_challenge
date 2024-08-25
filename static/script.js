document.addEventListener('DOMContentLoaded', () => {
    const dataInput = document.getElementById('dataInput');
    const filteredDataParagraph = document.getElementById('filteredData');
    const submitButton = document.getElementById('submitButton');
    const resetButton = document.getElementById('resetButton');
    const filterButtons = document.querySelectorAll('.filter-button');

    let apiResponse = null;

    async function submitData() {
        const userData = dataInput.value.split(',').map(item => item.trim()).filter(item => item);
        const requestData = { data: userData };

        try {
            const response = await fetch('http://127.0.0.1:8000/bfhl', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(requestData)
            });

            apiResponse = await response.json();
            updateFilteredData(); // Show all data initially
        } catch (error) {
            console.error('Error:', error);
            filteredDataParagraph.textContent = 'An error occurred while processing the data.';
        }
    }

    function updateFilteredData(filter = 'All') {
        if (!apiResponse) return;

        let outputText = '';

        if (filter === 'Numbers') {
            outputText = `Numbers: ${apiResponse.numbers.join(', ')}`;
        } else if (filter === 'Alphabets') {
            outputText = `Alphabets: ${apiResponse.alphabets.join(', ')}`;
        } else if (filter === 'Lowercase') {
            const lowercaseAlphabets = apiResponse.alphabets.filter(a => /^[a-z]$/.test(a));
            outputText = `Lowercase Alphabets: ${lowercaseAlphabets.join(', ')}`;
        } else if (filter === 'Uppercase') {
            const uppercaseAlphabets = apiResponse.alphabets.filter(a => /^[A-Z]$/.test(a));
            outputText = `Uppercase Alphabets: ${uppercaseAlphabets.join(', ')}`;
        } else if (filter === 'Highest Lowercase Alphabet') {
            const lowercaseAlphabets = apiResponse.alphabets.filter(a => /^[a-z]$/.test(a));
            const highestLowercase = lowercaseAlphabets.sort().slice(-1); // Get the highest alphabet
            outputText = `Highest Lowercase Alphabet: ${highestLowercase.join(', ')}`;
        } else {
            outputText = `Numbers: ${apiResponse.numbers.join(', ')}\n` +
                         `Alphabets: ${apiResponse.alphabets.join(', ')}\n` +
                         `Highest Lowercase Alphabet: ${apiResponse.highest_lowercase_alphabet.join(', ')}`;
        }

        filteredDataParagraph.textContent = outputText;
    }

    submitButton.addEventListener('click', submitData);
    resetButton.addEventListener('click', () => {
        dataInput.value = '';
        filteredDataParagraph.textContent = '';
        apiResponse = null; // Clear the stored API response
    });

    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            const filter = button.getAttribute('data-filter');
            updateFilteredData(filter);
        });
    });
});
