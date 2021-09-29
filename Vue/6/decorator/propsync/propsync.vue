<template>
  <SunComponent :sunValue.sync="childValue" />
</template>

<script lang="ts">
import { Component, PropSync, Vue } from "vue-property-decorator";

@Component
export default class SampleComponent extends Vue {
  @PropSync("value", { type: String, default: "" })
  childValue: string;

  // value を変更したいときに呼び出す
  updateValue(newValue) {
    this.childValue = newValue;
  }
}
</script>
