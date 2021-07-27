<template>
  <form @submit="submit">
    <input v-model="value" />
    <button type="submit">Submit</button>
  </form>
</template>

<script lang="ts">
import { Component, Emit, Vue } from "vue-property-decorator";

@Component
export default class ChildComponent extends Vue {
  value = "";

  // 値を送信する処理
  // イベント名を指定しない場合でも () は省略できない
  @Emit()
  submit() {
    return this.value;
  }
}
</script>

// 親コンポーネント <ChildComponent @submit-form="onSubmit" @submitForm="onSubmit" // 発火しない />
