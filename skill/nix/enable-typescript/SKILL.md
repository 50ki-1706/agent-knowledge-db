---
name: enable-typescript
description: >-
  devenv.nix で Node.js と TypeScript のツールチェーンを有効にする。
  devenv に node、npm、pnpm、yarn、tsc が無いときに使う。
---

## 説明

`languages.javascript` と `languages.typescript` を、リポジトリが既に使っているパッケージマネージャに合わせて有効にする手順。

## 本文

1. `devenv.nix` を読む。すでに `languages.javascript` や `languages.typescript` があるときは、不足しているフラグだけを足す。
2. Node.js を PATH に出すため `languages.javascript.enable = true;` を設定する。既定のパッケージは `pkgs.nodejs-slim` で、Node 本体は既定で有効になる。別の Node が必要なら `languages.javascript.package` を、`devenv search` で見つけた属性に替える。
3. TypeScript のツールが必要なら `languages.typescript.enable = true;` を設定する。言語サーバーは既定で有効である。
4. リポジトリのロックファイルに合わせてマネージャを1つ有効にする。`pnpm-lock.yaml` なら `languages.javascript.pnpm.enable`、`package-lock.json` なら `languages.javascript.npm.enable`、`yarn.lock` なら `languages.javascript.yarn.enable`。Corepack のラッパーを使う既存設定があるときだけ `languages.javascript.corepack.enable = true;` にする。`*.install.enable` は、シェル進入のたびにインストールする運用が既にあるときだけ有効にする。
5. CLI が language モジュールに無いときは `devenv search` で名前を確認し、`packages` に足す。
6. `devenv shell` で `node` と、有効にしたマネージャのバージョンを確認する。`devenv.lock` は手で編集しない。入力を動かしたときだけ `devenv update` を使う。

## 出典

- https://devenv.sh/languages/javascript/
- https://devenv.sh/languages/typescript/
- https://devenv.sh/packages/
- https://devenv.sh/getting-started/
