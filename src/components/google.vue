<template>
  <div>
    <GChart
    type="ColumnChart"
    :data="chartData1"
    :options="chartOptions"
    />

    <GChart
    type="ColumnChart"
    :data="chartData2"
    :options="chartOptions2"
    />
  </div>
</template>



<script>
export default {
  name: "google",

  data () {
    return {
      // Array will be automatically processed with visualization.arrayToDataTable function
      chartData1: [
        ['Year', 'Sales', 'Expenses', 'Profit'],
        ['2014', 1000, 400, 200]
      ],

      chartData2: [
        ['Year', 'Sales'],
        ['2014', 200],
        ['2015', 250],
        ['2016', 300],
        ['2017', 350]
      ],

      chartOptions1: {
        chart: {
          title: 'Company Performance',
          subtitle: 'Sales, Expenses, and Profit: 2014-2017',
        }
      },

      chartOptions2: {
        chart: {
          title: 'Company Performance',
          subtitle: 'Sales, Expenses, and Profit: 2017-2020',
        }
      }
    }
  }
}
</script>



<style scoped>

</style>
