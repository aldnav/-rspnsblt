<template>
	<div>
		<h1>Leaderboard</h1>
		<div class="board">
			<table>
				<tr>
				    <th>ID</th>
				    <th>Name</th> 
				    <th>Score</th>
				</tr>
				<tr v-for="record in records">
					<th>{{record.id}}</th>
					<th>{{record.name}}</th>
					<th>{{record.score}}</th>
				</tr>
			</table>
		</div>
	</div>
</template>

<script>
	export default{
		data: () => ({
			records: [{
				id:1,
				name:"Joe",
				score: 999,
			},{
				id:2,
				name:"Joey",
				score: 999,
			}]
		})
	}
</script>

<style scoped>
	.board {
		min-width: 200px;s
		width: 100%;
		height: 100%;
		text-align: center;
		display: flex;
		justify-content: center;
	}
	.board table{
		width: 100%;
	}
</style>