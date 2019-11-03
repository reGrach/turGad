import Vue from 'vue'
import Vuex from 'vuex'
import { loginStage, registerStage, changeToken } from '@/axios'
import { isValidJwt } from '@/utils'

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        stageTitle: localStorage.getItem('turist-name') || '',
        token: localStorage.getItem('turist-token') || '',
        status: '',
    },

    actions: {
        login({commit}, stage) {
            return new Promise((resolve, reject) => {
                commit('authLoading');
                loginStage(stage)
                    .then(resp => {
                        const token = resp.data.token;
                        const title = stage.title;
                        commit('authSuccess', {token, title});
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('authError', err);
                        reject(err)
                    })
            })
        },
        logout({commit}) {
            commit('authLogout');
        },

        register({commit, dispatch}, newStage) {
            return new Promise((resolve, reject) => {
                commit('authLoading');
                registerStage(newStage)
                    .then(resp => {
                        const stage = { id: resp.data.id, title: newStage.title, code: newStage.code };
                        dispatch('login', stage);
                        resolve(resp)
                    })
                    .catch(err => {
                        commit('regError', err);
                        reject(err)
                    })
            })
        },
    },

    mutations: {

        authLoading: (state) => {
            state.status = 'loading';
        },

        authSuccess: (state, {token, title}) => {
            localStorage.setItem('turist-token', token);
            localStorage.setItem('turist-name', title);
            changeToken(token);
            state.status = 'success';
            state.token = token;
            state.stageTitle = title;
        },

        authError: (state) => {
            localStorage.removeItem('turist-token');
            localStorage.removeItem('turist-name');
            changeToken('');
            state.status = 'error';
        },

        regError: (state) => {
            state.status = 'reg_error';
        },

        authLogout: (state) => {
            localStorage.removeItem('turist-token');
            localStorage.removeItem('turist-name');
            changeToken('');
            state.status = 'logout';
            state.stageTitle = '';
            state.token = '';
        }
    },

    getters: {
        isAuthenticated: state => isValidJwt(state.token),
        isMain: state => state.stageTitle === 'Древний этап',
        getTitle: state => state.stageTitle,
        authStatus: state => state.status,
    }
})

