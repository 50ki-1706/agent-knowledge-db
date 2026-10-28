## 説明

devenv の `devenv.nix` に、パッケージ、言語、スクリプト、プロセスを宣言するための指示。

## 本文

`devenv init` は `devenv.nix`、`devenv.yaml`、`.gitignore` を作る。ツールとランタイムは `devenv.nix` に書く。入力のピンは `devenv.lock` にある。ロックは `devenv update` で更新し、手で編集しない。パッケージ名は `devenv search <name>` で、そのロックが指す Nixpkgs から探す。

単体の実行ファイルやライブラリは `packages` に足す。

```nix
{ pkgs, ... }:
{
  packages = [ pkgs.git pkgs.jq ];
}
```

言語のツールチェーンは language モジュールを有効にする。TypeScript のツールは `languages.typescript.enable`。Node.js は `languages.javascript.enable` で、既定のパッケージは `pkgs.nodejs-slim`、Node 本体は既定で有効、npm / pnpm / Yarn は既定では入らない。使うマネージャだけ `languages.javascript.pnpm.enable` のように有効にする。Corepack 経由のラッパーは `languages.javascript.corepack.enable`。

Python は `languages.python.enable`。特定の版が必要なときだけ `languages.python.version` を指定し、そのときは `devenv.yaml` に `nixpkgs-python` 入力を足す。uv を devenv から使うときは `venv.enable`、`uv.enable`、`uv.sync.enable` を有効にする。`pyproject.toml` はプロジェクトディレクトリ、または `languages.python.directory` の先にあること。`poetry.install` と `uv.sync` は同時に有効にしない。uv の同期を有効にしたタスクは `after = [ "devenv:python:uv" ];` に依存する。仮想環境だけを使うタスクは `devenv:python:virtualenv` に依存する。`devenv tasks run` はシェル進入時の初期化を自動では実行しない。

一度きりのコマンドは `scripts.<name>.exec` に書く。そのスクリプトだけで必要なパッケージは `scripts.<name>.packages` に置き、シェル全体の `packages` を増やさない。常駐プロセスは `processes.<name>.exec` に書き、`devenv up` で起動する。停止は `devenv down`（2.2 以降の短縮形。それ以前の文書にある長い形は `devenv processes down`）。依存は `after = [ "devenv:processes:<name>" ];` のように書く。

## 出典

- https://devenv.sh/getting-started/
- https://devenv.sh/packages/
- https://devenv.sh/languages/
- https://devenv.sh/languages/javascript/
- https://devenv.sh/languages/typescript/
- https://devenv.sh/languages/python/
- https://devenv.sh/scripts/
- https://devenv.sh/processes/
- https://devenv.sh/tasks/
- https://github.com/cachix/devenv
