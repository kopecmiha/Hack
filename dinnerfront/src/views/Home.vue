<template>
    <div>
        <div class="home">
            <template>
                <v-carousel>
                    <v-carousel-item
                            v-for="(color, i) in colors"
                            :key="color"
                    >
                        <v-sheet
                                :color="color"
                                height="100%"
                                tile
                        >
                            <v-row
                                    class="fill-height"
                                    align="center"
                                    justify="center"
                            >
                                <div class="display-3">Slide {{ i + 1 }}</div>
                            </v-row>
                        </v-sheet>
                    </v-carousel-item>
                </v-carousel>
            </template>
            <br><br>
        </div>
        <footer-layout></footer-layout>
    </div>
</template>

<script>

import FooterLayout from "../components/FooterLayout";
export default {
    name: 'home',
    data () {
        return {
            colors: [
                'primary',
                'secondary',
                'yellow darken-2',
                'red',
                'orange',
            ],
        }
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
</style>
