<template>
<div>
    Serveur : <input type="text" v-model="serverUrl"><br>
    L'URL définie est : {{ serverUrl }}<br>
    Color de la led : <br>
    <ul>
        <li v-for="(colorValue, colorName) in ledColor" v-bind:key="colorName"> {{colorName}} : {{colorValue}}</li>
    </ul>

    <br><br>

</div>
</template>

<script>

export default {
  name: 'LedControl',
  data: function(){
      return {
          serverUrl: "http://localhost:5000",
          ledColor: { "red": 200, "blue": 200, "green": 200}
      }
  },
  methods: {
  }
}

</script>

<style scoped>
 /** La mise en forme en CSS va ici */
</style>

