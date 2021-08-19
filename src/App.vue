<template>
  <div id="app">
    <!--
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>

    <google></google>
    <br><hr><br>
    <gause></gause>
    -->

    <div>
      <div v-bind:class="{ bordaGreen: ficaVerde, bordaRed: ficaVermelho }">
        <cards></cards>
      </div>
      <div v-bind:class="{ bordaGreen: ficaVerde, bordaRed: ficaVermelho }">
        <cards></cards>
      </div>
      <div v-bind:class="{ bordaGreen: ficaVerde, bordaRed: ficaVermelho }">
        <cards></cards>
      </div>
      <div v-bind:class="{ bordaGreen: ficaVerde, bordaRed: ficaVermelho }">
        <cards></cards>
      </div>
      <div v-bind:class="{ bordaGreen: ficaVerde, bordaRed: ficaVermelho }">
        <cards></cards>
      </div>
      <div v-bind:class="{ bordaGreen: ficaVerde, bordaRed: ficaVermelho }">
        <cards></cards>
      </div>
    </div>
  </div>
</template>



<script>
// import HelloWorld from './components/HelloWorld.vue'
// import Google from "@/components/google";
// import Gause from "@/components/gause";
import Cards from "@/components/cards";

export default {
  components: {Cards},

  mounted() {
    this.$mqtt.subscribe('casa/#')
  },

  data() {
    return {
      ficaVerde: true,
      ficaVermelho: false
    }
  },

  mqtt: {
    'casa/#': function (val) {
      let temp = String.fromCharCode.apply(null, val)
      if (Number(temp) > 0) {
        this.ficaVerde = true
        this.ficaVermelho = false
      } else {
        this.ficaVerde = false
        this.ficaVermelho = true
      }
    }
  },
}

/*
export default {
  name: 'App',
  components: {HelloWorld}
}
*/
</script>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.bordaGreen {
  display: inline-block;
  border: 4px green ridge;
}

.bordaRed {
  display: inline-block;
  border: 4px red ridge;
}
</style>
