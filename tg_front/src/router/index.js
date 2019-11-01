import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import Team from '@/views/Team.vue'
import Login from '@/views/Login.vue'
import Registration from '@/views/Registration.vue'
import store from "@/store";

Vue.use(VueRouter);
const routes = [
  {
    path: '/',
    name: 'Главная',
    component: Home,
    beforeEnter (to, from, next) {
      if (!store.getters.isAuthenticated) {
        next('/login')
      } else {
        next()
      }
    }
  },
  {
    path: '/login',
    name: 'Страница входа',
    component: Login,
    beforeEnter (to, from, next) {
      if (store.getters.isAuthenticated) {
        next('/')
      } else {
        next()
      }
    }
  },
  {
    path: '/registration',
    name: 'Регистрация',
    component: Registration
  },
  // {
  //   path: '/main',
  //   name: 'Этап',
  //   component: Home,
  // },
  {
    path: '/team/qr/:id',
    name: 'Team',
    component: Team,
  },

  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
];

const router = new VueRouter({
  mode: 'history',
  routes: routes
});

export default router
