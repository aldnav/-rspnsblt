<template>
<div>
	<div class="words">	
        <div class="flashit"><h1>{{ currentWord }}</h1></div>
        <div class="forInput">
            <h1>ENTER ANSWER HERE:</h1>
            <input v-model="answer" class="input" type="text" v-on:keyup.enter="check">
            <!-- <button type="submit" class="play-btn" color="success" @click="check()" :disabled="submitted">ENTER</button> -->
        </div>
	</div>
</div>
</template>

<script>
export default {
    data: () => ({
		answer: '',
        currentWord: '',
        listOfWords: ["cook", "wash", "pick", "clean", "clean", "walk", "make"]
	}),
	mounted: function() {
        this.display();
    },
    methods: {
        display: function() {
            this.currentWord = this.listOfWords[Math.floor(Math.random() * this.listOfWords.length)];
        },
        check: function() {
            if (this.answer === this.currentWord) {
                console.log("Correct");
            }
        }
    }
}
</script>

<style scoped>
.words {
    width: 100%;
    background: white;
    border-radius: 5px;
    /* position: absolute; */
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    margin: auto;
    height: 854px;
    box-shadow: 5px 5px 25px #888888;
}
.play-btn {
    background-color: white !important;
    border-color: white !important;
    height: 30px;
    width: 50px;
}
.input {
  height: 30px;
  width: 250px;
  box-shadow: 1px 1px 3px #888888;
  padding: 20px;
  background: -webkit-gradient(linear, left top, left bottom, color-stop(0%, #FBFBFB), color-stop(100%, #E9E9E9));
}
.forInput {
    background-color: rgb(64, 248, 224);
    width: 100%;
    height: 200px;
    position: absolute;
    bottom: 0;
}
.flashit{
    color:black;
    animation-timing-function: linear;
    width: 100px;
    height: 50px;
    font-weight: bold;
    position: relative;
    -webkit-animation: mymove 5s infinite; /* Safari 4.0 - 8.0 */
    animation: mymove 2s infinite;
    animation-timing-function: linear;
}
@keyframes mymove {
    from {left: 0px;}
    to {left: 300px;}
}
</style>