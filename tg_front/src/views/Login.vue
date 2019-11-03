<template>
    <div class="login-form">
        <b-form class="form-signin">
            <b-img center src="../img/TG.svg" alt="" width="72" height="72"></b-img>
            <h1 class="h3 mb-3 font-weight-normal text-center">Начните этап!</h1>
            <b-form-group id="label-input-stage" label="Этапы:" label-for="input-stage">
                <b-form-select
                        class="form-control"
                        id="input-stage"
                        v-model="stageId"
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
                <b-link href="/registration"> Исправляй!</b-link>
            </div>
        </b-form>
    </div>
</template>

<script>
    import {EventBus} from '@/utils'
    import {getAllStages} from '@/axios'

    export default {
        name: "Login",
        data() {
            return {
                stageId: null,
                code: '',
                stages: [{text: 'Выберите из списка:', value: null}],
                error: null
            }
        },

        created() {
            this.getAllStages();
        },

        computed: {

            stageTitle() {
                let stage = this.stages.find(item => item.value === this.stageId);
                if (stage) {
                    return stage.text;
                } else return null;

            },

            validCode() {
                let re = /^\d{4}$/;
                return this.code.length === 4 && re.test(this.code);
            },
            validFrom() {
                return this.validCode && this.stageId
            }
        },

        methods: {

            login() {
                const {stageId, code} = this;
                this.$store.dispatch('login', {id: stageId, title: this.stageTitle, code: code})
                    .then(() => this.$router.push('/'))
            },


            getAllStages() {
                getAllStages()
                    .then((response) => {
                        if (response.data.result) {
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

        mounted() {
            EventBus.$on('failedAuthentication', (msg) => {
                this.errorMsg = msg;
            })
        },

        beforeDestroy() {
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