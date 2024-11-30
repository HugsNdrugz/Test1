
import { createRouter, createWebHistory } from 'vue-router';
import Chat from './components/Chat.vue';

const routes = [
  {
    path: '/chat',
    name: 'Chat',
    component: Chat,
  },
  {
    path: '/',
    redirect: '/chat',
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
