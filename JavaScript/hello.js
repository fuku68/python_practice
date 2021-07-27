/*
console.log("hello");

window.onload = function () {
  // ボタンクリック時に実行されるイベントハンドラーを登録
  document.getElementById("btn").onclick = function () {
    window.alert("ボタンがクリックされました");
  };
};

// elem.addEventListener(type,listener,capture)
//   elem: 要素オブジェクト type: イベントの種類
//   listener: イベントに応じて実行すべき処理
//   capture: イベントの方向
*/

/*
// ページロード時に実行されるイベントリスナーを登録
document.addEventListener(
  "DOMContentLoaded",
  function () {
    var btn = document.getElementById("btn");
    btn.addEventListener(
      "click",
      function () {
        var name = document.getElementById("name");
        console.log(name.value);
      },
      false
    );
  },
  false
);
*/

// var url = link.href; // 取得
// link.href = "http://www.google.com";

// elem.getAttribute(name)
// elem.setAttribute(name,value)

// var url = link.getAttribute("href");
// link.setAttribute("href", "http://www.example.com");

// document.addEventListener(
//   "DOMContentLoaded",
//   function () {
//     var btn = document.getElementById("btn");
//     btn.addEventListener(
//       "click",
//       function () {
//         var result = document.getElementById("result");
//         var xhr = new XMLHttpRequest();
//         xhr.onreadystatechange = function () {
//           if (xhr.readyState === 4) {
//             if (xhr.status === 200) {
//               result.textContent = xhr.responseText;
//               console.log(xhr.responseText);
//             } else {
//               result.textContent = "サーバーエラーが発生しました";
//             }
//           } else {
//             result.textContent = "通信中...";
//           }
//         };
//         xhr.open("GET", "hello_ajax.php?name=" + encodeURIComponent(document.getElementById("name").value), true);
//         xhr.send(null);
//       },
//       false
//     );
//   },
//   false
// );
/*
function asyncProcess(value) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      // 引数valueが未定義であるかどうかによって成否を判定
      if (value) {
        resolve(`入力値：${value}`);
      } else {
        reject("入力はからです");
      }
    }, 500);
  });
}

asyncProcess("タンジロウ").then(
  // 成功したときに実行される処理
  (responce) => {
    console.log(responce);
  },
  //  失敗したときに実行される処理
  (error) => {
    console.log(`エラー：${error}`);
  }
); //結果　入力値：タンジロウ
*/

// document.addEventListener(
//   "DOMContentLoaded",
//   function () {
//     // タイマーを設置
//     var timer = window.setTimeout(function () {
//       // 現在の時刻を<div id="result">要素に表示（5000ミリ秒ごとに更新）
//       var dat = new Date();
//       document.getElementById("result").textContent = dat.toLocaleTimeString();
//     }, 5000);

//     // ボタンクリック時にタイマー処理を中止
//     document.getElementById("btn").addEventListener(
//       "click",
//       function () {
//         window.clearTimeout(timer);
//       },
//       false
//     );
//   },
//   false
// );
/*
document.addEventListener(
  "DOMContentLoaded",
  function () {
    var btn = document.getElementById("btn");
    btn.addEventListener(
      "click",
      function () {
        var result = [];
        var foods = document.getElementsByName("food");

        // チェックボックスを走査し、チェック状態にあるかを確認
        for (var i = 0; i < foods.length; i++) {
          var food = foods.item(i);

          // チェックされている項目の値を配列に追加
          if (food.checked) {
            result.push(food.value);
          }
        }
        // 配列の内容をダイアログに出力
        window.alert(result.toString());
      },
      false
    );
  },
  false
);
*/
// document.addEventListener(
//   "DOMContentLoaded",
//   function () {
//     var books = [
//       { title: "走れメロス", price: 800 },
//       { title: "羅生門", price: 850 },
//       { title: "人間失格", price: 900 },
//     ];
//     var list = document.getElementById("list");

//     // コンテンツを貯めるためのDocumentFragmentオブジェクトを生成
//     var frag = document.createDocumentFragment();

//     // 配列booksの内容を順番に<li>要素に整形
//     for (var i = 0; i < books.length; i++) {
//       var book = books[i];
//       var li = document.createElement("li");
//       var text = document.createTextNode(`${book.title}：${book.price}円`);
//       li.appendChild(text);
//       frag.appendChild(li);
//     }
//     // <li>要素をまとめて文書ツリーに追加
//     list.appendChild(frag);
//   },
//   false
// );

document.addEventListener(
  "DOMContentLoaded",
  function () {
    var elem = document.getElementById("elem");

    elem.addEventListener(
      "click",
      function () {
        this.classList.toggle("highlight");
      },
      false
    );
  },
  false
);
