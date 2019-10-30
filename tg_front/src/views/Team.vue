<template>
    <b-jumbotron header="ТурГад">
        <b-form v-if="showReg">
            <b-form-group
                    label="Еще на зарегестрированы?"
                    label-for="regTitle">
                <b-form-input
                        id="regTitle"
                        v-model="team.title"
                        type="text"
                        required
                        placeholder="Введите название..."
                ></b-form-input>
            </b-form-group>
            <b-button type="button" variant="primary" @click="registration">Зарегестрировать</b-button>
        </b-form>
    </b-jumbotron>
</template>

<script>
export default {
    name: "Team",

    data() {
        return {
            team: {
                id: null,
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
        }
    },

    methods: {
        getTeam(id) {
            this.$api.get('/team/get/' + id)
                .then(response => {
                    if(response.data.result){
                        this.team.id = this.$route.params.id;
                        this.team.title = response.data.title;
                    }
                })
                .catch(error => {
                    this.error = error.response;
                })
        },
        registration() {
            let data = {
                'id': this.$route.params.id,
                'name': this.team.title
            };
            this.$api.post('/team/registration', data)
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