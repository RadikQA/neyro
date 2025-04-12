export async function sendMessageToOpenAI(message) {
    const response = await fetch('http://localhost:5000/api/message', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message }),
    });
  
    if (!response.ok) {
      const error = await response.text();
      console.error('Backend API error:', error);
      return 'Произошла ошибка. Проверь backend.';
    }
  
    const data = await response.json();
    return data.reply;
  }
  