## 説明

複数の Python パッケージを1つのリポジトリで育てるとき、uv workspace で依存とロックをまとめて扱うための指示。

## 本文

パッケージが2つ以上あり、互いに依存するときだけ workspace にする。1つだけのパッケージは、ふつうの uv プロジェクトのままでよい。

ルートの `pyproject.toml` に `[tool.uv.workspace]` を書く。`members` には `"packages/*"` のような glob を書く。`exclude` には含めないものを書く。glob に当たるディレクトリは、すべて `pyproject.toml` を持つ。ルート自身もメンバーである。

メンバー間の依存は `[tool.uv.sources]` に `{ workspace = true }` と書く。PyPI ではなく workspace の中から取ると宣言する。書かないと、同じ名前のパッケージを PyPI から取ろうとする。メンバー間の依存は editable で入る。

ロックファイルは workspace で1つだけである。`uv.lock` はルートに置き、バージョン管理に含める。手で編集しない。`uv lock` は workspace 全体を一度に解く。

`uv run` と `uv sync` は既定でルートを対象にする。特定のメンバーで実行するときは `--package <名前>` を付ける。`uv run --package api ...` のように書く。ルートの `tool.uv.sources` は全メンバーに効く。メンバー側で同じ依存の source を書くと、そちらが勝つ。

`requires-python` は workspace 全体で1つに揃える。メンバーごとに指定した版のうち、共通する版が使われる。版を分けたいメンバーがあるときは、workspace にしない。

依存が衝突するメンバーや、環境を分けたいメンバーは workspace に入れない。代わりに path 依存でつなぐ。その場合 `uv run --package` は使えない。実行は各パッケージの場所で行う。

Python には依存の隔離がない。あるメンバーが、他のメンバーの依存を import しても uv は止めない。使う依存は自分の `pyproject.toml` に書く。

## 出典

- https://docs.astral.sh/uv/concepts/projects/workspaces/
