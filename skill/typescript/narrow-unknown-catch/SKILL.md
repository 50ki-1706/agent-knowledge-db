---
name: narrow-unknown-catch
description: >-
  catch の unknown を型ガードで絞り込んでからプロパティを読む。
  TypeScript の strict で「err は unknown」や Property 'message' does not exist が出たときに使う。
---

## 説明

`strict` に含まれる `useUnknownInCatchVariables` のもとで、`catch` 変数を `unknown` のまま扱ってから絞り込む手順。

## 本文

1. `tsconfig` の `strict` を `false` にしない。`useUnknownInCatchVariables` も、このエラーを消すためだけに切らない。このフラグは strict に含まれる。
2. `catch (err)` の `err` は `unknown` である。`err.message` を直接読まない。JavaScript では `throw` できる値が `Error` に限られない。
3. 使う前に絞り込む。

```ts
try {
  await run();
} catch (err) {
  if (err instanceof Error) {
    console.error(err.message);
    return;
  }
  console.error(err);
}
```

4. `catch (err: any)` や `as any` で検査を通さない。呼び出し規約が別の型を要求するときは、その型への絞り込みを書く。
5. プロジェクトの型検査コマンドを実行し、同じ `unknown` エラーが残っていないことを確認する。

## 出典

- https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-4.html
- https://www.typescriptlang.org/tsconfig/useUnknownInCatchVariables.html
- https://www.typescriptlang.org/tsconfig/strict.html
- https://www.typescriptlang.org/docs/handbook/2/narrowing.html
