<template>
  <div id="app">
    <nav>
      <a href="/">Home</a> |
      <a href="/about">About</a>|
      <a href="/new/1to50">1to50</a>.
      <a href="/new/1toINF">1toINF</a>.
      
      <!-- <router-link :to="{name: 'new', params: { gamename: '1to50'}}">1to50</router-link>
      <router-link :to="{name: 'new', params: { gamename: '1toINF'}}">1toINF</router-link> -->
    </nav>
    <router-view/>
  </div>
</template>
<script>
export default {
  name: 'App',
  data() {
    return {
     
    }
  }

}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
