<template>
  <div id="forecast_icons">
    
  </div>
</template>
<script>
export default {
  name: "ForecastIcons",
  props: {
    values: Array
  },
  computed: {
    forecast: function() {
      let v = [];
      v[0] = [this.values[0][0], this.values[0][1]];
      let last_i = 0;
      for(int i=1;i<this.values.length;i++) {
        if (this.values[i][1] != this.values[last_i][1]) {
          v.push([this.values[i]); 
        } 
      }
      return v;
    }
  }
}
</script>
