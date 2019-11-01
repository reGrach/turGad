import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import '@/plugins/bootstrap-vue'
// import '@/axios'
import App from '@/App.vue'
import router from '@/router'
import store from "@/store";
import { changeToken } from "@/axios"
// import axios from "axios";

Vue.config.productionTip = false;

const token = localStorage.getItem('turist-token');
if (token) { changeToken(token); }

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
