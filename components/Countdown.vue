<template>
<p id="demo"></p>
</template>

<script>
export default {
    mounted(){
        var countDownDate = new Date("Sep 5, 2018 15:37:25").getTime();

// Update the count down every 1 second
        var x = setInterval(function() {

            // Get todays date and time
            var now = new Date().getTime();
            
            // Find the distance between now an the count down date
            var distance = countDownDate - now;
            
            // Time calculations for days, hours, minutes and seconds
            var seconds = Math.floor((distance % (1000 * 10)) / 1000);
            
            // Output the result in an element with id="demo"
            document.getElementById("demo").innerHTML =  seconds + "s ";
            
            // If the count down is over, write some text 
            if (distance < 0) {
                clearInterval(x);
                document.getElementById("demo").innerHTML = "EXPIRED";
            }
        }, 1000);
    }
}
</script>

<style scoped>
    #demo {
    align-items: center;
    justify-content: center;
    position: relative;
     text-align: center;
    
    }
</style>