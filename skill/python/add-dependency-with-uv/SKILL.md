---
name: add-dependency-with-uv
description: >-
  uv プロジェクトへ依存を追加または削除し、pyproject.toml と uv.lock を揃える。
  パッケージ追加、uv add、uv remove、ロックファイル更新のときに使う。
---

## 説明

`pip install` を使わず、`uv add` または `uv remove` で依存とロックファイルを同時に更新する手順。

## 本文

1. プロジェクトルートに `pyproject.toml` があることを確認する。uv プロジェクトでなければ、この手順で初期化しない。依頼がプロジェクト作成を含んでいるときだけ `uv init` を検討する。
2. 実行時の依存は `uv add <name>`。開発時だけなら `uv add --dev <name>`。既存の dependency group や extra に入れるときは `--group` か `--optional` を、その表が既にあるときに使う。バージョン下限を指定するときは `uv add 'httpx>=0.20'` のようにシェルのクォートを付ける。
3. 削除は `uv remove <name>`。追加したときと同じ `--dev`、`--group`、`--optional` を付ける。
4. `uv.lock` を手で編集しない。`pyproject.toml` とロックの両方を差分に含める。`.venv` はコミットしない。
5. 依頼がアップグレードでなければ `uv lock --upgrade` を実行しない。上げるときは `uv lock --upgrade-package <name>` に限る。
6. `uv lock --check` と、プロジェクトが既に使っているテストを `uv run` で実行する。devenv が `languages.python.uv.sync.enable` で同期している場合も、依存の変更自体は `uv add` でロックへ反映する。

## 出典

- https://docs.astral.sh/uv/concepts/projects/dependencies/
- https://docs.astral.sh/uv/concepts/projects/sync/
- https://docs.astral.sh/uv/guides/projects/
- https://devenv.sh/languages/python/
