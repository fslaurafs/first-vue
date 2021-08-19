import Vue from 'vue'
import App from './App'
import vuetify from '@/plugins/vuetify' // path to vuetify export
import VueGoogleCharts from 'vue-google-charts'
import VueMqtt from 'vue-mqtt'

Vue.use(VueMqtt, 'IP MQTT');
Vue.use(VueGoogleCharts)

Vue.config.productionTip = false

new Vue({vuetify,
  render: h => h(App),
}).$mount('#app')
