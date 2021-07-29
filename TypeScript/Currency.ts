type Unit = "EUR" | "GBP" | "JPY" | "USD";

export type Currency = {
  unit: Unit;
  value: number;
};

export let Currency = {
  from(value: number, unit: Unit): Currency {
    return {
      unit: unit,
      value,
    };
  },
};
