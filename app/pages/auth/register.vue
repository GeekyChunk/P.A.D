<template>
	<div class="container">
		<div  v-if="msg" class="alert alert-danger">
			{{msg.msg}}
		</div>
		<div class="d-flex justify-content-center">
			
			<b-form @submit.prevent="register" class="p-2" style="width: 30rem">
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
			        	v-model="user.password1"
			        	type="password"
			        	placeholder="Enter Password"
			        	required
			        ></b-form-input>
			        <ul class="text-muted mb-0 pb-0">
			        	<li>At Least 8 Charectors</li>
			        	<li> Fill All Fields </li>	
			        </ul>
		    	</b-form-group>
		    	<b-form-group
			        label="Password Confirmation*"
			      >
			      	<b-form-input
			        	v-model="user.password2"
			        	type="password"
			        	placeholder="Conform Password"
			        	required
			        ></b-form-input>
			        <ul class="text-muted mb-0 pb-0">
			        	<li>Same As Password Field</li>
			        </ul>
		    	</b-form-group>
		    	<div v-if="this.user.username">
		    		<div v-if="this.user.password1 == this.user.password2">
			    		<b-button type="submit" variant="primary" block>Register</b-button>
			    	</div>
			    	<div v-else>
		    			<b-button type="submit" variant="secondary" block disabled>Register</b-button>
			    	</div>
		    	</div>
		    	<div v-else>
		    		<b-button type="submit" variant="secondary" block disabled>Register</b-button>
		    	</div>
		    		
		    </b-form>
		</div>
	</div>
</template>

<script>
	export default {
		data() {
			return {
				user: {
					username: null,
					password1: null,
					password2: ''
				}
			}
		},
		methods: {
			register() {
				alert('sad')
			}
		}
	}

;
</script>