<template>
  <div class="about">
    <one-infinity></one-infinity>
  </div>
</template>
<script>
// @ is an alias to /src
import OneInfinity from '@/components/OneInfinity.vue'

export default {
  name: 'HomeView',
  components: {
    OneInfinity,
  }
}
</script>