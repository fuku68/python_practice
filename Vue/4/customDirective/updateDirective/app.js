Vue.directive("fallback-image", {
  bind: function (el, binding) {
    console.log(binding);
    el.addEventListener("error", function () {
      // 画像のロードに失敗したら実行される処理
      el.src = "https://dummyimage.com/400x400/000/ffffff.png&text=no+img";
    });
  },
  update: function (el, binding) {
    console.log("update", binding);
    el.style.border = "2px solid red";
  },
});

var vm = new Vue({
  el: "#app",
  data: function () {
    return {
      altText: "logo",
    };
  },
});
