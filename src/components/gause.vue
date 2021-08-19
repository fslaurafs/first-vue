<template>
  <div>
    <!-- <p>{{teste}}</p> -->
    <GChart
        :settings="{ packages: ['Gauge'] }"
        type="Gauge"
        :data="chartData"
        :options="chartOptions"
    />

    <p><v-btn @click="up">+</v-btn> | <v-btn @click="down">-</v-btn></p>
  </div>
</template>



<script>
export default {
  name: "gause",

  data() {
    return {
      // Array will be automatically processed with visualization.arrayToDataTable function
      chartData: [
        ['Label', 'Value'],
        ['Memory', 0],
        ['CPU', 0],
        ['Network', 0]
      ],

      chartOptions: {
        width: 500, height: 200,
        greenFrom: -100, greenTo: 100,
        redFrom: 100, redTo: 200,
        yellowFrom: -200, yellowTo: -100,
        minorTicks: 5, min: -200, max: 200
      },

      teste: 0
    }
  },

  methods: {
    down: function () {
      this.teste = this.teste - 1
      console.log('down', this.teste)
      this.chartData = [
        ['Label', 'Value'],
        ['Memory', this.teste],
        ['CPU', this.teste * 5],
        ['Network', this.teste * 10]
      ]
    },

    up: function () {
      this.teste += 1
      console.log('up', this.teste)
      this.chartData = [
        ['Label', 'Value'],
        ['Memory', this.teste],
        ['CPU', this.teste * 5],
        ['Network', this.teste * 10]
      ]
    }
  }
}
</script>



<style scoped>

</style>
