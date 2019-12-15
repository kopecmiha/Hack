<template>
    <v-footer
            color="primary lighten-1"
            padless
    >
        <v-row
                justify="center"
                no-gutters
        >

            <div v-for="link in links"
                 :key="link.href">
                <v-btn  color="white"
                        text
                        rounded
                        class="my-2"
                        @click="$router.push(link.href)"
                >
                    {{ link.name }}
                </v-btn>
            </div>
            <v-col
                    class="primary lighten-2 py-4 text-center white--text"
                    cols="12"
            >
                {{ new Date().getFullYear() }} — <strong>Admire</strong>
            </v-col>
        </v-row>
    </v-footer>
</template>

<script>
    export default {
        name: "FooterLayout",
        data: () => ({
            links: [
                {name: 'Главная', href:'/'}
            ],
        }),
    }
</script>

<style scoped>

</style>
