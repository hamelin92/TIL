<template>
  <div class="review-list">
    <div v-if="this.gamename=='1to50'"><one-fifty></one-fifty></div>
    <div v-if="this.gamename=='1toINF'"><one-infinity></one-infinity></div>
    
    
    
  </div>
</template>

<script>
import OneFifty from '@/components/OneFifty.vue'
import OneInfinity from '@/components/OneInfinity.vue'

  export default {

    name : 'GameList',
    components: {
      OneFifty,
      OneInfinity
    },
    computed: {
      gamename: function() {
        console.log(this.$route)
        const name = this.$route.params.gamename
        return name
      }
    }

  }
</script>

<style>

</style>