const Title: string = "Wings Project";

export function showMessage(): void {
  console.log(`Welcome ${Title}`);
}

export class Util {
  static getVersion(): string {
    return "1.0.0";
  }
}
