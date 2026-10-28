## 説明

uv が管理する Python プロジェクトで、依存関係とロックファイルを崩さないための指示。

## 本文

依存関係の追加と削除は `uv add` と `uv remove` で行う。`uv add httpx` は `pyproject.toml` の `project.dependencies` に制約付きで追加し、ロックファイルと環境も更新する。開発用は `uv add --dev` で dependency group に入れる。`dev` グループは `uv sync` が既定で入れる。追加のグループは `--group`、extras は `--optional` を使う。

実行時の依存を `pip install` でプロジェクト環境へ直接入れない。`uv sync` はロックファイルに無いパッケージを既定で取り除く。

`uv.lock` は環境を再現するためのロックファイルであり、バージョン管理に含める。手で編集しない。ロックファイルが `pyproject.toml` と一致するかは `uv lock --check` で見る。CI や「ロックを勝手に変えない」実行では `uv run --locked` を使う。新しいリリースへ上げるのは、依頼があるときだけ `uv lock --upgrade` か `uv lock --upgrade-package <name>` で行う。制約の範囲を超えては上がらない。

`uv run` は実行前にロックと環境を合わせる。エディタ向けに環境だけ合わせるときは `uv sync` を使う。プロジェクトとワークスペースメンバーは、ビルドシステムがあるとき editable で入る。

`uv init` が作る `.venv` はローカル環境である。コミットしない。Python の版は `.python-version` と `requires-python` に従う。

## 出典

- https://docs.astral.sh/uv/guides/projects/
- https://docs.astral.sh/uv/concepts/projects/dependencies/
- https://docs.astral.sh/uv/concepts/projects/sync/
- https://docs.astral.sh/uv/concepts/projects/layout/
- https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
- https://github.com/astral-sh/uv
