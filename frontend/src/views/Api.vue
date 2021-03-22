<template>
  <div class="commands-view">
    <ResultPopup :resPopup="this.resultPopup" @dPopup="deletePopup" v-if="this.resultPopup !== null"></ResultPopup>
    <div class="commands-header">
      <div class="headings">
        <div class="title-name">
          <h1>COMMANDS</h1>
        </div>
        <div class="sub-heading">
          <span>Add and remove commands for your Discord bot</span>
        </div>
      </div>

      <div class="user">
        <div class="user-profile-pic">
          <img :src="profileSrc">
        </div>
      </div>
    </div>
    <div class="commands">
      <div class="new-command">
        <div class="title-name">
          <h3>Add New Command</h3>
        </div>
        <div class="create-command">
          <input class="command-title" v-model="inputCommandName" placeholder="Enter a command name...">
          <textarea class="msgResponse" v-model="responseMsg" placeholder="Add a response to your command..."></textarea>
          <div class="addBtn">
            <button v-on:click="addCommand" :disabled="!isAddDisabled">Add Command</button>
          </div>
        </div>

      </div>
      <div class="title-name">
        <h3>Active Commands</h3>
      </div>
      <div class="command-container" >

        <ApiComponent :apiCommand="item" @dCommand="deleteCommand" v-for="item in commandData" :key="item.index"></ApiComponent>
      </div>
    </div>
  </div>

</template>

<script>
  import ApiComponent from '@/components/ApiComponent.vue'
  import ResultPopup from '@/components/ResultPopup.vue'
  import store from '../store'
  import {mapGetters} from 'vuex'
  import axios from 'axios';

  export default {
    name: 'About',
    components: {
      ApiComponent,
      ResultPopup,
    },
    props: {
      user: Object,
    },
    data() {
      return {
        reporters: [],
        commandData: {},
        newReporter: '',
        inputCommandName: '',
        resultPopup: null,
        popupTimeout: null,
        responseMsg: '',
        loggedIn: false,
        profileSrc: '',
      };
    },
    methods: {
      loadReporters: async function() {
        let url = this.$route.path.split('/');
        let guild = this.$route.path.split('/').pop();
        if (guild === '') {
          guild = url.pop();
        }
        let response = await axios.get('/api/commands/' + guild + '.json');
        //console.log(response);

        this.commandData = response.data;
        //console.log(this.commandData);
      },
      addCommand: async function() {
        let url = this.$route.path.split('/');
        let guild = this.$route.path.split('/').pop();
        if (guild === '') {
          guild = url.pop();
        }
        axios.defaults.xsrfCookieName = 'csrftoken';
        axios.defaults.xsrfHeaderName = 'X-CSRFToken';

        console.log(this.$route.path.split('/').pop());
        let response = await axios.post('/api/commands/' + guild + '.json', {
          guild: guild,
          cmd_name: this.inputCommandName,
          msg_response: this.responseMsg,
        });
        console.log(response);
        this.commandData = response.data;
      },
      deleteCommand: async function(item) {
        let url = this.$route.path.split('/');
        let guild = this.$route.path.split('/').pop();
        if (guild === '') {
          guild = url.pop();
        }
        axios.defaults.xsrfCookieName = 'csrftoken';
        axios.defaults.xsrfHeaderName = 'X-CSRFToken';
        let response = await axios.delete('/api/commands/delete/' + guild + '/' + item.pk + '/', {
          headers: { Authorization: 'Token token' },
        });
        this.resultPopup = item;
        let _this = this;
        this.popupTimeout = setTimeout(function () {
          _this.resultPopup = null;
        }, 3000);
        this.commandData = {};
        this.loadReporters();

      },
      deletePopup: function () {
        this.resultPopup = null;
        clearTimeout(this.popupTimeout);
        this.popupTimeout = null;
      },
    },
    computed: {
      ...mapGetters({
        curGuild: 'currentGuild'
      }),
      isAddDisabled() {
        return this.inputCommandName.length > 0 && this.responseMsg.length > 0;
      },
    },
    created() {
      this.loadReporters();
      this.profileSrc = 'https://cdn.discordapp.com/avatars/' + this.user.id + '/' + this.user.avatar + '.png';
    },
  }
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
