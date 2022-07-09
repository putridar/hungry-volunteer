import Vue from 'vue';
import Router from 'vue-router';
import Input from '../components/Input.vue';
import Result from '../components/Result.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Input',
      component: Input,
      props: true,
    },
    {
      path: '/result',
      name: 'Result',
      component: Result,
      props: true,
    },
  ],
});
