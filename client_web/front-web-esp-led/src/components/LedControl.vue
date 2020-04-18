<template>
<div>
    Serveur : <input type="text" v-model="serverUrl"><br>
    L'URL définie est : {{ serverUrl }}<br>
    Color de la led : <br>
    <ul>
        <li v-for="(colorValue, colorName) in ledColor" v-bind:key="colorName"> {{colorName}} : {{colorValue}}</li>
    </ul>

    <br><br>
    <button v-on:click="setLed">Set LED</button>
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LedControl',
  data: function(){
      return {
          serverUrl: "http://localhost:5000",
          ledColor: { "red": 200, "blue": 200, "green": 200}
      }
  },
  methods: {
      setLed(){
          var vm = this;
          axios.post(vm.serverUrl+"/pixel/1", vm.ledColor);
      }
  }
}

</script>

<style scoped>
 /** La mise en forme en CSS va ici */
</style>

