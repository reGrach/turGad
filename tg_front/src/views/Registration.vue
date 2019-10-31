<template>
    <div class="login-form">
        <b-form class="form-signin">
            <b-img center src="../img/TG.svg" alt="" width="72" height="72"></b-img>
            <h1 class="h3 mb-3 font-weight-normal text-center">Зарегистрируйте этап!</h1>
            <b-form-group id="label-input-stage" label="Что за этап?" label-for="input-stage">
                <b-form-input
                        class="form-control"
                        id="input-stage"
                        v-model="stage"
                        type="text"
                        required
                        placeholder="Введите название этапа"
                ></b-form-input>
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

            <b-form-group
                    class="form-control"
                    id="label-input-pin-repeat"
                    label="На всякий случай, еще разок:"
                    label-for="input-pin">
                <b-form-input
                        id="input-pin-repeat"
                        v-model="repeatCode"
                        type="password"
                        placeholder="Повторите пин-код..."
                        required
                ></b-form-input>
            </b-form-group>

            <b-button block type="button" :disabled="!validFrom" variant="primary" @click="registration">Регистрация</b-button>
        </b-form>
    </div>
</template>

<script>
import { EventBus } from '@/utils'
export default {
    name: "Registration",
    data() {
        return {
            stage: '',
            code: '',
            repeatCode: '',
            error: null
        }
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

    mounted () {
        EventBus.$on('failedRegistering', (msg) => {
            this.error = msg;
            this.makeToast(msg);
        });
    },

    methods: {
        registration() {
            if(this.code !== this.repeatCode) {
                this.makeToast('Введенные коды не совпадают. Еще разок!');
                return;
            }
            this.$store.dispatch('register', { title: this.stage, code: this.code })
                    .then(() => {
                        this.showSuccessMsg();
                    });
        },

        getAllStages(){
            this.$api.get('/stages/getAll')
                .then(response => {
                    if(response.data.result){
                        this.stages.push(response.data.stages);
                    }
                })
                .catch(error => {
                    this.error = error.response;
                })
        },

        makeToast(text) {
            this.$bvToast.toast(text, {
                title: 'Ошибка!',
                variant: 'danger',
                solid: true
            });
        },

        showSuccessMsg() {
            this.$bvModal.msgBoxOk('Ваш этап зарегестрирован!', {
                title: 'Успех!',
                size: 'sm',
                buttonSize: 'sm',
                okVariant: 'success',
                headerClass: 'p-2 border-bottom-0',
                footerClass: 'p-2 border-top-0',
                centered: true
            })
                .then(() => {
                    this.$router.push('/')
                })
        },

    },

    beforeDestroy () {
        EventBus.$off('failedRegistering');
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