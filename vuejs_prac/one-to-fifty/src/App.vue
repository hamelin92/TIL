<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <a href="/about">About</a>|
      <router-link to="/new">New</router-link>
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
