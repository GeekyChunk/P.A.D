<template>
	<div>
		<div class="alert alert-danger">
			Logged Out
		</div>
	</div>
</template>


<script>
	export default {
		created() {
			this.$auth.logout(/* .... */)
		}
	}
	;
</script>