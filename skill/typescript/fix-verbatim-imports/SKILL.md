---
name: fix-verbatim-imports
description: >-
  verbatimModuleSyntax のエラーを、import と export の type 修飾子で直す。
  型だけの import が値として残る、または type を付けた名前を値として使っているときに使う。
---

## 説明

`verbatimModuleSyntax` が有効なとき、型だけの名前に `type` を付け、値として残す名前からは `type` を外す手順。

## 本文

1. `verbatimModuleSyntax` を切ってエラーを消さない。`importsNotUsedAsValues` と `preserveValueImports` を新たに有効にしない。これらはこのフラグに置き換える形で非推奨である。
2. 規則は次のとおり。`type` が無い import / export は出力に残る。`type` が付いたものは出力から消える。
3. 型としてだけ使う名前を直す。

```ts
import type { User } from "./user";
import { createUser, type UserRole } from "./user";
export type { UserRole };
```

4. 実行時に必要な名前に `type` が付いていたら外す。クラスや関数は値である。
5. `import` を `require` に書き換えようとして失敗しているファイルは、CommonJS が必要なら `import x = require("x")` と `export =` に変える。このフラグは ECMAScript の `import` を `require` へ書き換えない。
6. プロジェクトの型検査を実行する。

## 出典

- https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-0.html
- https://www.typescriptlang.org/tsconfig/verbatimModuleSyntax.html
