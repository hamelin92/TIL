import Vue from 'vue'
import Vuex from 'vuex'
import _ from 'lodash'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    number: 0,
    ind_arr: [],
    numbers_next: [],
    inf_num_next: [],
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
    EXTENSION(state, n) {
      state.inf_num_next.push(...[
        ..._.shuffle(_.range(n+10,n+19)),
      ])
      console.log(state.inf_num_next)
    },
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
      console.log(state.numbers_next)
      state.number = 0
      state.miss = 0
    },
    STAN_NEXT_NUMS(state) {
      state.numbers_next=[]
      state.numbers_next=[
        ..._.shuffle(_.range(46,51)),
        ..._.shuffle(_.range(37,46)),
        ..._.shuffle(_.range(28,37)),
        ..._.shuffle(_.range(19,28)),
        ..._.shuffle(_.range(10,19)),
      ]
    },
    INF_NEXT_NUMS(state) {
      state.inf_num_next=[
        ..._.shuffle(_.range(10,19)),
      ]
    },
    NUMBER_SETTER(state,res) {
      state.number++
      console.log('num_now')
      state.numbers_now[res] = state.numbers_next.pop()
    },
    INF_NUM_SETTER(state,res) {
      state.number++
      console.log('num_now')
      state.numbers_now[res] = state.inf_num_next.pop()
    },
    SETTER(state) {
      console.log('setter')
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
      commit('SETTER')
      commit('STAN_NEXT_NUMS')

      window.addEventListener("keydown", e => {
        const key = document.getElementById(e.key);
        if (key) key.classList.add('pressed');
      });
      
      window.addEventListener("keyup", e => {
        const key = document.getElementById(e.key);
        if (key) key.classList.remove('pressed');

        if (this.state.numbers_now[e.key] == this.state.number+1) {
          commit('NUMBER_SETTER', e.key)
        } else if ((e.key in this.state.numbers_now)) {
          commit('COUNT_MISS')
        }
        if (this.state.number == 50) {
          commit('STANDARD_FINISHED')
        }
      });
    },
    infMode({commit}) {
      commit('START')
      commit('SETTER')
      commit('INF_NEXT_NUMS')

      window.addEventListener("keydown", e => {
        const key = document.getElementById(e.key);
        if (key) key.classList.add('pressed');
      });
      
      window.addEventListener("keyup", e => {
        const key = document.getElementById(e.key);
        if (key) key.classList.remove('pressed');

        if (this.state.numbers_now[e.key] == this.state.number+1) {
          commit('INF_NUM_SETTER', e.key)
          if (this.state.number%9 == 0) {
            console.log(this.state.number)
            commit('EXTENSION', this.state.number)
          }
        } else if ((e.key in this.state.numbers_now)) {
          commit('COUNT_MISS')
        }
        
        // if (this.state.number == 50) {
        //   commit('STANDARD_FINISHED')
        // }
      });
    }
  },
  modules: {
  }
})
