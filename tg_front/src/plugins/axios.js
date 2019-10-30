import Vue from 'vue'
import axios from 'axios'

Vue.use({
    install (Vue) {
        Vue.prototype.$api = axios.create({
            baseURL: 'http://84.201.184.131:5000/',
            timeout: 1000,
        })
    }
});