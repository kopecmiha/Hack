<template>
    <div>
        <div class="profile-info">
            <v-container>
                <v-row>
                    <v-col cols="9">
                        <v-row>
                            <v-col cols="3">
                                <!--avatar-->
                                <img class="avatar" src="../assets/no-avatar.jpg">
                            </v-col>
                            <v-col cols="9" class="user-info">
                                <!--profile info-->
                                {{$store.state.userInfo.fio}} <br>
                                Год рождения: {{$store.state.userInfo.date.getFullYear()}}
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

                <v-tab href="#tab-2">
                    Настройки
                    <v-icon>mdi-settings</v-icon>
                </v-tab>
            </v-tabs>

            <v-tabs-items v-model="tab">
                <v-tab-item value="tab-1">
                    <v-container>
                        <v-card flat>
                            <v-card-text>{{ text }}</v-card-text>
                        </v-card>
                    </v-container>
                </v-tab-item>
                <v-tab-item value="tab-2">
                    <v-container>
                        <v-card flat>
                            <v-card-text>{{ text }}</v-card-text>
                        </v-card>
                    </v-container>
                </v-tab-item>
            </v-tabs-items>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Profile",
        data: () => ({
            tab: "tab-1",
            text: "123",
            rating1: 2,
            rating2: 2
        })
    }
</script>

<style scoped>
    .avatar {
        width: 200px ;
    }
    .user-info {
        font-weight: bolder;
        font-size: 1.25em;
    }
</style>
