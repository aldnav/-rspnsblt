<template>
	<div>
		<span><strong>{{ text }}</strong></span>
	</div>
</template>


<script>
import axios from '~/plugins/axios';

export default {
	data: () => ({
		text: 'Anonymous'
	}),

	mounted() {
		console.log('yo');
		axios.get('/ohyeah').then(response => {
			this.text = response.data;
		});
	}
};
</script>