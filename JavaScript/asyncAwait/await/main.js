async function sample() {
  const result = await sampleResolve();

  // sampleResolve()のPromiseの結果が返ってくるまで以下は実行されない
  console.log(result);
}
