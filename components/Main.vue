<template>
	<div class="wrapper">
		<div class="leaderboard"><leaderboard></leaderboard></div>
		<div class="game-wrapper">
			<Countdown></Countdown>
			<div class="pepper-container">
				<div v-for="peper in counter" v-bind:key="peper" class="peppero">
					<pepper v-bind:style="pepperPosition"></pepper>
				</div>
			</div>
			<Words/>
		</div>
	</div>
</template>


<script>
import axios from '~/plugins/axios';
import leaderboard from '~/components/leaderboard'
import Words from '~/components/Words.vue'
import pepper from '~/components/pepper.vue';
import Countdown from '~/components/Countdown.vue';

export default {
	components: { leaderboard, Words , pepper, Countdown},
	data: () => ({
		text: 'Anonymous',
		counter: 0,
        pepperPosition: {
            right: 0,
            bottom: 0,
        },
	}),
	mounted() {
		var that = this;
		setInterval(function() {
			that.counter++;
		}, 1000);
    }
};
</script>

<style scoped>
.wrapper {
	width: 100%;
	min-height: 100%;
	display: inline-block;
}
.leaderboard {
	min-width: 200px;
	width: 20%;
	height: 100%;
	border: 1px solid black;
	float: left;
	text-align: center;
}
.game-wrapper {
	float: left;
	height: 100%;
	width: 80%;
	border: 1px solid red;
	position: relative;
}
.pepper-container {
    height: 104vh;
    width: 70vh;
    display: flex;
    flex-direction: column;
    flex-wrap: wrap;
	z-index: 10;
}
</style>