<template>
    <div class="result-popup" v-if="this.showPopup" v-on:click="removePopup">
        <div class="command-details">
            <span>Command {{ resPopup.fields.full_name }} was deleted.</span>
        </div>
    </div>
</template>

<script>
  export default {
    name: 'ResultPopup',
    props: {
      resPopup: Object,
    },
    data() {
      return {
        showPopup: true,
      };
    },
    methods: {
      removePopup: function() {
        this.showPopup = false;
        this.$emit('dPopup');
      }
    },
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    span {
        font-size: 12px;
        color: #fff;
        font-weight: bold;
        display: flex;
    }
    .result-popup {
        position: fixed;
        display: flex;
        align-items: center;
        top: 20px;
        right: 0;
        width: 200px;
        background: #ff645b;
        border-radius: 5px;
        margin: 0 20px 20px 0;
        z-index: 30;
        cursor: pointer;
        padding: 10px;
    }
</style>
