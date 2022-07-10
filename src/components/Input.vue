<template>
  <div class="bg">
    <div class="title">
    <div class="titleleft"> hungry</div>
    <div class="titleright"> Volunteer</div>
    </div>
    <p class = "title2"> “You make a living by what you get.
      You make a life by what you give.” — Winston Churchill </p>
    <p class = "title2"> Start your volunteer career with a single click </p>
    <div class = "content">
        <p class = "label"> Enter a keyword </p>
        <input type="text" placeholder="Keyword" v-model="name" class ="inputstyle" required><br>
        <button class = "submit" v-on:click="navigate()">Submit</button>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Result',
  data() {
    return {
      name: '',
    };
  },
  methods: {
    navigate() {
      this.$router.push({
        name: 'Result',
        params: {
          name: this.name,
        },
      });
    },
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
    .title {
        font-family: Inter;
        font-style: normal;
        font-weight: bold;
        font-size: 44px;
        line-height: 50px;
        text-align: center;
        margin: 15px;
        margin-top: 30px;
        display:flex;
        flex-direction: row;
        justify-content: center;
    }
    .titleleft{
      color: black
    }
    .titleright{
      color: #68bced
    }
    .title2 {
        font-family: Inter;
        font-style: normal;
        font-weight: bold;
        font-size: 20px;
        line-height: 50px;
        text-align: center;
        margin: 15px;
    }
    .label {
        font-family: Inter;
        font-style: normal;
        font-weight: bold;
        font-size: 28px;
        line-height: 50px;
        text-align: center;
        margin: 15px;
    }
    .content {
        background-color: #E5E5E5;
        margin-top: 4%;
        margin-left: 35%;
        margin-right: 35%;
        height: 50%;
        width: 30%;
        justify-content: center;
        align-items: center;
        text-align: center;
        border-radius: 8px;
        padding: 10px;
        animation: zoomIn ease 0.7s
    }
    .inputstyle {
        font-family: Inter;
        padding: 8px;
        width: 80%;
        margin: 3%;
        font-size: 22px;
        border-radius: 8px;
        border: 1px solid #E5E5E5;
        height: 15%;
        margin-bottom: 7%;
    }
    .submit {
        background: #68bced;
        border-radius: 8px;
        border-color: #68bced;
        font-family: Inter;
        font-style: normal;
        font-weight: bold;
        font-size: 24px;
        line-height: 44px;
        text-align: center;
        width: 80%;
        height: 60px;
        margin: 3%;
        cursor: pointer;
        transition-duration: 0.4s;
    }
</style>
