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
    },
    isAddMeeting: false
  },
  mutations: {
    userinfo (state, payload) {
      state.isLogin = true;
      state.userInfo = payload;
      localStorage.setItem("l", payload.id);
    },
    logout(state) {
      state.isLogin = false;
      localStorage.removeItem("l");
    },
    addMeetingOn(state) {
      state.isAddMeeting = true;
    },
    addMeetingOff(state) {
      state.isAddMeeting = false;
    }
  }
});
var t = localStorage.getItem("l");
if (t) {
  axios.get('http://dinner-near.tw1.ru/database/user_view/' + t)
      .then(resp => {
         store.commit('userinfo', resp.data)
      });
}

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app');
