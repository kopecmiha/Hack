import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/map',
    name: 'map',
    component: () => import('../views/Map.vue')
  },
  {
    path: '/profile',
    name: 'profile',
    component: () => import('../views/Profile.vue')
  },
  {
    path: '/profileview/:id',
    name: 'profileview',
    component: () => import('../views/profileview.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
