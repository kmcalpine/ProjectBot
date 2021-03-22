<template>
  <div class="guilds-view">
    <Guild
        :guildData="this.guildsData"
        @uApiShow="this.updateApiShow">
    </Guild>
  </div>

</template>

<script>
  import Guild from '@/components/Guild.vue'
  import axios from 'axios';

  export default {
    name: 'Guilds',
    components: {
      Guild
    },
    props: {
    },
    data() {
      return {
        guildsData: {},
      };
    },
    methods: {
      getGuilds: async function(item) {
        axios.defaults.xsrfCookieName = 'csrftoken';
        axios.defaults.xsrfHeaderName = 'X-CSRFToken';
        let response = await axios.get('/guilds.json', {
          headers: { Authorization: 'Token token' },
        });
        console.log(response);
        this.guildsData = response;
      },
      updateApiShow: function () {

        console.log('updating api show');
        this.$emit('upApiView');
      },

    },
    computed: {
    },
    created() {
      this.getGuilds();
    }
  }
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .guilds-view {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .user {
    display: flex;
    margin-left: auto;
  }
  .user-profile-pic {
    display: flex;
    margin-left: auto;
    align-items: center;
  }
  .user-name {
    display: flex;
    align-items: center;
  }
  img {
    border-radius: 50%;
    height: 50%;
    margin-left: auto;
  }
  h1 {
    left: 0;
    float: left;
    color: aliceblue;
    font-weight: bold;
    margin: 0;
  }
  h3 {
    margin: 0;
    color: aliceblue;
    font-size: 16px;
  }
  span {
    float: left;
    color: #777a92;
    font-size: 13px;
  }
  .addBtn {
    margin-top: 20px;
  }
  .addBtn button {
    height: 50px;
    border-radius: 5px;
    background: #4ff8ff;
    color: #162832;
    font-weight: bold;
    font-size: 14px;
    font-family: 'Nunito', sans-serif;
    cursor: pointer;
    border: none;
    width: 420px;
  }
  button:hover {
    border: none;
  }
  button:disabled {
    background: #777a92;
    color: #9fa2bb;
    cursor: auto;
    border: 1px solid #777a92;
  }
  *:focus {
    outline: none;
  }
  .commands-view {
    padding: 50px;
    width: 100%;
    display: flex;
    flex-direction: column;
  }
  .commands-header {
    display: flex;
    flex-direction: row;
    float: left;
    align-items: center;
  }
  .new-command {
    float: left;
    margin-bottom: 50px;
  }
  .commands {
    display: flex;
    flex-direction: column;
    z-index: 20;
    float: left;
    background: #252632;
    padding: 50px;
    border-radius: 5px;
  }
  .command-title {
    height: 50px;
    border-radius: 5px;
    border: none;
    background: #161722;
    padding-left: 20px;
    font-size: 13px;
    font-family: 'Nunito', sans-serif;
    color: aliceblue;
    width: 400px;
  }
  .title-name {
    display: flex;
  }
  .command-container {
    display: flex;
    flex-flow: wrap;
  }
  .create-command {
    display: flex;
    flex-direction: column;
    margin-top: 20px;
    float: left;
  }
  .msgResponse {
    border-radius: 5px;
    border: none;
    background: #161722;
    padding-left: 20px;
    padding-top: 20px;
    font-size: 13px;
    font-family: 'Nunito', sans-serif;
    color: aliceblue;
    height: 100px;
    min-height: 40px;
    min-width: 400px;
    max-width: 400px;
    max-height: 300px;
  }
</style>
