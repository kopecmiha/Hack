<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
    <div>
        <div class="profile-info">
            <v-container>
                <v-row>
                    <v-col cols="12" md="4">
                        <!--avatar-->
                        <v-badge
                                :bottom="true"
                                :overlap="true"
                                class="align-self-center"
                                v-if="$store.state.userInfo.pasport_photo && $store.state.userInfo.pasport_photo.length != 0"
                        >
                            <template v-slot:badge>
                                <v-icon dark>
                                    mdi-check
                                </v-icon>
                            </template>
                            <template v-if="$store.state.userInfo.avatar && $store.state.userInfo.avatar.length != 0">
                                <img class="avatar" :src="$store.state.userInfo.avatar">
                            </template>
                            <template v-else>
                                <img class="avatar" src="../assets/no-avatar.jpg">
                            </template>
                        </v-badge>

                        <div v-else>
                            <template v-if="$store.state.userInfo.avatar && $store.state.userInfo.avatar.length != 0">
                                <img class="avatar" :src="$store.state.userInfo.avatar">
                            </template>
                            <template v-else>
                                <img class="avatar" src="../assets/no-avatar.jpg">
                            </template>
                        </div>

                    </v-col>
                    <v-col cols="12" md="7" class="user-info">
                        <!--profile info-->
                        {{$store.state.userInfo.FIO}} <br>

                        Возраст: {{birth}} лет
                    </v-col>
<!--                    <v-col cols="3">-->
<!--                        <div>-->
<!--                            <v-rating-->
<!--                                    v-model="rating1"-->
<!--                                    background-color="red lighten-3"-->
<!--                                    color="red"-->
<!--                            ></v-rating>-->
<!--                        </div>-->
<!--                        <div>-->
<!--                            <v-rating-->
<!--                                    v-model="rating2"-->
<!--                                    background-color="red lighten-3"-->
<!--                                    color="red"-->
<!--                            ></v-rating>-->
<!--                        </div>-->
<!--                    </v-col>-->
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
                <!--
                <v-tab href="#tab-1">
                    О пользователе
                    <v-icon>mdi-account</v-icon>
                </v-tab>-->

                <v-tab href="#tab-2" @click="tab2load()">
                    Настройки
                    <v-icon>mdi-settings</v-icon>
                </v-tab>
            </v-tabs>

            <v-tabs-items v-model="tab">

                <v-tab-item value="tab-1">
                    <v-container>
                        <v-card flat>

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
                                    <v-col cols="12" sm="7">
                                        <v-btn color="red" dark @click="mapRoute()">Сменить местоположение</v-btn>
                                    </v-col>
                                    <v-col cols="12" sm="5">
                                        <v-btn class="" color="red" style="color: #fff" @click="submit()">Сохранить</v-btn>
                                    </v-col>
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
        <footer-layout></footer-layout>
    </div>
</template>

<script>
    import { Editor, EditorContent, EditorMenuBar } from 'tiptap'
    import {
        Blockquote,
        CodeBlock,
        HardBreak,
        Heading,
        HorizontalRule,
        OrderedList,
        BulletList,
        ListItem,
        TodoItem,
        TodoList,
        Bold,
        Code,
        Italic,
        Link,
        Strike,
        Underline,
        History,
    } from 'tiptap-extensions'
    import FooterLayout from "../components/FooterLayout";
    export default {
        components: {
            FooterLayout,
            EditorContent,
            EditorMenuBar
        },
        name: "Profile",
        data: () => ({
            tab: "tab-2",
            ex11: false,
            menu1: false,
            rating1: 2,
            rating2: 2,
            dialog: false,
            snackbar: false,
            editor: null,
        }),
        computed: {
            // геттер вычисляемого значения
            birth: function () {
                // `this` указывает на экземпляр vm
                return this.calculateAge(new Date(this.$store.state.userInfo.birthday_date))
            }
        },
        mounted() {
            this.editor = new Editor({
                extensions: [
                    new Blockquote(),
                    new BulletList(),
                    new CodeBlock(),
                    new HardBreak(),
                    new Heading({ levels: [1, 2, 3] }),
                    new HorizontalRule(),
                    new ListItem(),
                    new OrderedList(),
                    new TodoItem(),
                    new TodoList(),
                    new Link(),
                    new Bold(),
                    new Code(),
                    new Italic(),
                    new Strike(),
                    new Underline(),
                    new History(),
                ],
                content: ""
            });

            this.axios.get('http://dinner-near.tw1.ru/user_id_status/'+this.$store.state.userInfo.id).then(a => {
                this.ex11 = a.data[0] === 1;
            });
        },
        beforeDestroy() {
            this.editor.destroy()
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
            },
            mapRoute() {
                this.$store.commit('addMeetingOn');
                this.$router.push('map');
            },
            calculateAge(birthday) { // birthday is a date
                var ageDifMs = Date.now() - birthday.getTime();
                var ageDate = new Date(ageDifMs); // miliseconds from epoch
                return Math.abs(ageDate.getUTCFullYear() - 1970);
            }
        }
    }
</script>

<style scoped>
    .avatar {
        max-width: 250px;
        width: 250px;
        border-radius: 5px;
    }

    .user-info {
        font-weight: bolder;
        font-size: 1.25em;
    }
</style>
