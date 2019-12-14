<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
    <div>
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
                                    v-model="form.fio"
                                    label="ФИО"
                                    required
                                    prepend-icon='mdi-account'
                            ></v-text-field>

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
                                    v-model="form.avatar"
                            ></v-file-input>

                            <v-file-input
                                    accept="image/png, image/jpeg, image/bmp"
                                    placeholder="Загрузите скан паспорта"
                                    prepend-icon="mdi-camera"
                                    label="Паспорт"
                                    v-model="form.passport"
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

                            <v-radio-group v-model="form.sex" :mandatory="false" row>
                                <v-radio label="Мужской" value="М"></v-radio>
                                <v-radio label="Женский" value="Ж"></v-radio>
                            </v-radio-group>
                            <v-divider></v-divider>
                        </v-form>
                        <div class="my-2">
                            <v-btn class="login-button" large color="red" v-on:click="submit()">Зарегистрироваться</v-btn>
                        </div>
                    </div>
                </div>
            </v-card>
        </v-dialog>
        <v-snackbar
                v-model="snackbar"
                :timeout="timeout"
        >
            Ошибка в регистрации!
            <v-btn
                    color="blue"
                    text
                    @click="snackbar = false"
            >
                Закрыть
            </v-btn>
        </v-snackbar>
        <v-snackbar
                v-model="snackbarSuccess"
                :timeout="timeout"
        >
            Регистрация успешна, войдите в аккаунт
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
        name: "RegisterModal",
        data: vm => ({
            snackbar: false,
            snackbarSuccess: false,
            timeout: 2000,
            dateFormatted: vm.formatDate(new Date().toISOString().substr(0, 10)),
            date: new Date().toISOString().substr(0, 10),
            menu1: false,
            valid: false,
            form: {
                fio: "",
                email: "",
                pass: "",
                series: "",
                number: "",

                passport: [],
                avatar: [],
                sex: ""
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

                const [year, month, day] = date.split('-');
                return `${day}.${month}.${year}`
            },
            parseDate (date) {
                if (!date) return null;

                const [month, day, year] = date.split('/');
                return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`
            },
            submit() {
                if (this.$refs.form.validate()) {
                    var pas = this.getBase64(this.form.passport).then(p => {
                        var ava =  this.getBase64(this.form.avatar).then(a => {
                            var object = {
                                email: this.form.email,
                                password: this.form.pass,
                                pasport_number: this.form.series + this.form.number,
                                birthday_date: this.date,
                                pasport_photo: p,
                                avatar: a,
                                sex: this.form.sex,
                                fio: this.form.fio,
                                create_time: this.getDateString(new Date())
                            }
                            // alert(JSON.stringify(object));
                            this.axios.post('http://dinner-near.tw1.ru/regist', object)
                            .then(resp => {
                                this.show = false;
                                this.snackbarSuccess = true;
                            }).catch(c => {
                                this.snackbar = true;
                            });
                        });
                    });
                }
            },
            getDateString(date) {
                return  date.getFullYear() + '.' + ((date.getMonth() > 8) ? (date.getMonth() + 1) : ('0' + (date.getMonth() + 1))) + '.' + ((date.getDate() > 9) ? date.getDate() : ('0' + date.getDate()))
            },
            getBase64(file) {
                if (!file || file.length === 0)
                    return Promise.resolve("");
                return new Promise((resolve, reject) => {
                    const reader = new FileReader();
                    reader.readAsDataURL(file);
                    reader.onload = () => resolve(reader.result.split(',')[1]);
                    reader.onerror = error => reject(error);
                });
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
