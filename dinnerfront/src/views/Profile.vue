<template>
    <div>
        <div class="profile-info">
            <v-container>
                <v-row>
                    <v-col cols="9">
                        <v-row>
                            <v-col cols="6">
                                <!--avatar-->
                                
                            </v-col>
                            <v-col cols="6">
                                <!--profile info-->

                            </v-col>
                        </v-row>
                    </v-col>
                    <v-col cols="3">

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
                    <v-icon>mdi-phone</v-icon>
                </v-tab>

                <v-tab href="#tab-2">
                    Подписки
                    <v-icon>mdi-heart</v-icon>
                </v-tab>

                <v-tab href="#tab-3">
                    Настройки
                    <v-icon>mdi-account-box</v-icon>
                </v-tab>
            </v-tabs>

            <v-tabs-items v-model="tab">
                <v-tab-item
                        v-for="i in 3"
                        :key="i"
                        :value="'tab-' + i"
                >
                    <v-container>
                        <v-card flat>
                            <v-card-text>{{ text }}</v-card-text>
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
            tab: 0,
            text: "123"
        })
    }
</script>

<style scoped>

</style>
