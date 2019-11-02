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

        <b-form v-if="showReg">
            <hr>
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

        <div v-if="showTeam">
            <b-container>
                <b-row>
                    <h3>Команда:
                        <b-badge variant="success">{{team.title}}</b-badge>
                    </h3>
                </b-row>
                <b-row>
                    <h3>Контрольное время:
                        <b-badge variant="success">{{getStrControlTime}}</b-badge>
                    </h3>
                </b-row>
            </b-container>

            <div v-if="this.$store.getters.isAuthenticated">
                <b-button variant="success" @click="fixStage" block>{{stageType}}</b-button>
                <hr>
            </div>

        </div>
    </b-jumbotron>

</template>

<script>
    import {getTeamById, registerTeam, setEndMark} from '@/axios'

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

                controlTime: new Date(0).setMinutes(120),
                timer: null,

                error: null,
            }
        },

        created() {
            this.getTeam(this.$route.params.id)
        },

        watch: {
            controlTime(time) {
                if (time <= 0) {
                    this.stopTimer()
                }
            }
        },

        computed: {
            showReg() {
                return this.team.id == null;
            },
            showTeam() {
                return this.team.id > 0;
            },
            stageType() {
                if (this.$store.getters.isMain) {
                    if (this.team.start) return 'Финиш';
                    else return 'Старт';
                } else return 'Пройти этап';
            },

            calcDeltaMillisec() {
                let ct = this.team.start.split(':');
                return new Date().setHours(ct[0], ct[1], ct[2]) - new Date().getTime() + 2*60*60*1000;
            },

            getStrControlTime() {
                let time = new Date(this.controlTime).getTime() - 3*60*60*1000;
                let minutes = 0;
                if (new Date(time).getHours() > 0)
                    minutes = 60 * new Date(time).getHours() + Number(new Date(time).getMinutes());
                else minutes = new Date(time).getMinutes();
                return minutes + ':' + new Date(time).getSeconds().toString()
            }


        },

        destroyed() {
            this.stopTimer()
        },

        methods: {
            getTeam(id) {
                getTeamById(id)
                    .then(response => {
                        if (response.data.result) {
                            this.team.id = this.$route.params.id;
                            this.team.title = response.data.team.title;
                            this.team.start = response.data.team.start;
                            this.team.finish = response.data.team.finish;
                            if (this.team.start && this.team.finish === '') {
                                this.controlTime = this.calcDeltaMillisec;
                                this.startTimer();
                            }

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

            fixStage() {
                if (this.$store.getters.isMain) {
                    setEndMark(this.team.start, this.team.id)
                        .then(resp => {
                            if (resp.data.result) {
                                if (resp.data.start) {
                                    this.team.start = resp.data.start;
                                    this.this.controlTime = this.calcDeltaMillisec;
                                    this.startTimer();
                                }
                                if (resp.data.finish) {
                                    this.team.finish = resp.data.finish;
                                    this.stopTimer();
                                }

                            }

                        })
                        .catch(error => {
                            console.log(error.response)
                        })
                }

            },

            startTimer() {
                this.timer = setInterval(() => {
                    this.controlTime -= 1000;
                }, 1000)
            },

            stopTimer() {
                clearTimeout(this.timer)
            },

        }
    }
</script>