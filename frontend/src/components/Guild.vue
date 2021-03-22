<template>
  <div class="guild">
    <h2>Select your server</h2>
    <div class="guild-card" v-on:click="goTo(item.id)" v-for="item in this.guildData.data">
      <div class="guild-icon">
        <img :src=getIcon(item) v-if="item.icon !== null">
      </div>
      <div class="guild-name">

        <h4>{{ item.name }}</h4>
      </div>
    </div>

  </div>
</template>

<script>
  import axios from 'axios';
  export default {
    name: 'Guild',
    props: {
      guildData: Object,
    },
    data() {
      return {
        iconSrc: ''
      };
    },
    methods: {
      getIcon: function(data) {
        console.log(data);
        let src = "https://cdn.discordapp.com/icons/" + data.id + "/" + data.icon + ".png";
        return "https://cdn.discordapp.com/icons/" + data.id + "/" + data.icon + ".png";
      },
      goTo: function (id) {
        window.location.href = "http://127.0.0.1:8000/api/commands/" + id;
        this.$emit('uApiShow');
      },

    },
    created() {

    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h2 {
    color: aliceblue;
    margin-bottom: 50px;
  }
  h4 {
    color: aliceblue;
  }
  .guild {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    width: 100%;
  }
  .guild-card {
    display: flex;
    border-radius: 10px;
    align-items: center;
    width: 300px;
    height: 75px;
    margin-bottom: 20px;
    border: 1px solid #4242c7;
    background: #202055;
    cursor: pointer;
    padding: 20px;
  }
  .guild-card:hover {
    background: #29298f;
    border-radius: 10px;
    border: 1px solid #242466;
    transition: all 1s ease;
  }
  .guild-icon {
    width: 75px;
    height: 75px;
    border-radius: 50%;
    background: #080810;
    margin-right: 20px;
  }
  .guild-icon img{
    width: 75px;
    border-radius: 50%;
    background: #080810;
  }
</style>
