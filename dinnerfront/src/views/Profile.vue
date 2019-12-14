<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
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

                <v-tab href="#tab-2">
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
                                <v-form>
                                    <v-text-field
                                            label="Заголовок"
                                    ></v-text-field>
                                </v-form>
                                <v-textarea
                                        solo
                                        name="input-7-4"
                                        label="Описание точки"
                                        class="mt-5"
                                ></v-textarea>
                                <!--Price-->
                                <v-col cols="12" sm="6" md="3">
                                    <v-text-field
                                            placeholder="Цена"
                                            prepend-icon="mdi-cash"
                                    ></v-text-field>
                                </v-col>
                                <!-- Calendar-->
                                <v-col cols="12" lg="6">
                                    <v-menu
                                            ref="menu1"
                                            v-model="menu1"
                                            :close-on-content-click="false"
                                            transition="scale-transition"
                                            offset-y
                                            full-width
                                            max-width="290px"
                                            min-width="290px"
                                    >
                                        <template v-slot:activator="{ on }">
                                            <v-text-field
                                                    v-model="dateFormatted"
                                                    label="Дата"
                                                    hint="Месяц/День/Год"
                                                    persistent-hint
                                                    prepend-icon="event"
                                                    @blur="date = parseDate(dateFormatted)"
                                                    v-on="on"
                                            ></v-text-field>
                                        </template>
                                        <v-date-picker v-model="date" no-title @input="menu1 = false"></v-date-picker>
                                    </v-menu>
                                </v-col>

                                <!-- modal button for map -->
                                <v-row>
                                    <v-dialog v-model="dialog" persistent max-width="290">
                                        <template v-slot:activator="{ on }">
                                            <v-btn color="red" dark v-on="on">Сменить местоположение</v-btn>
                                        </template>
                                        <v-card>
                                            <v-card-title class="headline"></v-card-title>
                                            <v-card-text></v-card-text>
                                            <v-card-actions>
                                                <v-spacer></v-spacer>
                                                <v-btn color="green darken-1" text @click="dialog = false">Disagree
                                                </v-btn>
                                                <v-btn color="green darken-1" text @click="dialog = false">Agree</v-btn>
                                            </v-card-actions>
                                        </v-card>
                                    </v-dialog>
                                    <v-btn class="ml-3" color="red" style="color: #fff">Сохранить</v-btn>
                                </v-row>
                            </v-col>
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
            menu1: false,
            rating1: 2,
            rating2: 2
        })
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
