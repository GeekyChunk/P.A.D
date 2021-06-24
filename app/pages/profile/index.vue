<template>
	<div class="container">
		<div class="row d-flex justify-content-center">
		 	
    		<div class="col-md-10 mt-2 pt-5">

    		<div class="row z-depth-3">
    			<div class="col-sm-4 bg-info rounded">
    				<div class="card-block text-center text-white pt-3">
    					<img src="http://192.168.1.8/media/av.jpeg" alt="Profile" class="img-thumbnail rounded-circle">
    					<h2 class="font-weight-bold mt-4 text-capitalize"> 
                                <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
								  <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
								  <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
								</svg> 
                         </h2>
    					<p>
    						Edit Your Profile
    					</p>
    				</div>
    			</div>
    			<div class="col-sm-8 bg-white rounded-right">
    				<h3 class="mt-3 font-Info text-center text-capitalize"> {{prof.username}}'s Profile </h3>
    				<hr class="badge-primary mt-0 w-25">
    				
    				<div class="row">
    					<div class="col-sm-6">
    						<p class="font-weight-bold">First Name:</p>
    						<h6 class="text-muted"> 
    							<input v-model="prof.first_name" type="text" class="form-control">
    						</h6>
    					</div>
    					<div class="col-sm-6">
    						<p class="font-weight-bold">LastName:</p>
    						<h6 class="text-muted"> 
    							<input v-model="prof.last_name" type="text" class="form-control">
    						</h6>
    					</div>
    				</div>
    				<hr class="badge-light mt-0">
                    
    				<div class="row">
    					<div class="col-sm-6">
    						<p class="font-weight-bold">Email:</p>
    						<h6 class="text-muted">
    							<input v-model="prof.email" type="text" class="form-control">
    						</h6>
    					</div>
    					<div class="col-sm-6">
    						<p class="font-weight-bold">Gender:</p>
    						<b-form-select :options="options">
    							
    						</b-form-select>
    					</div>
    				</div>

                <div class="row mb-3 mt-2">
                    <div class="col-sm-12">

                    </div>
                </div>
                <div class="row mb-3 mt-2">
                    <div class="col-sm-12">
                    	<div class="d-flex btn-group">
                    		<button @click="discard" class="btn btn-danger">
                    			Discard
                    		</button>
                    		<button class="btn btn-success">
                    			Save<svg xmlns="http://www.w3.org/2000/svg" width="17" height="17" fill="currentColor" class="ml-1 bi bi-server" viewBox="0 0 16 16">
								  <path d="M1.333 2.667C1.333 1.194 4.318 0 8 0s6.667 1.194 6.667 2.667V4c0 1.473-2.985 2.667-6.667 2.667S1.333 5.473 1.333 4V2.667z"/>
								  <path d="M1.333 6.334v3C1.333 10.805 4.318 12 8 12s6.667-1.194 6.667-2.667V6.334a6.51 6.51 0 0 1-1.458.79C11.81 7.684 9.967 8 8 8c-1.966 0-3.809-.317-5.208-.876a6.508 6.508 0 0 1-1.458-.79z"/>
								  <path d="M14.667 11.668a6.51 6.51 0 0 1-1.458.789c-1.4.56-3.242.876-5.21.876-1.966 0-3.809-.316-5.208-.876a6.51 6.51 0 0 1-1.458-.79v1.666C1.333 14.806 4.318 16 8 16s6.667-1.194 6.667-2.667v-1.665z"/>
								</svg>
                    		</button>
                    	</div>
                    </div>
                </div>
    			</div>

    			</div>
    			
    		</div>
    	</div>
    </div>

	</div>	
</template>

<script>
import axios from 'axios'

	export default {
		data() {
			return {
				options: [
					{value: 'public', text: 'Public'},
					{value: 'private', text: 'Private'},

				],
				prof: {}
			}
		},
		created() {
			if (this.$auth.loggedIn) {
				let token = this.$auth.strategy.token.get()
				axios.get('http://127.0.0.1:8000/api/user/', {headers: {
					'Authorization': `${token}`
				}})
				.then(response => {this.prof = response.data.user})
			} else {
				this.$router.push('/auth/login')
			}
		},
		methods: {
			save() {
				// axios.post('http://127.0.0.1:8000/api/user/', prof, {headers: {

				// }})
				// .then(response => )
			},
			discard() {
				// let token = this.$auth.strategy.token.get()
				// axios.get('http://127.0.0.1:8000/api/user/', {headers: {
				// 	'Authorization': token
				// }})
				// .then(response => {this.prof = response.data.user})
				this.$router.push('/')
			}
		}
	}
;
</script>