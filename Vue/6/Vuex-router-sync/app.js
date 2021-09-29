import Vue from "vue";
import Vuex from "vuex";
import VuexRouter from "vuex";

// npm install vuex-router-sync
import { sync } from "vuex-router-sync";

Vue.use(VuexRouter);
Vue.use(Vuex);

const router = new VuexRouter({
  route: [
    // ... ルーティングの定義 ...
  ],
});

// ストアを生成
const store = new Vuex.Store({
  //　...ストアの定義...
});

// ルーターとストアを同期する
sync(store, router);

// store.state.route以下にルーティングのデータが入る
console.log(store.state.route);
