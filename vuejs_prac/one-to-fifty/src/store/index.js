import Vue from 'vue'
import Vuex from 'vuex'
import _ from 'lodash'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    number: 0,
    ind_arr: [],
    numbers_next: [],
    numbers_now: {
      'q': null,
      'w': null,
      'e': null,
      'a': null,
      's': null,
      'd': null,
      'z': null,
      'x': null,
      'c': null,
    },
    miss: 0
  },
  getters: {
 
  },
  mutations: {
    STANDARD_FINISHED(state) {
      console.log(state)
      alert('끝!')
    },
    COUNT_MISS(state) {
      state.miss++
    },
    START(state) {
      console.log('start')
      state.ind_arr= _.shuffle(_.range(1,10))
      state.numbers_next=[
        ..._.shuffle(_.range(46,51)),
        ..._.shuffle(_.range(37,46)),
        ..._.shuffle(_.range(28,37)),
        ..._.shuffle(_.range(19,28)),
        ..._.shuffle(_.range(10,19)),
      ]
      console.log(state.numbers_next)
      state.number = 0
      state.miss = 0
    },
    NUM_NOW(state, res) {
      console.log('num_now')
      state.numbers_now[res[1]] = state.numbers_next.pop()
    },
    NUMBER_SETTER(state) {
      state.number++
    },
    SETTE(state) {
      console.log('sette')
      state.numbers_now['q'] = state.ind_arr[0]
      state.numbers_now['w'] = state.ind_arr[1]
      state.numbers_now['e'] = state.ind_arr[2]
      state.numbers_now['a'] = state.ind_arr[3]
      state.numbers_now['s'] = state.ind_arr[4]
      state.numbers_now['d'] = state.ind_arr[5]
      state.numbers_now['z'] = state.ind_arr[6]
      state.numbers_now['x'] = state.ind_arr[7]
      state.numbers_now['c'] = state.ind_arr[8]
    },
    
  },
  actions: {
  
    keyDown({commit}) {
      commit('START')
      commit('SETTE')


      
      window.addEventListener("keydown", e => {
        const key = document.getElementById(e.key);
        if (key) key.classList.add('pressed');
      });
      
      window.addEventListener("keyup", e => {
        const key = document.getElementById(e.key);
        if (key) key.classList.remove('pressed');

        if (this.state.numbers_now[e.key] == this.state.number+1) {
          commit('NUMBER_SETTER')
          let n = this.state.numbers_now[e.key]
          const res = [n, e.key]
          commit('NUM_NOW', res)
        } else {
          commit('COUNT_MISS')
        }

        if (this.state.number == 50) {
          commit('STANDARD_FINISHED')
        }
      });
    }
  },
  modules: {
  }
})
