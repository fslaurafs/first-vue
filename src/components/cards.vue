<template>
  <div>
    &emsp;&emsp;&emsp;
    <GChart
        :settings="{ packages: ['Gauge'] }"
        type="Gauge"
        :data="chartData"
        :options="chartOptions"
    />

    <br>

    &emsp;&emsp;&emsp;
    <v-btn fab light @click="up">
      <v-icon light>mdi-plus</v-icon>
    </v-btn>
    &emsp;
    <v-btn fab light @click="down">
      <v-icon light>mdi-minus</v-icon>
    </v-btn>
    &emsp;&emsp;&emsp;
    <br><br>
  </div>
</template>



<script>
export default {
  name: "cards",

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
        width: 500, height: 250,
        greenFrom: -100, greenTo: 100,
        redFrom: 100, redTo: 200,
        yellowFrom: -200, yellowTo: -100,
        minorTicks: 5, min: -200, max: 200
      },

      teste: 0
    }
  },

  mqtt: {
    'casa/#': function (val, topic) {
      let temp = String.fromCharCode.apply(null, val)
      console.log(temp)
      console.log(topic)
      this.chartData = [
        ['Label', 'Value'],
        ['Memory', Number(temp)],
        ['CPU', Number(temp)],
        ['Network', Number(temp)]
      ]
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
