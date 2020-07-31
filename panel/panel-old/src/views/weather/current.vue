<template>
  <div id="app">
    {{ this.values }}
    <Temperature :values="this.values" :units="'F'"/>
    <Wind :degree="20"/>
  </div>
</template>

<script>
import Temperature from "../../components/weather/current/temperature.vue";
import Wind from "../../components/weather/current/wind.vue";
import Influx from "../../connections/influxdb.js";

export default {
  name: 'App',
  components: {
    Temperature,
    Wind
  },
  mounted() {
    this.values = Influx.current_temperature();
  },
  data() {
    return {
      old_values: [
        [1595600000, 32],
        [1595667593, 80],
        [1595667594, 80],
        [1595667595, 70],
        [1595667596, 74],
        [1595667597, 101],
      ],
      values: []
    }
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 60px;
}
</style5>
