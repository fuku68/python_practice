<script lang="ts">
import { Component, Watch, Vue } from "vue-property-decorator";

@Component
export default class SampleComponent extends Vue {
  isLoading = false;
  profile = {
    name: "Yamada Hanako",
    age: 28,
  };

  @Watch("isLoading")
  onChangeLoadingStatus() {
    // ローディング状態が切り替わったときの処理
  }

  @Watch("profile.age", { immediate: true })
  onChangeProfileAge() {
    // プロフィールの年齢が変更されたときの処理
  }
}
</script>
