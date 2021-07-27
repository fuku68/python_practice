<template>
  <div id="app">
    <h1 class="greeting">メッセージ：{{ msg }}</h1>
    <Content />
  </div>
</template>
<template src="./template.html"></template>
<template src="./script.js"></template>
<template src="./style.css"></template>

<script>
// import Content from "./content.vue";

export default {
  //   component: {
  //     Content,
  //   },
  data() {
    return { msg: "こんにちは！" };
  },
};
</script>

<style>
.greeting {
  color: #42b983;
}
</style>

