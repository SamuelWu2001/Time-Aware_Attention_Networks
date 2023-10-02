import {createApp} from 'vue'
import VueChartkick from 'vue-chartkick'
import 'chartkick/chart.js'
import App from './App.vue'
import Ele from 'element-plus'
import 'element-plus/dist/index.css'


import "./assets/bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import router from './router'
import store from './store'
import axios from 'axios'


createApp(App).use(Ele).use(VueChartkick).use(store).use(router).mount('#app')