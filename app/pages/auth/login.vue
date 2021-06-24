<template>
	<div class="container">
		<div  v-if="msg" class="alert alert-danger">
			{{msg.msg}}
		</div>
		<div class="d-flex justify-content-center">
			
			<b-form @submit.prevent="Login" class="p-2" style="width: 30rem">
		    	<b-form-group
			        label="Username*"		        
			      >
			      	<b-form-input
			        	v-model="user.username"
			        	type="text"
			        	placeholder="Enter Username"
			        	required
			        ></b-form-input>
		    	</b-form-group>
		    	<b-form-group
			        label="Password*"
			      >
			      	<b-form-input
			        	v-model="user.password"
			        	type="password"
			        	placeholder="Enter Password"
			        	required
			        ></b-form-input>
		    	</b-form-group>
		    	<b-button type="submit" variant="primary" block>Submit</b-button>
		    </b-form>
		</div>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				user: {
					username: '',
					password: ''
				},
				msg: null
			}
		},
		methods: {
			async Login() {
				try {
					await this.$auth.loginWith('local', {
						data: this.user
					})
				} catch {
					this.msg = {
						var: 'danger',
						msg: 'En Error Reached Make Sure Username & Password Are Correct then try again'
					}
				}
				// alert(String(this.user.username) + "&" + String(this.user.password))
			}
		}
	}
	;
</script>