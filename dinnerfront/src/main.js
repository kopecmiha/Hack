import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import axios from 'axios';
import VueAxios from 'vue-axios';
import Vuex from 'vuex';

Vue.use(VueAxios, axios);
Vue.use(Vuex);

Vue.config.productionTip = false;

const store = new Vuex.Store({
  state: {
    prod: Vue.config.productionTip,
    isLogin: false,
    userInfo: {
      fio: "",
      date: new Date()
    }
  },
  mutations: {
    userinfo (state, payload) {
      state.isLogin = true;
      state.userInfo.fio = payload.fio;
    },
    logout(state) {
      state.isLogin = false;
    }
  }
})

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app');
