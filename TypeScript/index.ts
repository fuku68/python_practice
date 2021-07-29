console.log("hello TypeScript!");

import { Currency } from "./Currency";

let amountDue: Currency = {
  // Currencyを型として利用
  unit: "JPY",
  value: 83733.18,
};

// Currencyを値として使う
let otherAmountDue = Currency.from(330, "EUR");
