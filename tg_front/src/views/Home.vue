<template>
    <div class="home">
        <b-navbar variant="faded" type="light">
            <b-navbar-brand>
                <b-container fluid>

                    <div class="d-flex justify-content-between">
                        <b-col cols="3" class="align-self-center">
                            <b-img src="../img/TG.svg" class="d-inline-block align-top" width="50"
                                   height="50"></b-img>
                        </b-col>
                        <b-col cols="6" class="align-self-center"><h4>{{this.$store.getters.getTitle}}</h4></b-col>

                        <b-col cols="3" class="align-self-center">
                            <b-button variant="outline-dark" @click="logout">Выход</b-button>
                        </b-col>
                    </div>
                </b-container>
            </b-navbar-brand>
        </b-navbar>

        <b-alert show>Чтобы зафиксировать этап, просканируйте qr-код команды</b-alert>

<!--        <div>-->
<!--            <b-input-group-->
<!--                    class="mb-3"-->
<!--                    prepend="Команда:"-->
<!--            >-->
<!--                <b-form-select-->
<!--                        id="input-team"-->
<!--                        v-model="teamId"-->
<!--                        :options="teams"-->
<!--                        required-->
<!--                ></b-form-select>-->
<!--                <b-input-group-append>-->
<!--                    <b-button variant="success">Зафиксировать</b-button>-->
<!--                </b-input-group-append>-->
<!--            </b-input-group>-->
<!--        </div>-->
    </div>
</template>

<script>
    // import HelloWorld from '@/components/Fixation.vue'
    // import {getUnPassTeam} from '@/axios'

    export default {
        name: 'home',
        data() {
            return {
                error: null,
                teamId: null,
                teams: [{text: 'Выберите из списка:', value: null}],
            }
        },
        // components: {
        //   HelloWorld
        // }

        // created() {
        //     this.getTeams();
        // },

        methods: {
            logout() {
                this.$store.dispatch('logout');
                this.$router.push('/login');
            },

            // getTeams() {
            //     getUnPassTeam()
            //         .then(resp => {
            //             if (resp.data.result) {
            //                 resp.data.teams.forEach(team => {
            //                     this.teams.push({text: team.text, value: team.value});
            //                 });
            //             }
            //         })
            //         .catch(error => {
            //             this.error = error.response;
            //         })
            // }
        }
    }
</script>
