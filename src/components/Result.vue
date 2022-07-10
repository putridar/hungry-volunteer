<template>
  <div class="bg">
    <div class="title">
      <button class = "submit2" v-on:click="back()">Try other keyword</button>
      <button class = "submit2" v-on:click="getMessage()">Refresh</button>
      <p class="name">{{this.name}}</p><br><br>
    </div>
    <div v-if="this.result == 'Loading...'">{{this.result}}</div>
    <div class="bottom">
      <div v-if="this.result != 'Loading...'">
          <ul>
            <li v-for="(value, name, index) in this.result" :key="index" class="list">
              <div class="listcontent">
              <div class="titlecontent">{{ value }}</div>
              <button class="submit" v-on:click="visit(name)">Visit</button>
              </div>
            </li>
          </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Result',
  props: ['name'],
  components: {
  },
  data() {
    return {
      result: 'Loading...',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/scrape';
      axios.post(path, { name: this.name })
        .then((res) => {
          this.result = res.data;
        });
    },
    back() {
      this.$router.push({
        name: 'Input',
      });
    },
    visit(link) {
      window.open(link, '_blank');
    },
  },
  mounted() {
    this.getMessage();
  },
};
</script>

<style scoped>
    @import url('https://fonts.googleapis.com/css?family=Inter');
    .bg {
        justify-content: center;
        align-items: center;
        text-align: center;
    }
    .name {
        font-family: Inter;
        font-style: normal;
        font-weight: bold;
        font-size: 60px;
        line-height: 58px;
        text-align: center;
        margin: 3vh;
        color: #1F335C;
        margin-bottom: 0vh;
        margin-right: 8vw;
        margin-left: 12vw;
    }
    .title {
      display: flex;
      justify-content:center;
      text-align: center;
    }
    .left {
      float: left;
      margin-left: 2vw;
      width: 30vw;
    }
    .right {
      margin-left: 37vw;
      width: 55vw;
      margin-top: 0vh;
      border-radius: 8px;
      height: 60vh;
    }
    .bottom {
      display: flex;
      justify-content:center;
      text-align: center;
    }
    .submit {
      background: #68bced;
      border-radius: 8px;
      border-color: #68bced;
      font-family: Inter;
      font-style: normal;
      font-weight: bold;
      font-size: 16px;
      line-height: 4vh;
      text-align: center;
      width: 20vw;
      height: 7vh;
      margin: 5vh;
      cursor: pointer;
      transition-duration: 0.4s;
      margin-top: 2.5vh;
    }
    .submit2 {
      background: #68bced;
      border-radius: 8px;
      border-color: #68bced;
      font-family: Inter;
      font-style: normal;
      font-weight: bold;
      font-size: 22px;
      line-height: 4vh;
      text-align: center;
      width: 17vw;
      height: 10vh;
      margin: 5vh;
      margin-left: 5vh;
      cursor: pointer;
      transition-duration: 0.4s;
      margin-top: 2.5vh;
    }
    ul {
      display: flex;
      flex-wrap: wrap;
      list-style-type: none;
      padding: 0;
      justify-content: center;
    }
    .list {
      display:flex;
      flex-direction:row;
      justify-content:center;
      text-align: center;
      padding: 3vh;
      margin: 2vh;
      border-radius: 10px;
      background-color: #F5F5F5;
      color: black;
      width: 20vw;
      height: 30vh;
      margin-top: 0vh;
    }
    .listcontent {
      display:flex;
      flex-direction:column;
      justify-content: center;
    }
    .titlecontent {
      width: 20vw;
      text-align: center;
      padding: 3vh;
      margin-left: 2vh;
      display: flex;
      justify-content: center;
    }
</style>
