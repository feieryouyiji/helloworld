<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <Html2Canvas></Html2Canvas>
    <Drag></Drag>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Html2Canvas from './components/Html2Canvas.vue'
import Drag from './components/Drag.vue'

export default {
  name: 'app',
  components: {
    HelloWorld,
    Html2Canvas,
    Drag
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
