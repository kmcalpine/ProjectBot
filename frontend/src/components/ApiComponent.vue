<template>
  <div class="api-command" v-if="this.activeCommand">
    <div class="command-details">

      <div class="api-name">
        <h3>!{{ apiCommand.fields.full_name }}</h3>
        <div class="del-command" v-on:click="deleteCommand">
          <span>X</span>
        </div>
      </div>
      <div class="api-key">
        <span>{{ apiCommand.fields.msg_response }}</span>
      </div>
    </div>

  </div>
</template>

<script>
  export default {
    name: 'ApiComponent',
    props: {
      apiCommand: Object,
    },
    data() {
      return {
        activeCommand: true
      };
    },
    methods: {
      deleteCommand: async function() {
        this.$emit('dCommand', this.apiCommand);
      }
    },
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .del-command {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 1rem;
    height: 1rem;
    background: #ff645b;
    cursor: pointer;
    margin-left: auto;
    border-radius: 5px;
    margin-top: -5px;
    margin-right: -5px;
  }
  .del-command span {
    color: #541700;
    font-weight: bold;
    font-size: 12px;
  }
  h3 {
    margin: 0 0 5px 0;
    float: left;
    color: aliceblue;
    font-size: 18px;
  }
  span {
    color: #a2aab1;
    font-size: 13px;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    color: #42b983;
  }
  .api-command {
    background: #161722;
    border-radius: 5px;
    display: flex;
    margin-top: 20px;
    margin-right: 20px;
    min-width: 320px;
    max-width: 320px;
    padding: 20px;
  }
  .command-details {
    display: flex;
    flex-direction: column;
    width: 100%;
  }
  .api-name {
    float: left;
    width: 100%;
  }
  .api-key {
    float: left;
    width: 100%;
  }
  .api-key span {
    word-wrap: break-word;
    white-space: normal;
    width: 320px;

  }
</style>
