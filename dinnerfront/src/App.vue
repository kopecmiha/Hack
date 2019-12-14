<template>
  <v-app>
    <div>
      <v-toolbar>
        <v-toolbar-title>
<!--          <v-img class="logo" src="./assets/logo.png" height="80" max-width="100"></v-img>-->
        </v-toolbar-title>

        <v-spacer></v-spacer>

        <v-toolbar-items>
          <v-btn text @click.stop="showLogin=true">Вход</v-btn>
          <v-btn text @click.stop="showReg=true">Регистрация</v-btn>
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

<style scoped>
  .logo {
  }
</style>
