import Vue from 'vue'
import axios from 'axios'

Vue.use({
    install (Vue) {
        Vue.prototype.$api = axios.create({
            // baseURL: process.env.VUE_APP_BASE_URL,
            // baseURL: 'http://127.0.0.1:5000/api',
            baseURL: 'http://84.201.184.131:5000/api',
            timeout: 1000,
        })
    }
});