import axios from 'axios'

const instance = axios.create({
    baseURL: 'http://127.0.0.1:5000/api',
    // baseURL: 'http://84.201.184.131:5000/api',
    timeout: 5000
});

export function changeToken(token) {
    instance.defaults.headers.common['Authorization'] = token;
}

export function getAllStages() {
    return instance.get('/stages/getAll')
}

export function getTeamById(id) {
    return instance.get('/team/get/' + id)
}

export function registerTeam(data) {
    return instance.post('/team/registration', data)
}

export function loginStage(data) {
    return instance.post('/stages/login', data)
}

export function registerStage(data) {
    return instance.post('/stages/registration', data)
}

export function checkToken() {
    return instance.post('/stages/check')
}
