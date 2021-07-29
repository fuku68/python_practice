/*
// a. ジェネリック対応のクラス
class MyGenerics<T = string> {
  // T型の value プロパティ
  value!: T;
  // T型の値を返す　getValue メソッド
  getValue(): T {
    return this.value;
  }
}

// b. MyGenericsクラスにstring型を割り当て
let g = new MyGenerics();
// c. valueプロパティに文字列型の値を代入
g.value = "Hoge";
console.log(g.getValue()); // 結果：Hoge
*/

// a. ジェネリック対応のクラス
class MyGenerics<T = string> {
  // T型の value プロパティ
  value!: T;
  // T型の値を返す　getValue メソッド
  getValue(): T {
    return this.value;
  }
}

let g = new MyGenerics();

g.value = "Hoge";
console.log(g.getValue()); // 結果：Hoge

/*
class MyGeneric<T,R> { ... }

// この場合、インスタンス化に際しても以下のように複数の型を指定する
let h = new MyGeneric<string,number>();
*/
