//
<script>
// export default {
//   mounted() {
//     // コンポーネントがマウントされたときの処理
//   },
//   beforeDestroy() {
//     // コンポーネントが破棄される直前の処理
//   },
// };
//
</script>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component
export default class SampleComponent extends Vue {
  mounted() {
    // コンポーネントがマウントされたときの処理
  }

  beforeDestroy() {
    // コンポーネントが破棄される直前の処理
  }
}
</script>
