/*
const promise = new Promise((resolve) => {
  setTimeout(() => {
    // resolveを呼び出すとPromiseの処理が完了
    resolve();
  }, 3000);
});

// then()メソッドで続く処理を記述できる
promise.then(() => {
  console.log("次の処理");
});
*/

const promise = new Promise((resolve) => {
  setTimeout(() => {
    // resolveを呼び出すとPromiseの処理が完了
    resolve("orange");
  }, 3000);
});

// then()メソッドで続く処理を記述できる
promise.then((value) => {
  console.log(value);
});
