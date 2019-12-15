<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
    <div>
        <div class="profile-info" v-if="model">
            <v-container>
                <v-row>
                    <v-col cols="12" md="4">
                        <!--avatar-->
                        <v-badge
                                :bottom="true"
                                :overlap="true"
                                class="align-self-center"
                                v-if="model.pasport_photo && model.pasport_photo.length != 0"
                        >
                            <template v-slot:badge>
                                <v-icon dark>
                                    mdi-check
                                </v-icon>
                            </template>
                            <template v-if="model.avatar && model.avatar.length != 0">
                                <img class="avatar" :src="model.avatar">
                            </template>
                            <template v-else>
                                <img class="avatar" src="../assets/no-avatar.jpg">
                            </template>
                        </v-badge>

                        <div v-else>
                            <template v-if="model.avatar && model.avatar.length != 0">
                                <img class="avatar" :src="model.avatar">
                            </template>
                            <template v-else>
                                <img class="avatar" src="../assets/no-avatar.jpg">
                            </template>
                        </div>

                    </v-col>
                    <v-col cols="12" md="7" class="user-info">
                        <!--profile info-->
                        {{model.FIO}} <br>
                        Возраст: {{birth}} лет
                    </v-col>
                </v-row>
            </v-container>
        </div>
        <footer-layout></footer-layout>
    </div>
</template>

<script>
    import FooterLayout from "../components/FooterLayout";
    export default {
        name: "profileview",
        components: {FooterLayout},
        data: () => ({
            model: null
        }),
        computed: {
            // геттер вычисляемого значения
            birth: function () {
                // `this` указывает на экземпляр vm
                return this.calculateAge(new Date(this.model.birthday_date))
            }
        },
        mounted() {
            const id = this.$route.params.id;
            this.axios.get('http://dinner-near.tw1.ru/database/user_view/' + id)
                .then(resp => {
                    this.model = resp.data
                });
        },
        methods: {
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
