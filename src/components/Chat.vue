
<template>
  <div id="chat-container">
    <div v-if="isLoading" class="loading">Loading messages...</div>
    <div v-if="error" class="error">{{ error }}</div>
    <div v-else>
      <div
        v-for="(message, index) in messages"
        :key="index"
        :class="['message', message.sender === 'You' ? 'sender-you' : 'sender-other']"
      >
        <strong>{{ message.sender }}:</strong>
        <p>{{ message.text }}</p>
        <span class="time">{{ message.time }}</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';

const messages = ref([]);
const isLoading = ref(true);
const error = ref<string | null>(null);

onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:8080/api/chat_messages');
    messages.value = response.data;
  } catch (err) {
    error.value = 'Failed to load messages';
  } finally {
    isLoading.value = false;
  }
});
</script>

<style scoped>
#chat-container {
  max-width: 600px;
  margin: 20px auto;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 10px;
  background: #f9f9f9;
  overflow-y: auto;
  height: 80vh;
  display: flex;
  flex-direction: column;
}

.message {
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 8px;
  max-width: 70%;
}

.sender-you {
  background: #e0f7fa;
  align-self: flex-end;
}

.sender-other {
  background: #e8f5e9;
  align-self: flex-start;
}

.time {
  font-size: 0.8em;
  color: #888;
}
</style>
