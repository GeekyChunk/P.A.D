<template>
  <div class="container">
    <br>
    <br>
    <br>
    <div class="row">
      <div class="col">
         <MainChart :chartdata="datacollection" :options="options" />
      </div>
    </div>
  </div>
</template>

<script>
import MainChart from '../components/MainChart'


export default {
    components: {
      MainChart
    },
    data() {
      return {
        datacollection: {
          labels: [10, 23],
          datasets: [
            {
              label: 'asds',
              backgroundColor: '#f87979',
              data: [10, 12]
            }, {
              label: 'something',
              backgroundColor: 'blue',
              data: [15, 13]
            }
          ]
        },
        options: {
        responsive: true,
        maintainAspectRatio: false
      }
      }
    }
}
</script>
