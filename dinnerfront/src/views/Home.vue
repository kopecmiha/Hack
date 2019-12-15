<template>
    <div>
        <div class="home">
            <template>
                <v-carousel>
                    <v-carousel-item>
                        <div class="slider_next1"></div>
                    </v-carousel-item>
                    <v-carousel-item>
                        <div class="slider_next2"></div>
                    </v-carousel-item>
                    <v-carousel-item>
                        <div class="slider_next3"></div>
                    </v-carousel-item>
                </v-carousel>
            </template>
            <br><br>
            <!-- Card -->
            <v-row class="text-center">
                <template>
                    <v-card
                            class="mx-auto mt-4"
                            max-width="250"
                            width="250"
                    >
                        <v-row align="center" justify="center">
                            <v-img
                                    max-width="200px"
                                    src="../assets/p.png"
                            >
                            </v-img>
                        </v-row>


                        <v-card-title class="pb-0 headline red--text text-center" style="display: block">Простота
                        </v-card-title>

                        <v-card-text class="text--primary">

                            <div>Сервисом легко пользоваться</div>
                        </v-card-text>
                    </v-card>
                </template>

                <template>
                    <v-card
                            class="mx-auto mt-4"
                            max-width="250"
                            width="250"
                    >
                        <v-row align="center" justify="center">
                            <v-img
                                    max-width="200px"
                                    src="../assets/y.png"
                            >
                            </v-img>
                        </v-row>

                        <v-card-title class="pb-0 headline red--text" style="display: block">Удобство</v-card-title>

                        <v-card-text class="text--primary">

                            <div>Где вы бы не были, вы можете найти себе трапезу</div>
                        </v-card-text>
                    </v-card>
                </template>

                <template>
                    <v-card
                            class="mx-auto mt-4"
                            max-width="250"
                            width="250"
                    >
                        <v-row align="center" justify="center">
                            <v-img
                                    max-width="200px"
                                    src="../assets/a.png"
                            >
                            </v-img>
                        </v-row>

                        <v-card-title class="pb-0 headline red--text" style="display: block">Актуальность</v-card-title>

                        <v-card-text class="text--primary">

                            <div>Мы удовлетворяем потребность в дешёвой и вкусной еде</div>
                        </v-card-text>
                    </v-card>
                </template>

            </v-row>
            <!--     Удалить потом ,пометка для себя   -->
            <br><br>
        </div>
        <footer-layout></footer-layout>
    </div>
</template>

<script>

    import FooterLayout from "../components/FooterLayout";

    export default {
        name: 'home',
        data() {
            return {}
        },
        components: {
            FooterLayout
        },
    }
</script>

<style lang="scss" scoped>
    .home {

    }

    .home-logo {
        display: block;
        margin: auto;
    }

    .slider_next1 {
        background: url("../assets/1.jpg") no-repeat center;
        background-size: cover;
        height: 100%;
        width: 100%;
    }

    .slider_next2 {
        background: url("../assets/2.jpg") no-repeat center;
        background-size: cover;
        height: 100%;
        width: 100%;
    }

    .slider_next3 {
        background: url("../assets/3.jpg") no-repeat center;
        background-size: cover;
        height: 100%;
        width: 100%;
    }
</style>
