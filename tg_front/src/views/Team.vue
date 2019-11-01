<template>
    <b-jumbotron
            bg-variant="white"
            container-fluid
            style="color:#002f55">
        <template v-slot:header>
            <b-row>
                <b-col>
                    <b-img center src="../img/TG.svg" alt="" width="72" height="72"></b-img>
                </b-col>
                <b-col>ТурГад</b-col>
            </b-row>
        </template>
        <b-container>
            <b-row v-if="showTeam">
                <h2>Команда:
                    <b-badge variant="success">{{team.title}}</b-badge>
                </h2>
            </b-row>
        </b-container>
        <hr>
        <b-form v-if="showReg">
            <b-form-group
                    label="Еще на зарегистрированы?"
                    label-for="regTitle">
                <b-form-input
                        id="regTitle"
                        v-model="team.title"
                        type="text"
                        required
                        placeholder="Введите название..."
                ></b-form-input>
            </b-form-group>
            <b-button type="button" variant="primary" @click="registration" block>Зарегистрировать</b-button>
        </b-form>
    </b-jumbotron>

</template>

<script>
    import {getTeamById, registerTeam} from '@/axios'

    export default {
        name: "Team",

        data() {
            return {
                team: {
                    id: 0,
                    title: null,
                    start: null,
                    finish: null
                },

                error: null,
            }
        },

        created() {
            this.getTeam(this.$route.params.id)
        },

        computed: {
            showReg() {
                return this.team.id == null
            },
            showTeam() {
                return this.team.title != null
            }
        },

        methods: {
            getTeam(id) {
                getTeamById(id)
                    .then(response => {
                        if (response.data.result) {
                            this.team.id = this.$route.params.id;
                            this.team.title = response.data.title;
                        } else {
                            this.team.id = null
                        }
                    })
                    .catch(error => {
                        this.error = error.response;
                    })
            },
            registration() {
                let team = {
                    'id': this.$route.params.id,
                    'name': this.team.title
                };

                registerTeam(team)
                    .then(response => {
                        this.team = response.data;
                    })
                    .catch(error => {
                        this.error = error.response;
                    })
            },
        }
    }
</script>