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
    //　現在のページに紐づく商品を返したい
    currentProduct(state) {
      return state.products.find((product) => {
        //　表示するべき商品のIDはストア内にないため、
        // 対象の商品を探すことができない
        // return product.id === ???
      });
    },
  },
};
