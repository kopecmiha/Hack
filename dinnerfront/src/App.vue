<template>
  <v-app>
    <div>
      <v-toolbar>
        <v-toolbar-title>Title</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-toolbar-items>
          <v-btn text>Вход</v-btn>
          <v-btn text>Регистрация</v-btn>
        </v-toolbar-items>
      </v-toolbar>
    </div>
    <v-content>
      <HelloWorld/>
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld';

export default {
  name: 'App',

  components: {
    HelloWorld,
  },

  data: () => ({

  }),
};
</script>
