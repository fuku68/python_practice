<script>
export default {
  data() {
    isLoading: false;
    profile: {
      name: "Yamada Hanako";
      age: 28;
    }
  },
  watch: {
    isLoading() {
      // ローディング状態が切り替わったときの処理
    },
    "profile.age": {
      handler: function() {
        // プロフィールの年齢が変更されたときの処理
      },
      immediate: true,
    },
  },
};
</script>
