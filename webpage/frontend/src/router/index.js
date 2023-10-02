
import { createRouter, createWebHashHistory} from 'vue-router'
import axios from 'axios'
import store from '../store'

import Home from '../view/Home.vue'
import Tutorial from '../view/Tutorial.vue'
import Upload from '../view/Upload.vue'
import History from '../view/History.vue'
import Patient from '../view/Patient.vue'
import Display from '../view/Display.vue'

const routes = [
    {
      path: "/",
      name: "/",
      redirect: "/Upload",
    },
    {
      path: '/Upload',
      name: "Upload",
      component: Upload
    },
    {
      path: '/History',
      name: 'History',
      component: History,
      beforeEnter:(to,from,next) => {
        axios.get("http://127.0.0.1:5000/api/getdata")
        .then((res)=>{
            console.log('資料 : ',res.data)
            store.dispatch("LoadHistory", res.data);
            next();
        })
      }
    },
    {
      path: '/Tutorial',
      name: 'Tutorial',
      component: Tutorial
    },
    {
      path: '/Patient',
      name: 'Patient',
      component: Patient,
      beforeEnter:(to,from,next) => {
        axios.get("http://127.0.0.1:5000/api/getPatient")
        .then((res)=>{
            console.log('資料 : ',res.data)
            store.dispatch("LoadPatient", res.data);
            next();
        })
      }
    },
    {
      path: '/Display',
      name: 'Display',
      component: Display
    }
  ]
const router = createRouter({
    history: createWebHashHistory(import.meta.env.BASE_URL), // 這邊我使用 # 路徑模式
    routes, // 導入使用上方 routes 所定義的路徑
    linkActiveClass: "active",
  })

export default router;