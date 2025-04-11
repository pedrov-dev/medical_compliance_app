// frontend/app.js
const API_URL = "http://localhost:8000/chat";
const userId = "user123"; // In production, use proper user authentication.

async function sendMessage() {
  const inputElem = document.getElementById("user-input");
  const message = inputElem.value;
  if (!message) return;

  // Append user message to chat window.
  appendMessage("user", message);

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: userId, message: message })
    });
    const data = await response.json();
    // Display the conversation (could just display the latest message)
    data.responses.forEach(msg => {
      appendMessage(msg.role, msg.message);
    });
  } catch (error) {
    console.error("Error:", error);
  }
  inputElem.value = "";
}

function appendMessage(role, message) {
  const chatWindow = document.getElementById("chat-window");
  const messageElem = document.createElement("div");
  messageElem.className = role;
  messageElem.innerText = `${role}: ${message}`;
  chatWindow.appendChild(messageElem);
}
