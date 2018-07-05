<template>
	<div class="wrapper">
		<div class="leaderboard"><leaderboard></leaderboard></div>
		<div class="game-wrapper">game</div>
	</div>
</template>


<script>
import axios from '~/plugins/axios';
import leaderboard from '~/components/leaderboard'

export default {
	components: {
    	leaderboard,
  	},
	data: () => ({
		text: 'Anonymous'
	}),

	mounted() {
		// console.log('yo');
		// axios.get('/ohyeah').then(response => {
		// 	this.text = response.data;
		// });
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
}
</style>