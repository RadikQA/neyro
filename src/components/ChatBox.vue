<template>
    <div :class="['chat-container', { soft: isSoftMode }]">
      <div class="messages">
        <div
          v-for="(msg, index) in messages"
          :key="index"
          :class="['message', msg.role]"
        >
          <span>{{ msg.content }}</span>
        </div>
      </div>
      <div class="input-area">
        <input
          v-model="newMessage"
          @keyup.enter="sendMessage"
          placeholder="Введите сообщение..."
        />
        <button @click="sendMessage">➤</button>
        <label class="toggle">
          <input type="checkbox" v-model="isSoftMode" />
          <span>Мягкий режим</span>
        </label>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        messages: [
          { role: 'user', content: 'привет' },
          { role: 'assistant', content: 'Привет! Как могу помочь?' }
        ],
        newMessage: '',
        isSoftMode: false
      }
    },
    methods: {
      sendMessage() {
        if (!this.newMessage.trim()) return
        this.messages.push({ role: 'user', content: this.newMessage })
        this.newMessage = ''
        // Добавь тут нейросетевой отклик при необходимости
      }
    }
  }
  </script>
  
  <style scoped>
  .chat-container {
    display: flex;
    flex-direction: column;
    max-width: 600px;
    margin: 0 auto;
    background: #f5f5f5;
    min-height: 100vh;
    padding: 20px;
    box-sizing: border-box;
  }
  
  .soft {
    background: #fafafa;
  }
  
  .messages {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-bottom: 20px;
  }
  
  .message {
    max-width: 75%;
    padding: 10px 14px;
    border-radius: 12px;
    font-size: 15px;
    line-height: 1.4;
    color: #1a1a1a;
    word-break: break-word;
  }
  
  .message.user {
    align-self: flex-end;
    background-color: #daf0ff;
  }
  
  .message.assistant {
    align-self: flex-start;
    background-color: #ececec;
  }
  
  .soft .message.user {
    background-color: #e0f5ff;
  }
  
  .soft .message.assistant {
    background-color: #f9f1e8;
  }
  
  .input-area {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: auto;
  }
  
  input[type='text'],
  input {
    flex: 1;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 14px;
    outline: none;
  }
  
  button {
    background: #007bff;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 14px;
    cursor: pointer;
    font-size: 14px;
  }
  
  .toggle {
    margin-left: auto;
    font-size: 14px;
    color: #444;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  
  .toggle input[type='checkbox'] {
    transform: scale(1.2);
  }
  </style>
  