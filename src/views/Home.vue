<template>
  <div class="chat-container">
    <ChatWindow />
  </div>
</template>

<script setup>
import ChatWindow from '../components/ChatWindow.vue'
</script>

<style>
.chat-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  padding: 1rem;
  box-sizing: border-box;
}
</style>
