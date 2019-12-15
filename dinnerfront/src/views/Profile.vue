<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
    <div>
        <div class="profile-info">
            <v-container>
                <v-row>
                    <v-col cols="9">
                        <v-row>
                            <v-col cols="3">
                                <!--avatar-->
                                <template v-if="$store.state.userInfo.avatar && $store.state.userInfo.avatar.length != 0">
                                    <img class="avatar" :src="$store.state.userInfo.avatar">
                                </template>
                                <template v-else>
                                    <img class="avatar" src="../assets/no-avatar.jpg">
                                </template>
                            </v-col>
                            <v-col cols="9" class="user-info">
                                <!--profile info-->
                                {{$store.state.userInfo.FIO}} <br>
                                Год рождения: {{new Date($store.state.userInfo.birthday_date).getFullYear()}}
                            </v-col>
                        </v-row>
                    </v-col>
                    <v-col cols="3">
                        <div>
                            <v-rating
                                    v-model="rating1"
                                    background-color="red lighten-3"
                                    color="red"
                            ></v-rating>
                        </div>
                        <div>
                            <v-rating
                                    v-model="rating2"
                                    background-color="red lighten-3"
                                    color="red"
                            ></v-rating>
                        </div>
                    </v-col>
                </v-row>
            </v-container>
        </div>
        <div class="profile-text">
            <v-tabs
                    v-model="tab"
                    background-color="red accent-4"
                    centered
                    dark
                    icons-and-text
            >
                <v-tabs-slider></v-tabs-slider>

                <v-tab href="#tab-1">
                    О пользователе
                    <v-icon>mdi-account</v-icon>
                </v-tab>

                <v-tab href="#tab-2" @click="tab2load()">
                    Настройки
                    <v-icon>mdi-settings</v-icon>
                </v-tab>
            </v-tabs>

            <v-tabs-items v-model="tab">
                <v-tab-item value="tab-1">
                    <v-container>
                        <v-card flat>
                            <v-card-text></v-card-text>
                        </v-card>
                    </v-container>
                </v-tab-item>
                <!--   point -->
                <v-tab-item value="tab-2">
                    <v-container>
                        <v-card flat>
                            <v-card-text></v-card-text>
                            <v-switch
                                    v-model="ex11"
                                    class="mx-2"
                                    color="red"
                                    label="Включить или выключить точку"
                                    hide-details>
                            </v-switch>
                            <v-col cols="12" md="6">

                                <!-- modal button for map -->
                                <v-row>
                                    <v-btn color="red" dark @click="mapRoute()">Сменить местоположение</v-btn>
                                    <v-btn class="ml-3" color="red" style="color: #fff" @click="submit()">Сохранить</v-btn>
                                </v-row>
                            </v-col>
                        </v-card>
                    </v-container>
                </v-tab-item>
            </v-tabs-items>
        </div>
        <v-snackbar
                v-model="snackbar"
                :timeout="2000"
        >
            Настройки сохранены
            <v-btn
                    color="blue"
                    text
                    @click="snackbar = false"
            >
                Закрыть
            </v-btn>
        </v-snackbar>
    </div>
</template>

<script>
    export default {
        name: "Profile",
        data: () => ({
            tab: "tab-1",
            ex11: false,
            menu1: false,
            rating1: 2,
            rating2: 2,
            dialog: false,
            snackbar: false
        }),
        mounted: function() {
        },
        methods: {
            submit() {
                this.axios.post('http://dinner-near.tw1.ru/status', {
                    status: this.ex11? 1: 0,
                    User_ID: this.$store.state.userInfo.id
                }).then(a => this.snackbar = true);
            },
            init() {

            },
            tab2load(){
                this.axios.get('http://dinner-near.tw1.ru/user_id_status/'+this.$store.state.userInfo.id).then(a => {
                    this.ex11 = a.data[0] === 1;
                });
            },
            mapRoute() {
                this.$store.commit('addMeetingOn');
                this.$router.push('map');
            }
        }
    }
</script>

<style scoped>
    .avatar {
        width: 200px;
    }

    .user-info {
        font-weight: bolder;
        font-size: 1.25em;
    }
</style>
