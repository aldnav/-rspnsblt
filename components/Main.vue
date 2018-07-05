<template>
	<div class="wrapper">
		<div class="leaderboard"></div>
		<div class="game-wrapper"></div>
	</div>
</template>


<script>
import axios from '~/plugins/axios';

export default {
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
}


.leaderboard {
	min-width: 200px;
	width: 20%;
	height: 100%;
	border: 1px solid black;
}

.game-wrapper {
	height: 100%;
	border: 1px solid red;
}
</style>