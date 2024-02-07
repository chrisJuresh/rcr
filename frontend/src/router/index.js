import { createRouter, createWebHistory } from 'vue-router'
import AuthPage from '../views/AuthPage.vue'
import ProfilePage from '../views/ProfilePage.vue'
import JD from '../views/JD.vue'

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
    },
    {
        path: '/jd',
        redirect: '/JD',
        component: JD
    }
]

const router = createRouter({
  history: createWebHistory(),
  routes 
})

export default router