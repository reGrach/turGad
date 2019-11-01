<template>
  <div class="home">
<!--    <HelloWorld msg="Welcome to Your Vue.js App"/>-->
    <b-button variant="danger" @click="logout">Выход</b-button>

    <b-button variant="success" @click="check">check</b-button>

  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import { checkToken } from '@/axios'
export default {
  name: 'home',
  // components: {
  //   HelloWorld
  // }

  methods: {
    logout() {
      this.$store.dispatch('logout');
      this.$router.push('/login');
    },

    check() {
      const { id } = this.$store.state;
      checkToken(id).then(resp => console.log(resp.data))
    }
  }
}
</script>
