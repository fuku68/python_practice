<script>
export default {
  data() {
    return {
      score: 55,
    };
  },
  computed: {
    triple() {
      return this.score * 3;
    },
  },
};
</script>

//
<script lang="ts">
// import { Component, Vue } from 'vue-property-decorator';

// @Component
// export default class SampleComponent extends Vue {
//   score = 55;

//   get triple() {
//     return this.score * 3;
//   }
// }
//
</script>
