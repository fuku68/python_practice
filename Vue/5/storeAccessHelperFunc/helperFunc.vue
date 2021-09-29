<template>
  <div>
    <p>{{ count }}</p>
    <button v-on:click="increment(1)">+1</button>
  </div>
</template>

<script>
// mapState と mapMutations をインポート
import { mapState, mapMutations } from "vuex";

export default {
  // $store.count を this.countに結びつける
  computed: mapState(["count"]),
  //　$store.commit('increment',value) を
  // this.ingrement(value)で呼び出せるようにする
  methods: mapMutations(["increment"]),
};
</script>

