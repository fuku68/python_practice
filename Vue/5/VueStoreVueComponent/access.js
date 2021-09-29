import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const store = new Vuex.Store({
  // ストアの定義を書く
});

new Vue({
  el: "#app",
  store, // ストアをコンポーネントに渡す
  render: (h) => h(App),
});
