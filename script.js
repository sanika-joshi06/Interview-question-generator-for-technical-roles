document.getElementById('questionForm').addEventListener('submit', async (e) => {
    e.preventDefault();
  
    const role = document.getElementById('role').value.trim();
    const level = document.getElementById('level').value;
  
    // Clear previous output
    const outputElement = document.getElementById('questionsText');
    outputElement.textContent = 'Generating questions...';
  
    try {
      const response = await fetch('/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ role, level })
      });
  
      if (!response.ok) {
        // If the response is not OK, throw an error with the status
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      const data = await response.json();
      outputElement.textContent = data.questions;
    } catch (error) {
      console.error('Error:', error);
      outputElement.textContent = 'An error occurred while generating questions. Please try again later.';
    }
  });