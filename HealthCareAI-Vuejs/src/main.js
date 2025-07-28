import { createApp } from 'vue'
import { Quasar } from 'quasar'
import '@quasar/extras/material-icons/material-icons.css'
import 'quasar/src/css/index.sass'

import { createWebHistory, createRouter } from 'vue-router'

import App from './App.vue'
import Home from './components/Home.vue'
import PatientList from './components/PatientList.vue'
import AddPatient from './components/AddPatient.vue'

const routes = [
  { path: '/Home', component: Home },
  { path: '/PatientList', component: PatientList },
  { path: '/', redirect: '/Home' },
  { path: '/AddPatient', component: AddPatient },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

const myApp = createApp(App)

myApp
  .use(router)
  .use(Quasar, { plugins: {} })

myApp.mount('#app')
