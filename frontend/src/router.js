// frontend/src/router.js

import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from './components/Dashboard.vue';
import PatientProfile from './components/PatientProfile.vue';

const routes = [
  { path: '/', component: Dashboard },
  { path: '/patient/:id', component: PatientProfile, props: true },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
