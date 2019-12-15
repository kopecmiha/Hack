<template>
  <v-app>
    <div>
      <v-toolbar>
        <v-toolbar-title>
            <router-link to="/" class="logo">
                <img class="logo-img" src="./assets/logo-mini.png">
                <span class="logo-title">Dinner Near</span>
            </router-link>
<!--          <v-img class="logo" src="./assets/logo.png" height="80" max-width="100"></v-img>-->
        </v-toolbar-title>

        <v-spacer></v-spacer>

        <v-toolbar-items>
          <template v-if="$store.state.isLogin">
<!--            <v-btn text @click="$router.push('profile')">-->
<!--              <v-badge :overlap='true'>-->
<!--                <template v-slot:badge>0</template>-->
<!--                <v-icon>mdi-email</v-icon>-->
<!--              </v-badge>-->
<!--            </v-btn>-->
            <v-btn text @click="$router.push('/map')" class="logo-button"><span class="routerlink">Карта</span></v-btn>
            <v-btn text @click="$router.push('/profile')" class="logo-button"><span class="routerlink">Профиль</span></v-btn>
            <v-btn text @click="$store.commit('logout')" class="logo-button"><span class="routerlink">Выход</span></v-btn>
          </template>
          <template v-if="!$store.state.isLogin">
            <v-btn text @click.stop="showLogin=true" class="logo-button"><span class="routerlink">Вход</span></v-btn>
            <v-btn text @click.stop="showReg=true" class="logo-button"><span class="routerlink">Регистрация</span></v-btn>
          </template>
        </v-toolbar-items>
      </v-toolbar>
    </div>
    <v-content>
      <router-view></router-view>
    </v-content>
    <login-modal v-model="showLogin"></login-modal>
    <register-modal v-model="showReg"></register-modal>
  </v-app>
</template>

<script>

import RegisterModal from "./components/RegisterModal";
import LoginModal from "./components/LoginModal";
export default {
  name: 'App',

  components: {
    LoginModal,
    RegisterModal
  },

  data: () => ({
    showLogin: false,
    showReg: false
  }),
};
</script>

<style lang="scss">
    .notif {
      display: flex;
      align-items: center;
      margin-right: 20px;
    }
    .logo {
        display: flex;
        align-items: center;
        text-decoration: none;
    }
    .logo-img {
      max-height: 64px;
    }
    .logo-title {
        font-size: 1.5em;
        font-family: 'Pacifico', cursive;
        padding-left: 0.5em;
      @media (max-width: 540px) {
        display: none;
      }
    }
    .routerlink {
      text-decoration: none;
      color: #f44336
    }
    header {
      height: 64px!important;
      .v-toolbar__content {
        height: 64px!important;
      }
    }
    .logo-button {
      @media (max-width: 360px) {
        padding: 8px!important;
      }
    }
</style>
