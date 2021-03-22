import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    curGuild: '',
  },
  mutations: {
    change(state, currentGuild) {
      state.curGuild = currentGuild;
    }
  },
  getters: {
    currentGuild: state => {
      console.log('inside store: ' + state.curGuild);
      return state.curGuild;
    },
  },
  actions: {
  },
  modules: {
  }
})
