## 説明

`strict` を維持し、`catch` 変数を `unknown` として絞り込むための指示。

## 本文

`strict` は strict 系の検査をまとめて有効にする。将来の TypeScript はこのフラグの下に検査を追加する。型エラーを消す目的で `strict` を `false` にしない。個別の strict 系フラグも、そのエラーを避けるためだけに切らない。

`useUnknownInCatchVariables` は strict に含まれる。有効なとき `catch` 変数の既定の型は `unknown` になる。JavaScript では `throw` できる値が `Error` に限られないため、`err.message` のようにプロパティを直接読まない。`instanceof Error` や別の型ガードで絞り込んでから使う。絞り込みの書き方は narrowing の案内に従う。

`catch (err: any)` や `as any` で検査を通さない。呼び出し側の契約が `any` を要求している箇所以外では、`unknown` のまま受けて絞り込む。

## 出典

- https://www.typescriptlang.org/tsconfig/strict.html
- https://www.typescriptlang.org/tsconfig/useUnknownInCatchVariables.html
- https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-4.html
- https://www.typescriptlang.org/docs/handbook/2/narrowing.html
