async function resolveSample() {
  return "Success！";
}

// then()が実行されコンソールに「Success!!」が表示される
resolveSample().then((value) => {
  console.log(value); // => Success!!
});

// Failure!!をthrowしているためこの値がrejectされる
async function rejectSample() {
  throw new Error("Failure!");
}

// rejectSampleがPromiseを返し、「Failure!」がrejectされるため
// catch()が実行されコンソールに「Failure!」が表示される
rejectSample().catch((err) => {
  console.log(err); // => Failure!!
});
