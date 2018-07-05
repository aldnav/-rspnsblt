<template>


  <div id="app">
      <!-- <Countdown date="July 06, 2018"></Countdown> -->  
      <Countdown></Countdown>
      <div class="pepper-container">
          <div v-for="peper in counter" v-bind:key="peper" class="peppero">
            <pepper v-bind:style="pepperPosition"></pepper>
          </div>
      </div>
  </div>

</template>

<script>
import pepper from '~/components/pepper.vue';
import Countdown from '~/components/Countdown.vue';

export default {
    components:{ Countdown, pepper },
    data: () => ({
        counter: 25,
        pepperPosition: {
            right: 0,
            bottom: 0,
        },
    }),
    methods: {
        gameOver: function(event) {

        }
    },
    mounted() {
        var timer = document.getElementById("demo").text();
        if(timer.includes('15s')){
            this.counter++;
        }
    }
}


</script>

<style>
#app {
    width: 100%;
    height: 100%;
}

</style>