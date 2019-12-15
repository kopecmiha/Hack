<template>
    <div>
        <v-btn
                color="red"
                v-if="$store.state.isAddMeeting"
                @click="$store.commit('addMeetingOn')"
                style="position: absolute;
    z-index: 1;
    color: white;
    bottom: 0;
    left: 0;
    right: 0;
    margin-left: auto;
    margin-right: auto;
    width: 256px;"
        >Выберите место на карте</v-btn>
        <div id="map">
        </div>
        <v-bottom-sheet v-model="sheet" v-if="sheet" inset>
            <v-sheet class="text-center" style="overflow: auto;">
                <div class="px-4 py-4 text-center">
                    <div class="marker-title">{{meetingToOpen.title}}</div>
                    <div>
                        <router-link :to="'/profileview/'+meetingToOpen.User.id">Добавил: {{meetingToOpen.User.FIO}}</router-link>
                    </div>
                    <p> Цена: {{meetingToOpen.price}}</p>
                    <p>Адрес: {{meetingToOpen.address}}</p>
                    <p class="mb-4">{{meetingToOpen.description}}</p>


                    <div style="height: 200px;
                                    overflow-x: auto;
                                    white-space: nowrap;
                                    overflow-y: hidden;" v-if="meetingToOpen.images.length != 0">
                        <img style="height: 100%; margin-right: 10px;" v-for="image of meetingToOpen.images" :src="image">
                    </div>

                    <v-btn class="text-white mt-2"
                           color="red"
                           @click="sheet = !sheet"
                    >Закрыть</v-btn>

                </div>
            </v-sheet>
        </v-bottom-sheet>
        <v-dialog v-model="addPlaceSheet" v-if="addPlaceSheet">
            <v-sheet class="text-center" style="overflow: auto;">
                <div class="text-right px-4 py-4">
                    <v-form
                            ref="form"
                    >
                        <div style="font-size: 1.5em; text-align: center;">Добавьте новое место</div>

                        <v-text-field
                                class="mt-2"
                                v-model="newPlace.title"
                                label="Название"
                                required
                                prepend-icon='mdi-email'/>

                        <v-text-field
                                class="mt-2"
                                v-model="newPlace.description"
                                label="Описание"
                                required
                                prepend-icon='mdi-lock'/>

<!--                        <v-text-field-->
<!--                                class="mt-2"-->
<!--                                label="Изображения"-->
<!--                                required-->
<!--                                prepend-icon='email'-->
<!--                                type="file"-->
<!--                                multiple-->
<!--                                accept="image/**"-->
<!--                                @change="addImages"/>-->

                        <v-file-input multiple label="Фото еды"
                                      accept="image/png, image/jpeg, image/bmp"
                                      prepend-icon="mdi-camera"
                                      @change="addImages"></v-file-input>
                        <div v-show="newPlace.images.length > 0" style="height: 200px;
overflow-x: auto; white-space: nowrap;
overflow-y: hidden; text-align: left;">
                            <img style="height: 100%; margin-right: 10px;" v-for="image of newPlace.images" :src="'data:image/jpg;base64,' + image">
                        </div>
<!--                        <div style="height: 200px;-->
<!--                                overflow-x: auto;-->
<!--                                white-space: nowrap;-->
<!--                                overflow-y: hidden;">-->
<!--                            <img style="height: 100%; margin-right: 10px;" v-for="image of newPlace.images" :src="'data:image/jpg;base64,' + image">-->
<!--                        </div>-->

                        <v-text-field
                                class="mt-2"
                                v-model="newPlace.price"
                                label="Цена"
                                required
                                type="number"
                                prepend-icon='mdi-email'/>

<!--                        <v-text-field-->
<!--                                class="mt-2"-->
<!--                                v-model="newPlace.FIO"-->
<!--                                label="ФИО"-->
<!--                                required-->
<!--                                prepend-icon='email'/>-->

                        <v-text-field
                                class="mt-2"
                                v-model="newPlace.address"
                                label="Адрес"
                                required
                                prepend-icon='mdi-email'/>
                        <v-divider/>
                    </v-form>
                    <div class="my-2">
                        <v-btn color="red" class="text-white"
                               @click="addPlaceSheet = !addPlaceSheet" style="float: left"
                        >Закрыть</v-btn>
                        <v-btn class="login-button text-white" color="red" style="float: right" @click="submitAddPlace()">Добавить место</v-btn>
                    </div>
                    <br>
                </div>
            </v-sheet>
        </v-dialog>
    </div>
</template>

<script>
    export default {
        name: "Map",
        data: function() {
            return {
                meetingGroup: new H.map.Group(),
                sheet: false,
                addPlaceSheet: false,
                meetingToOpen: {},
                newPlace: {
                    title: '',
                    description: '',
                    images: [],
                    price: 0,
                    User_ID: 0,
                    address: '',
                    lat: 0,
                    long: 0
                }
            }
        },
        mounted: function() {
            this.init();
        },
        methods: {
            init: function () {
                this.newPlace.User_ID = this.$store.state.userInfo.id;
                const app_id = 'UdRH6PlISTlADYsW6mzl';
                const app_code = 'lfrrTheP9nBedeJyy1NtIA';
                const app_key = 'jpqCEYkwL543JRJJb12V31gUT9AiwShHNSyqCTg4S4w';

                const platform = new H.service.Platform({
                    app_id  : app_id,
                    app_code: app_code,
                    useHTTPS: true
                });
                let blockId = 'map';
                let defaultLatitude = 44.73;
                let defaultLongitude = 37.76;
                let defaultZoom = 8;
                const pixelRatio    = window.devicePixelRatio || 1;
                const defaultLayers = platform.createDefaultLayers({
                    lg      : 'rus',
                    tileSize: pixelRatio === 1 ? 256      : 512,
                    ppi     : pixelRatio === 1 ? undefined: 320
                });

                window.map = new H.Map(
                    document.getElementById(blockId),
                    defaultLayers.normal.map,
                    {
                        zoom  : 8,
                        center: { lat: 55.58015026546139, lng: 37.266876548842674 }
                    },
                    {
                        pixelRatio: pixelRatio
                    });

                const behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));

                const ui = H.ui.UI.createDefault(map, defaultLayers, 'ru-RU');

                const mapSettings = ui.getControl('mapsettings');
                const zoom        = ui.getControl('zoom');
                const scalebar    = ui.getControl('scalebar');
                const pano        = ui.getControl('panorama');

                window.addEventListener('resize', () => {
                    map.getViewPort().resize();
                });

                map.addEventListener('tap', event => {
                    const coords = window.map.screenToGeo(event.currentPointer.viewportX,
                        event.currentPointer.viewportY);
                    console.log(coords);
                    if(this.$store.state.isAddMeeting) {
                        this.$store.commit('addMeetingOff');
                        this.addPlaceSheet = true;

                        this.newPlace.lat = coords.lat;
                        this.newPlace.long = coords.lng;
                        /*fetch(`https://reverse.geocoder.api.here.com/6.2/reversegeocode.json` +
                            `?app_id=${'fIeOFrHcuWktZtENNd0x'}` +
                            `?app_code=${app_code}` +
                            `?mode=retrieveAddresses` +
                            `&prox=` + coords.lat + `,` + coords.lng).then(response => response.text()).then(result => console.log(result));*/
                    }
                });

                map.addObject(this.meetingGroup);

                this.meetingGroup.addEventListener('tap', event => {
                    const data = event.target.getData();
                    console.info(data);
                    this.meetingToOpen = data;
                    this.sheet = true;
                });

                this.getMeetingPlaces();
            },
            getMeetingPlaces: function() {
                fetch('http://dinner-near.tw1.ru/database/point_view_all').then(response => response.json()).then(data => {

                    data.forEach(place => {
                        if (!isNaN(place.lat) && !isNaN(place.long))
                            this.addIconToMap(place);
                    });
                });
            },
            addIconToMap: function(meetingData) {
                if(typeof meetingData.images == 'string') {
                    meetingData.images = meetingData.images.split('::').filter(el => el !== '');
                }
                const icon = new H.map.DomIcon(`
                    <div>
                        <div style="position: relative; width: 1px; height: 1px;">
                            <img style="width: 30px; height: 44px;
                                margin-top: -44px; cursor: pointer;
                                margin-left: -15px; display: block;" src="/img/logo-mini.f49d760f.png">
                        </div>
                    </div>
                `);

                const marker = new H.map.DomMarker({lat: meetingData.lat, lng: meetingData.long}, {icon: icon,
                    min: 0,
                    max: 20
                });
                marker.setData(meetingData);
                this.meetingGroup.addObject(marker);
            },
            addImages: async function () {
                this.newPlace.images = [];
                const self = this;
                setTimeout(async function() {
                    for (const image of document.querySelector('input[type=file]').files) {
                        self.newPlace.images.push(await self.getBase64(image));
                    }
                }, 100);
            },
            submitAddPlace: async function () {
                this.newPlace.User_ID = this.$store.state.userInfo.id;
                this.axios.post('http://dinner-near.tw1.ru/database/point_add', this.newPlace)
                    .then(resp => {
                        this.meetingGroup.getObjects().forEach(icon => {
                            if(icon.getData().User.id === this.$store.state.userInfo.id) {
                                this.meetingGroup.removeObject(icon);
                            }
                        });
                        console.log(resp);
                        // const places = JSON.parse(localStorage.getItem('cashMeetings')) || [];
                        // places.push(this.newPlace);
                        // localStorage.setItem('cashMeetings', JSON.stringify(places));
                        this.addIconToMap({
                            title: this.newPlace.title,
                            description: this.newPlace.description,
                            images: this.newPlace.images,
                            price: this.newPlace.price,
                            address: this.newPlace.address,
                            lat: this.newPlace.lat,
                            long: this.newPlace.long,
                            User: this.$store.state.userInfo
                        });
                        this.newPlace = {
                            title: '',
                            description: '',
                            images: [],
                            price: 0,
                            User_ID: this.$store.state.userInfo.id,
                            address: '',
                            lat: 0,
                            long: 0
                        };
                        this.addPlaceSheet = false;
                    });
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
        }
    }
</script>

<style scoped>
    #map {
        width: 100%;
        height: calc(100vh - 64px);
    }
    .v-dialog--active {
        overflow: auto;
    }
    .text-white {
        color: white;
    }
</style>
