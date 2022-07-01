<template>
  <div id="1to50-stan">
    <h1 @click="routerTest()">1 to 50</h1> ///// <span @click="clearListener"> CLEAR</span>
    <div style="background-color: brown; font-weight: bold;" @click="gameStart()">START</div>
    {{this.title}}
    {{this.seconds}}.{{this.mseconds}}
    <input type="button" @click="startTimer()" value="start">
    <input type="button" @click="resetTimer()" value="reset">
    <input type="button" @click="stopTimer()" value="stop">
    <h1> MISS:{{ $store.state.miss}} </h1>
    <div>
      <span class="test" id="q">
        <span style="font-weight: bold; font-size: 2rem">{{ $store.state.numbers_now['q']}}</span>
      </span>
      <span class="test" id="w">
        <span style="font-weight: bold; font-size: 2rem">{{ $store.state.numbers_now['w']}}</span>
      </span>
      <span class="test" id="e">
        <span style="font-weight: bold; font-size: 2rem">{{ $store.state.numbers_now['e']}}</span>
      </span>
    </div>
    <div>
      <span class="test" id="a">
        <span style="font-weight: bold; font-size: 2rem">{{ $store.state.numbers_now['a']}}</span>
      </span>
      <span class="test" id="s">
        <span style="font-weight: bold; font-size: 2rem">{{ $store.state.numbers_now['s']}}</span>
      </span>
      <span class="test" id="d">
        <span style="font-weight: bold; font-size: 2rem">{{ $store.state.numbers_now['d']}}</span>
      </span>
    </div>
    <div>
      <span class="test" id="z">
        <span style="font-weight: bold; font-size: 2rem">{{ $store.state.numbers_now['z']}}</span>
      </span>
      <span class="test" id="x">
        <span style="font-weight: bold; font-size: 2rem">{{ $store.state.numbers_now['x']}}</span>
      </span>
      <span class="test" id="c">
        <span style="font-weight: bold; font-size: 2rem">{{ $store.state.numbers_now['c']}}</span>
      </span>
    </div>
  </div>
</template>

<script>
// import _ from 'lodash'
import { mapActions } from 'vuex'

export default {
  name: 'OneFifty',
  data() {
    return {
      title: 'Timer',
      timer: null,
      totalTime: (0 * 6000),
      resetButton: false, 
      keyDown: function (e) {
        const key = document.getElementById(e.key);
        if (key) key.classList.add('pressed');
      },
      keyUp: (e) => {
        const key2 = document.getElementById(e.key);

        if (key2) key2.classList.remove('pressed');
        if (this.$store.state.numbers_now[e.key] == this.$store.state.number+1) {
          this.$store.commit('NUMBER_SETTER', e.key)
        } else if ((e.key in this.$store.state.numbers_now)) {
          this.$store.commit('COUNT_MISS')
          this.totalTime += 100
        }
        if (this.$store.state.number == 50) {
          this.$store.commit('STANDARD_FINISHED')
          this.stopTimer()
          console.log('finished')
        }
      }
    }
  },
  methods: {
    ...mapActions(['clearState']),
    routerTest() {
      console.log(this.$router)
      // this.$router.go('/new')
    },
    gameStart() { 
      this.resetTimer()
      this.startTimer()
      this.$store.commit('START')
      this.$store.commit('SETTER')
      this.$store.commit('STAN_NEXT_NUMS')
      document.addEventListener("keydown", this.keyDown);
      document.addEventListener("keyup", this.keyUp)
    },
    clearListener() {
      document.removeEventListener("keydown", this.keyDown);
      document.removeEventListener("keyup", this.keyUp)
    },
    startTimer: function() {
      this.timer = setInterval(() => this.countup(), 10);
      this.resetButton = true;
    },
    stopTimer: function() {
      clearInterval(this.timer);
      this.timer = null
      this.resetButton = true;
    },
    resetTimer: function() {
      this.totalTime = (0 * 6000);
      clearInterval(this.timer);
      this.timer = null;
      this.resetButton = false;
    },
    padTime: function(time) {
      return (time < 10 ? '0' : '') + time;
    },
    countup: function() {
      if(this.totalTime >= 0) {
        this.totalTime++;
      } else {
        this.totalTime = 0;
        this.resetTimer;
      }
    },
  },
  created() {
    return this.clearState
  },
  computed: {
    seconds: function() {
      const minutes = Math.floor(this.totalTime / 100);
      return this.padTime(minutes);
    },
    mseconds: function() {
      const seconds = this.totalTime - (this.seconds * 100);
      return this.padTime(seconds);
    },
  },
  mounted() {
  }
}
</script>

<style>
div {
  margin: 80px;
}
span {
  margin: 5px;
}
.test {
  font-size: 2rem;
  text-align: center;
  color: white;
  background: gray;
  border-radius: 1rem;
  padding: 2rem;
  transition: all .2s ease;
  margin-top: 3px;
}

.pressed {
  background: tomato;
  transform: scale(1.2);
}

</style>