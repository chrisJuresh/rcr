import { createRouter, createWebHistory } from 'vue-router'
import AuthPage from '../views/AuthPage.vue'
import ProfilePage from '../views/ProfilePage.vue'

const routes = [
    {
        path: '/auth',
        name: 'auth',
        component: AuthPage
    },
    {
        path: '/profile',
        name: 'profile',
        component: ProfilePage
    }
]

const router = createRouter({
  history: createWebHistory(),
  routes 
})

export default router