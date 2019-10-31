<template>
    <div class="login-form">
        <b-form class="form-signin">
            <b-img center src="../img/TG.svg" alt="" width="72" height="72"></b-img>
            <h1 class="h3 mb-3 font-weight-normal text-center">Начните этап!</h1>
            <b-form-group id="label-input-stage" label="Этапы:" label-for="input-stage">
                <b-form-select
                        class="form-control"
                        id="input-stage"
                        v-model="stage"
                        :options="stages"
                        required
                ></b-form-select>
            </b-form-group>

            <b-form-group
                    class="form-control"
                    id="label-input-pin"
                    label="Ваш пин-код:"
                    label-for="input-pin"
                    :state="validCode">
                <b-form-input
                        id="input-pin"
                        v-model="code"
                        type="password"
                        required
                        placeholder="Введите пин-код..."
                ></b-form-input>
            </b-form-group>

            <b-button block type="button" :disabled="!validFrom" variant="primary" @click="login">Войти</b-button>

            <div class="text-center" style="margin-top: 10px">
                У тебя еще нет этапа?
                <b-link href="/registration"> Исправляй! </b-link>
            </div>

        </b-form>


    </div>
</template>

<script>
import { EventBus } from '@/utils'
export default {
    name: "Login",
    data() {
        return {
            stage: null,
            code: '',
            stages: [{ text: 'Выберите из списка:', value: null }],
            error: null
        }
    },

    created() {
        this.getAllStages();
    },

    computed: {
        validCode() {
            let re =  /^\d{4}$/;
            return this.code.length === 4 && re.test(this.code);
        },
        validFrom() {
            return this.validCode && this.stage
        }
    },

    methods: {
        // login() {
        //     this.$store.dispatch('login', { id: this.stage, code: this.code })
        //         .then(() => this.$router.push('/'))
        // },

        login() {
            const { stage, code } = this;
            this.$store.dispatch('AUTH_REQUEST', { id: stage, code: code })
                .then(() => this.$router.push('/'))
        },


        getAllStages(){
            this.$api.get('/stages/getAll')
                .then((response) => {
                    if(response.data.result){
                        response.data.stages.forEach(stage => {
                            this.stages.push({text: stage.text, value: stage.value});
                        });
                    }
                })
                .catch(error => {
                    this.error = error.response;
                })
        }
    },

    mounted () {
        EventBus.$on('failedAuthentication', (msg) => {
            this.errorMsg = msg;
        })
    },

    beforeDestroy () {
        EventBus.$off('failedAuthentication');
    }

}
</script>

<style scoped>
    .login-form {
        padding-top: 40px;
        padding-bottom: 40px;
        background-color: #f5f5f5;
    }

    .form-signin {
        width: 100%;
        max-width: 330px;
        padding: 15px;
        margin: auto;
    }
    .form-signin .form-control {
        position: relative;
        box-sizing: border-box;
        height: auto;
        padding: 10px;
        font-size: 16px;
    }
    .form-signin .form-control:focus {
        z-index: 2;
    }
</style>