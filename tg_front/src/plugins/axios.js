import Vue from 'vue'
import axios from 'axios'

Vue.use({
    install (Vue) {
        Vue.prototype.$api = axios.create({
            baseURL: 'http://127.0.0.1:5000/',
            timeout: 1000,
        })
    }
});