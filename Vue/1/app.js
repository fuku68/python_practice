var items = [
  { name: "万年筆", price: 300, quantity: 0 },
  { name: "ノート", price: 400, quantity: 0 },
  { name: "消しゴム", price: 500, quantity: 0 },
];

var iroha = ["い", "ろ", "は"];

var vm = new Vue({
  el: "#app",
  data: {
    items: items,
    arr: iroha,
  },
  filters: {
    numberWithDelimiter: function (value) {
      if (!value) {
        return "0";
      }
      return value.toString().replace(/(\d)(?=(\d{3})+$)/g, "$1,");
    },
  },
  computed: {
    totalPrice: function () {
      // this経由でインスタンス内のデータにアクセス
      return this.items.reduce(function (sum, item) {
        return sum + item.price * item.quantity;
      }, 0);
    },
    totalPriceWithTax: function () {
      // 算出プロパティに依存した算出プロパティも定義できる
      return Math.floor(this.totalPrice * 1.08);
    },
    canBuy: function () {
      return this.totalPrice >= 1000; // 1000円以上から購入可能にする
    },
    errorMessageStyle: function () {
      return {
        border: this.canBuy ? "" : "1px solid red",
        color: this.canBuy ? "" : "red",
      };
    },
  },
  methods: {
    // メソッド名：function() {
      // 処理
    // }
  }
});

window.vm = vm;

console.log(vm.totalPrice);

// var vm = new Vue({
//   el: "#button",
//   data: {
//     loggedInButton: "ログイン済みのため購入できます",
//   },
// });
