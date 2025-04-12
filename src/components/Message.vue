<template>
  <div :class="['message', role]">
    <div class="text">{{ text }}</div>
  </div>
</template>

<script setup>
const props = defineProps({
  role: String,
  text: String
})
</script>

<style scoped>
.message {
  padding: 0.75rem;
  border-radius: 0.75rem;
  max-width: 80%;
}
.message.user {
  align-self: flex-end;
  background: #4e9;
  color: #000;
}
.message.assistant {
  align-self: flex-start;
  background: #444;
  color: #fff;
}
</style>
