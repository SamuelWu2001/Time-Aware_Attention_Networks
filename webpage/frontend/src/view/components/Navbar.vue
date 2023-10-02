
<template>
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <!-- <a class="navbar-brand " href="#"><router-link to="/Home"><img src="../../assets/home.png" height="40"></router-link></a> -->
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <!-- <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#"></a>
        </li> -->
        <li class="nav-item" v-if="'/Upload' === this.$route.path">
          <a class="nav-link" href="#"><router-link to="/Upload" class="nav-link label" style="background: rgb(159, 200, 222);"><label><b>Upload</b></label></router-link></a>
        </li>
        <li class="nav-item" v-else>
          <a class="nav-link" href="#"><router-link to="/Upload" class="nav-link label" style="background: white;"><label><b>Upload</b></label></router-link></a>
        </li>
        <li class="nav-item" v-if="'/History' === this.$route.path">
          <a class="nav-link" href="#"><router-link to="/History"  class="nav-link label" style="background: rgb(159, 200, 222);"><b>History</b></router-link></a>
        </li>
        <li class="nav-item" v-else>
          <a class="nav-link" href="#"><router-link to="/History"  class="nav-link label" style="background: white;"><b>History</b></router-link></a>
        </li>
        <!-- <li class="nav-item" v-if="'/Tutorial' === this.$route.path">
          <a class="nav-link" href="#"><router-link to="/Tutorial"  class="nav-link label" style="background: rgb(159, 200, 222);"><b>Tutorial</b></router-link></a>
        </li>
        <li class="nav-item" v-else>
          <a class="nav-link" href="#"><router-link to="/Tutorial"  class="nav-link label" style="background: white;"><b>Tutorial</b></router-link></a>
        </li> -->
        <li class="nav-item" v-if="'/Patient' === this.$route.path">
          <a class="nav-link" href="#"><router-link to="/Patient"  class="nav-link label" style="background: rgb(159, 200, 222);"><b>Patient data</b></router-link></a>
        </li>
        <li class="nav-item" v-else>
          <a class="nav-link" href="#"><router-link to="/Patient"  class="nav-link label" style="background: white;"><b>Patient data</b></router-link></a>
        </li>
        <!-- <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li> -->
        <!-- <li class="nav-item">
          <a class="nav-link disabled">Disabled</a>
        </li> -->
      </ul>
      <!-- <form class="d-flex">
        <input class="form-control me-4"  v-show="url === this.$route.path" type="search" placeholder="PatientID" aria-label="Search">
        <button class="btn btn-outline-success me-2" v-show="url === this.$route.path" type="submit">Search</button>
        <button class="btn btn-outline-success me-2" v-show="url === this.$route.path" type="submit">Add</button>
        <button class="btn btn-outline-success me-3" v-show="url === this.$route.path" type="submit">Update</button>
      </form> -->
    </div>
  </div>
</nav>
</template>

<script>

export default {
  data() {
    return{
      url : "/Patient",
    };
  },
}
</script>


<style>
    .label{
      border-radius:15px;
    }
</style>
