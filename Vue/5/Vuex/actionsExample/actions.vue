<template></template>

<script>
import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    count: 10,
  },
  mutations: {
    increment(state, amount) {
      state.count += amount;
    },
  },
  actions: {
    incrementAction(ctx) {
      // 'increment'　ミューテーションを実行する
      ctx.commit("increment");
    },
  },
});

// store.dispatchでアクションを呼び出す
console.log(store.state.count); // -> 10
// 'incrementAction'アクションを呼び出す
store.dispatch("incrementAction");
console.log(store.state.count); // -> 11

export default {};
</script>