## 説明

devenv のシェルを、信頼したプロジェクトだけで自動または手動で有効にするための指示。

## 本文

手動で入るときは、プロジェクトで `devenv shell` を実行する。プロセス付きの開発スタックは `devenv up` で起動する。

自動で入るときは、シェル設定に devenv の hook を1行足す。bash は `eval "$(devenv hook bash)"`、zsh は `eval "$(devenv hook zsh)"`。fish と nushell は、Nix 経由のインストールなら同梱の snippet が読み込む。読まないときは各シェルの文書にある `devenv hook` の行を足す。

hook は `devenv.nix` があるディレクトリをプロジェクトとみなす。2.2 より前は `devenv.yaml` を見ていた。未信頼のディレクトリは自動では有効にならない。内容を確認してから、そのプロジェクトで `devenv allow` を実行する。信頼を外すときは `devenv revoke`。プロファイル付きで許可した選択は、次の devenv コマンドにも効く。明示した `--profile` が優先される。

direnv で現在のシェルへ直接変数を載せたいときは、`.envrc` に次を書く。

```bash
eval "$(devenv direnvrc)"
use devenv
```

その後 `direnv allow` で、その `.envrc` を承認する。`devenv init` は `.envrc` を作らない。2.2 以降は `devenv init --include-envrc` で含められる。外部依存が無い方は `devenv hook`、サブシェルを避けてその場のシェルを変えたいときは direnv を使う。

未確認のリポジトリを、hook や direnv の警告を無視して許可しない。

## 出典

- https://devenv.sh/getting-started/
- https://devenv.sh/auto-activation/
- https://devenv.sh/integrations/direnv/
- https://devenv.sh/processes/
