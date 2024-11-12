// frontend/src/main.js

import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

import './assets/style.css'; // Optional: add additional CSS for styling

const app = createApp(App);
app.use(router);
app.mount('#app');
