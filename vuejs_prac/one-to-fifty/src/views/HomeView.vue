<template>
  <div class="home">
    <one-fifty msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import OneFifty from '@/components/OneFifty.vue'

export default {
  name: 'HomeView',
  components: {
    OneFifty,
  }
}
</script>
