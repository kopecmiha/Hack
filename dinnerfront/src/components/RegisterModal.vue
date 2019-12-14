<template>
    <v-dialog v-model="show" max-width="400px">
        <v-card>
            <div class="login">
                <div class="login-title">Регистрация</div>
                <div class="login-form">
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
                    </v-form>
                    <div class="my-2">
                        <v-btn class="login-button" large color="red">Зарегистрироваться</v-btn>
                    </div>
                </div>
            </div>
        </v-card>
    </v-dialog>
</template>

<script>
    export default {
        name: "RegisterModal",
        data: () => ({
            valid: false,
            form: {
                email: "",
                pass: "",
                passport: "",
                avatar: "",
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
        }
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
