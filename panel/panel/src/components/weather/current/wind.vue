<template>
  <div id="wind">
    {{ this.direction }}
  </div>
</template>
<script>
export default {
  name: "Wind",
  props: {
    degree: Number
  },
  computed: {
    direction: function() {
      let directions = [
        "NNW",
        "N",
        "NNE",
        "NE",
        "ENE",
        "E",
        "ESE",
        "SE",
        "SSE",
        "S",
        "SSW",
        "SW",
        "WSW",
        "W",
        "WNW",
        "NW",
        "NNW",
        "N"
      ];
      let index = Math.ceil(
        (this.degree / 22.5) + 0.5
      );
      let value = directions[index];
      return value;
    }
  }
}
</script>
<style scoped>

</style>
