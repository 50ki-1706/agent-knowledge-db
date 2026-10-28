## 説明

`verbatimModuleSyntax` が有効なプロジェクトで、型だけの import / export に `type` 修飾子を付けるための指示。

## 本文

このフラグの規則は単純である。`type` 修飾子の無い import と export は出力に残る。`type` 修飾子の付いたものは出力から完全に消える。見たままが出力になる。

型としてだけ使う名前は `import type`、または `import { type Foo }` のように inline の `type` で書く。実行時に値が必要な名前には `type` を付けない。型と値が混ざる named import は、型の名前だけに `type` を付ける。

```ts
import type { User } from "./user";
import { createUser, type UserRole } from "./user";
```

フラグを切ってエラーを消さない。`--importsNotUsedAsValues` と `--preserveValueImports` は、このフラグに置き換える形で非推奨になっている。新しくこれらを有効にしない。

このフラグの下では、ECMAScript の `import` / `export` は `require` へ書き換えられない。設定や拡張子が別のモジュール方式を示しているとエラーになる。CommonJS の `require` と `module.exports` を出す必要があるファイルでは、TypeScript の `import x = require(...)` と `export =` を使う。

## 出典

- https://www.typescriptlang.org/tsconfig/verbatimModuleSyntax.html
- https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-0.html
