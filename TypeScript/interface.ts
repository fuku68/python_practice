// オブジェクトのみのタイプエイリアス（型の変数）
interface Human {
  name: any;
  age: any;
  greeting: any;
}

const human: Human = {
  name: "Quill",
  age: 38,
  greeting(message: string) {
    console.log(message);
  },
};

// 高齢者情報の配列
const seniorHumans = [
  {
    name: "Bill",
    age: 98,
    greeting(message: string) {
      console.log(message);
    },
    hasGrandChild: true,
    grandChildFirstNames: ["Eimy", "Ken"],
  },
  {
    name: "Michael",
    age: 100,
    greeting(message: string) {
      console.log(message);
    },
    hasGrandChild: true,
    grandChildFirstNames: ["Lisa", "Jessy", "David", "Wess"],
  },
  {
    name: "Tom",
    age: 77,
    greeting(message: string) {
      console.log(message);
    },
    hasGrandChild: false,
  },
];
