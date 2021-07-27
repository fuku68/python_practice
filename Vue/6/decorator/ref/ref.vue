<template>
  <div>
    <ChildComponent ref="childComponent" />
    <button ref="submitButton">Submit</button>
  </div>
</template>

<script lang="ts">
import { Component, Ref, Vue } from "vue-property-decorator";
import ChildComponent from "@/component/ChildComponent.vue";

@Component({
  components: {
    ChildComponent,
  },
})
export default class SampleComponent extends Vue {
  @Ref() childComponent: ChildComponent;
  @Ref() submitButton: HTMLButtonElement;

  mounted() {
    // 子コンポーネントのメソッドを実行する
    this.childComponent.updateValue();

    // ボタンをフォーカスする
    this.submitButton.focus();
  }
}
</script>
