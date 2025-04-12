<template>
  <div :class="['chat-container', { soft: isSoftMode }]">
    <div class="chat-box">
      <div v-for="(msg, index) in messages" :key="index" :class="['message', msg.role]">
        <span>{{ msg.content }}</span>
      </div>
    </div>

    <form class="input-box" @submit.prevent="sendMessage">
      <input
        type="text"
        v-model="input"
        placeholder="Введите сообщение..."
        :disabled="loading"
        class="input-field"
      />
      <button type="submit" :disabled="loading">➤</button>
    </form>

    <label class="toggle">
      <input type="checkbox" v-model="isSoftMode" />
      Мягкий режим
    </label>
  </div>
</template>

<script>
export default {
  data() {
    return {
      input: "",
      messages: [
        { role: "assistant", content: "Привет! Я здесь, чтобы помочь. Можешь начать с любого слова." },
        { role: "assistant", content: "Как ты себя сегодня чувствуешь?" }
      ],
      loading: false,
      isSoftMode: true, // по умолчанию включён
    };
  },
  methods: {
    async sendMessage() {
      if (!this.input.trim()) return;

      const userMsg = { role: "user", content: this.input };
      this.messages.push(userMsg);
      this.loading = true;
      const systemMessage = this.isSoftMode
        ? "Ты — внимательный, мягкий собеседник. Говори тихо, спокойно, с заботой."
        : "Ты поддерживающий собеседник.";

      try {
        const res = await fetch("http://localhost:5000/api/message", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            message: this.input,
            mode: this.isSoftMode ? "reflect" : "chat", // отправляем режим
          }),
        });
        const data = await res.json();
        if (data.reply) {
          this.messages.push({ role: "assistant", content: data.reply });
        }
      } catch (e) {
        this.messages.push({ role: "assistant", content: "Ошибка соединения." });
      } finally {
        this.input = "";
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
.chat-container {
  font-family: "Inter", sans-serif;
    background: #f9f9f9;
    min-height: 100vh;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: 20px;
    box-sizing: border-box;
    align-content: space-between;
    flex-wrap: wrap;
}

.chat-box {
  width: 100%;
  max-width: 700px;
  background: white;
  padding: 20px;
  border-radius: 16px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  gap: 10px;
  overflow-y: auto;
  max-height: 80vh;
}

.message {
  padding: 10px 14px;
  border-radius: 12px;
  max-width: 80%;
  word-break: break-word;
  font-size: 16px;
  line-height: 1.4;
  color: #333; /* Увеличен контраст */
}

.message.user {
  background: #d6f7f5;
  align-self: flex-end;
}

.message.assistant {
  background: #f0f4ff;
  align-self: flex-start;
}

.input-box {
  display: flex;
  align-items: center;
  gap: 8px;
  max-width: 700px;
  width: 100%;
  margin-top: 10px;
}

.input-field {
  flex: 1;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 12px;
  font-size: 16px;
  outline: none;
  box-sizing: border-box;
}

button {
  padding: 10px 14px;
  background: #409eff;
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 18px;
  cursor: pointer;
}

.toggle {
  margin-top: 10px;
  font-size: 14px;
  display: flex;
  justify-content: flex-end;
  color: #444;
  align-items: center;
  gap: 6px;
}

.soft .message.user {
  background: #e7f5ff;
}

.soft .message.assistant {
  background: #fff9f0;
}

.soft .chat-box {
  background: #fcfcfc;
  box-shadow: 0 4px 12px rgba(160, 160, 160, 0.1);
}
</style>
