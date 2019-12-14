<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
    <v-dialog v-model="show" max-width="400px">
        <v-card>
            <div class="login">
                <div class="login-title">Регистрация</div>
                <div class="login-form">
                    <v-divider></v-divider>
                    <v-form
                            ref="form"
                            v-model="valid"
                    >
                        <v-text-field
                                class="mt-2"
                                v-model="form.email"
                                :rules="emailRules"
                                label="Эл. почта"
                                required
                                prepend-icon='email'
                        ></v-text-field>

                        <v-text-field
                                class="mt-2"
                                v-model="form.pass"
                                label="Пароль"
                                type="password"
                                required
                                prepend-icon='lock'
                        ></v-text-field>

                        <v-file-input
                                accept="image/png, image/jpeg, image/bmp"
                                placeholder="Загрузите аватар"
                                prepend-icon="mdi-camera"
                                label="Аватар"
                        ></v-file-input>

                        <v-file-input
                                accept="image/png, image/jpeg, image/bmp"
                                placeholder="Загрузите скан паспорта"
                                prepend-icon="mdi-camera"
                                label="Пасспорт"
                        ></v-file-input>
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
                                        label="Дата рождения"
                                        prepend-icon="event"
                                        @blur="date = parseDate(dateFormatted)"
                                        v-on="on"
                                ></v-text-field>
                            </template>
                            <v-date-picker v-model="date" no-title @input="menu1 = false" locale="ru"></v-date-picker>
                        </v-menu>

                        <v-text-field
                                class="mt-2"
                                v-model="form.series"
                                label="Серия паспорта"
                                required
                                prepend-icon='email'
                        ></v-text-field>

                        <v-text-field
                                class="mt-2"
                                v-model="form.number"
                                label="Номер паспорта"
                                required
                                prepend-icon='email'
                        ></v-text-field>
                        <v-divider></v-divider>
                    </v-form>
                    <div class="my-2">
                        <v-btn class="login-button" large color="red" v-on:click="submit()">Зарегистрироваться</v-btn>
                    </div>
                </div>
            </div>
        </v-card>
    </v-dialog>
</template>

<script>
    export default {
        name: "RegisterModal",
        data: vm => ({

            dateFormatted: vm.formatDate(new Date().toISOString().substr(0, 10)),
            date: new Date().toISOString().substr(0, 10),
            menu1: false,
            valid: false,
            form: {
                email: "",
                pass: "",
                passport: "",
                avatar: "",

                series: "",
                number: ""
            },
            emailRules: [
                v => !!v || 'E-mail is required',
                v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
            ],
        }),
        props: {
            value: Boolean
        },
        computed: {
            show: {
                get () {
                    return this.value
                },
                set (value) {
                    this.$emit('input', value)
                }
            }
        },

        watch: {
            date (val) {
                this.dateFormatted = this.formatDate(this.date)
            },
        },

        methods: {
            formatDate (date) {
                if (!date) return null

                const [year, month, day] = date.split('-')
                return `${day}.${month}.${year}`
            },
            parseDate (date) {
                if (!date) return null

                const [month, day, year] = date.split('/')
                return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
            },
            submit() {

            }
        },
    }
</script>

<style scoped>

    .login {
        padding: 16px;
    }
    .login-title {
        padding: 10px 25px;
        font-size: 1.5em;
        text-align: center;
    }
    .login-button {
        width: 100%;
        color: white!important;
    }
</style>
