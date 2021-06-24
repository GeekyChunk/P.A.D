<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="info" fixed="" :sticky="true">
    <b-navbar-brand href="#">
      <span>
        P.A.D
      </span>
    </b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <NuxtLink to="/" class="nav-link mr-2 ml-2">
          Home
        </NuxtLink>
          
        <NuxtLink to="/auth/login" class="nav-link mr-2 ml-2">
          About
        </NuxtLink>

      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">

        <div v-if="$auth.loggedIn">
          <b-nav-item-dropdown class="mr-2 ml-2" right>
          <!-- Using 'button-content' slot -->
          <template #button-content>
            <em> {{$auth.user.username}} </em>
          </template>
          
          <NuxtLink to="/profile">
            <a role="menuitem" target="_self" class="dropdown-item">Profile</a>
          </NuxtLink>
            
          <NuxtLink to="/auth/logout">
            <a role="menuitem" target="_self" class="dropdown-item">Sign Out</a>
          </NuxtLink>

        </b-nav-item-dropdown>
        </div>

        <div class="d-flex" v-else>
          <NuxtLink to="/auth/login">
            <button class="btn btn-success text-white"> Login In </button>
          </NuxtLink>
            
        </div>

      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
    <Nuxt />
  </div>
</template>

<style> 
.nuxt-link-exact-active {
  color: #fff !important;
}
</style>