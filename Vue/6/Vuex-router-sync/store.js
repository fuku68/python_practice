// 商品のリストをステートとして保持するモジュール
export default {
  state: {
    products: [
      { id: 1, name: "Apple" }, // 商品リスト
      { id: 2, name: "Orange" },
      { id: 3, name: "Banana" },
    ],
  },
  getters: {
    //　ゲッターの第三引数にはルートのステートが渡される
    currentProduct(state, getters, rootState) {
      const productId = Number(rootState.route.params.id);
      return state.products.find((product) => {
        return product.id === productId;
      });
    },
  },
};
