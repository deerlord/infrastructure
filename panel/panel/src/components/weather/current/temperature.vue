<template>
  <div id="temperature" :style="{'--color': this.color}">
    <Trend
      id="recent"
      :data="this.graph_data"
      :gradient="this.gradient"
      gradientDirection="top"
      :radius="12"
      :stroke-width="2"
      :width="100"
      :height="75"
      :max="100"
      :min="0"
      stroke-linecap="round"
      smooth
    ></Trend>
    <span id="current">
      {{ this.value }}°{{ this.units }}
    </span>
  </div>
</template>
<script>
import Trend from "vuetrend"

export default {
  name: "Temperature",
  props: {
    values: Array,
    units: String
  },
  components: {
    Trend
  },
  computed: {
    graph_data: function() {
      let result = [];
      let i = 0;
      for (i;i<this.values.length;i++) {
        let value = this.values[i][1];
        result.push(value);
      }
      return result;
    },
    value: function() {
      if (this.values.length) {
        return this.values[this.values.length - 1][1]
      }
      return null
    },
    color: function() {
      let tmp = 4;
      if (this.value > 100) {
        tmp = 0;
      } else if (this.value > 40) {
        tmp = Math.ceil((this.value - 40) / 20);
        tmp = Math.abs(tmp - 3) + 1;
      }
      return this.gradient[tmp];
    }
  },
  data() {
    return {
      gradient: [
        "#E82316",
        "#F59619",
        "#F5E919",
        "#1A84E4",
        "#1FF2EC",
      ],
    }
  }
}
</script>
<style scoped>
#recent {
  margin-right: 0px;
}
#current {
  margin-left: 0px;
  color: var(--color);
  font-weight: 900;
  font-size: 96px;
}
</style>
