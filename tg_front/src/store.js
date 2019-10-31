import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
// import { isValidJwt, EventBus } from '@/utils'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        stage: {},
        token: localStorage.getItem('token') || '',
        status: '',
    },

    actions: {
        'AUTH_REQUEST': ({commit, dispatch}, stage) => {
            return new Promise((resolve, reject) => { // The Promise used for router redirect in login
                commit('AUTH_REQUEST');
                axios.post('http://127.0.0.1:5000/api/stages/login', stage)
                    .then(resp => {
                        const token = resp.data.token;
                        localStorage.setItem('token', token); // store the token in localstorage
                        commit('AUTH_SUCCESS', token);
                        // you have your token, now log in your user :)
                        dispatch('USER_REQUEST');
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('AUTH_ERROR', err);
                        localStorage.removeItem('token'); // if the request fails, remove any possible user token if possible
                        reject(err)
                    })
            })
        }




        // login(context, stageData) {
        //     context.commit('setStageData', {stageData});
        //     return axios.post('http://127.0.0.1:5000/api/stages/login', stageData)
        //         .then(response => {
        //             context.commit('setJwtToken', {jwt: response.data})
        //         })
        //         .catch(error => {
        //             console.log('Error Authenticating: ', error);
        //             EventBus.$emit('failedAuthentication', error)
        //         })
        // },
        // register(context, stageData) {
        //     context.commit('setUserData', {stageData});
        //     return axios.post('http://127.0.0.1:5000/api/stages/registration', stageData)
        //         .then(context.dispatch('login', stageData))
        //         .catch(error => {
        //             console.log('Error Registering: ', error);
        //             EventBus.$emit('failedRegistering: ', error)
        //         })
        // },
    },

    mutations: {
        AUTH_REQUEST: (state) => {
            state.status = 'loading';
        },
        AUTH_SUCCESS: (state, token) => {
            state.status = 'success';
            state.token = token
        },
        AUTH_ERROR: (state) => {
            state.status = 'error';
        },
    },
    //     setStageData (state, payload) {
    //         console.log('setUserData payload = ', payload);
    //         state.stage = payload.stageData
    //     },
    //     setJwtToken (state, payload) {
    //         console.log('setJwtToken payload = ', payload);
    //         localStorage.token = payload.jwt.token;
    //         state.jwt = payload.jwt
    //     }
    // },
    getters: {
        isAuthenticated: state => !!state.token,
        authStatus: state => state.status,
    }
})


// const state = {
//     // single source of data
//     surveys: [],
//     currentSurvey: {},
//     user: {},
//     jwt: ''
// };

// const actions = {
//     login (context, stageData) {
//         context.commit('setUserData', { stageData });
//         return this.$api.post('/login', stageData)
//             .then(response => context.commit('setJwtToken', { jwt: response.data }))
//             .catch(error => {
//                 console.log('Error Authenticating: ', error);
//                 EventBus.$emit('failedAuthentication', error)
//             })
//     },
//     register (context, stageData) {
//         context.commit('setUserData', { stageData });
//         return this.$api.post('/stages/registration', stageData)
//             .then(context.dispatch('login', stageData))
//             .catch(error => {
//                 console.log('Error Registering: ', error);
//                 EventBus.$emit('failedRegistering: ', error)
//             })
//     }
// };

// const mutations = {
//     setUserData (state, payload) {
//         console.log('setUserData payload = ', payload);
//         state.userData = payload.userData
//     },
//     setJwtToken (state, payload) {
//         console.log('setJwtToken payload = ', payload);
//         localStorage.token = payload.jwt.token;
//         state.jwt = payload.jwt
//     }
// };

// const getters = {
//     // reusable data accessors
//     isAuthenticated (state) {
//         return isValidJwt(state.jwt.token)
//     }
// };

