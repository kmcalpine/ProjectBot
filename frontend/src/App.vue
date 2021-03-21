<template>
  <div id="app">
    <Api :user="user"></Api>
  </div>
</template>

<script>
  import Api from '@/views/Api.vue'
  export default {
    name: 'About',
    components: {
      Api
    },
    props: {
      username: String,
      avatar: String,
      id: String,
    },
    data() {
      return {
        user: {
          username: '',
          avatar: '',
          id: ''
        }
      }
    },
    created() {
      console.log(this.username);
      this.user.username = this.username;
      this.user.avatar = this.avatar;
      this.user.id = this.id;
    }
  }
</script>

<style>

@import url('https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,200;0,300;0,400;0,600;0,700;0,800;0,900;1,200;1,300;1,400;1,600;1,700;1,800;1,900&display=swap');
body {
  margin: 0;

}
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  width: 100%;
  height: 100%;
  display: flex;
  background: #11121d;
  font-family: 'Nunito', sans-serif;
  min-height: 100vh;
}

#nav {
  align-items: center;
  min-width: 200px;
  min-height: 100%;
  background: #222330;
}

.nav-links {
  position: fixed;
  min-width: 200px;
}

.logo {
  display: flex;
  align-items: center;
  width: 100%;
  height: 75px;
  background: #0b0c17;
  text-decoration: none;
  font-weight: bold;
  font-size: 13px;
  color: #777a92;
  cursor: pointer;
}

.logo span {
  margin-left: 20px;
}

.nav-wrapper {
  display: inline-block;
  width: 100%;
}

.nav-item {
  display: flex;
  width: 100%;
  height: 50px;
  align-items: center;
  float: left;


}

#nav a {
  text-decoration: none;
  font-weight: bold;
  font-size: 13px;
  color: #777a92;
  float: left;
  margin-left: 20px;
}

#nav a.router-link-exact-active {
  color: #e4e5f1;
}
</style>
