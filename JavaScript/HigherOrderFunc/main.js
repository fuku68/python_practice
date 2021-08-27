var data = [5, 6, 7, 8];

// forEach
data.forEach(function (value, index, array) {
  console.log(value * value);
});

// map
var resultMap = data.map(function (value, index, array) {
  return value * value;
});
console.log("map result:", resultMap);

// filter
var resultFiltered = data.filter(function (value, index, array) {
  return value === 5;
});
console.log("filter result:", resultFiltered);

//　reduce
var resultReduced = data.reduce(function (a, b) {
  return a + b;
});
console.log("reduce result:", resultReduced);

// map 演習
var cars = [
  { type: "軽自動車", price: "安い" },
  { type: "高級車", price: "高い" },
];

var prices = cars.map(function (car) {
  return car.price;
});

console.log(prices);
