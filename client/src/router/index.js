import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Graphs from '../views/Graphs.vue'
import Prediction from '../views/Prediction.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/prediction',
    name: 'Prediction',
    component: Prediction
  },
  {
    path: '/graphs',
    name: 'Graphs',
    component: Graphs
  },
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
