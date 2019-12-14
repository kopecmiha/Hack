<template>
    <div>
        <v-dialog v-model="show" max-width="400px">
            <v-card>
                <div class="login">
                    <div class="login-title">Вход</div>
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
                                    label="Эл.почта"
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
                        </v-form>
                        <v-divider></v-divider>
                        <div class="my-2">
                            <v-btn class="login-button" large color="red" v-on:click="submit()">Войти</v-btn>
                        </div>
                    </div>
                </div>
            </v-card>
        </v-dialog>

        <v-snackbar
                v-model="snackbar"
                :timeout="timeout"
        >
            Вход провален. Проверьте правильность ввода данных
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
        name: "LoginModal",
        data: () => ({
            snackbar: false,
            timeout: 2000,
            valid: true,
            form: {
                email: '',
                pass: '',
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
        methods: {
            submit() {
                if (this.$refs.form.validate()) {
                    var json = JSON.stringify(this.form);

                    this.axios.post('http://dinner-near.tw1.ru/login', {email: this.form.email, password: this.form.pass})
                    .then(resp => {
                        this.loginPass(resp.data);
                    }).catch(c => {
                        this.snackbar = true;
                    });
                }
            },
            loginPass(data) {
                console.log(data);
                // get user info
                this.axios.get('http://dinner-near.tw1.ru/database/user_view/' + data)
                    .then(resp => {
                        this.pushUserInfo(resp.data);
                    });
            },
            pushUserInfo(data) {
                this.$store.commit('userinfo', data)
                this.show = false;
            }
        }
    }
</script>

<style lang="scss" scoped>
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
        color: white;
    }
</style>
