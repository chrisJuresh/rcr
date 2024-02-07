import { createRouter, createWebHistory } from 'vue-router'
import AuthPage from '../views/AuthPage.vue'
import ProfilePage from '../views/ProfilePage.vue'
import PanelPage from '../views/PanelPage.vue'
import NewJDPage from '../views/NewJD.vue' 

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
        path: '/panel',
        component: PanelPage
    },
    {
        path: '/newJD', 
        component: NewJDPage
    }
]

const router = createRouter({
  history: createWebHistory(),
  routes 
})

export default router