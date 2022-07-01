<template>
  <div class="new">
    NEW GAMES
    <game-list></game-list>
  </div>
</template>
<script>
// @ is an alias to /src
import GameList from '@/components/GameList'

export default {
  name: 'NewView',
  components: {
    GameList,
  },
  
}
</script>