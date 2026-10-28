---
name: run-ruff
description: >-
  変更した Python を Ruff で検査し、修正可能な診断を直してからフォーマットする。
  ruff check、ruff format、lint、未使用 import を扱うときに使う。
---

## 説明

プロジェクトに入っている Ruff で、変更箇所を `ruff check` と `ruff format` に通す手順。

## 本文

1. `pyproject.toml` の `[tool.ruff]`、`ruff.toml`、`.ruff.toml`、または開発依存の `ruff` を探す。無ければ追加しない。依頼が Ruff の導入を含んでいるときだけ `uv add --dev ruff` を実行する。Black、isort、Flake8 を重ねて足さない。
2. 変更したパスに対して `uv run ruff check <path>` を実行する。設定は、そのファイルから見て最も近い設定ファイルに従う。
3. 今回の変更が原因の修正可能な診断は `uv run ruff check --fix <path>` で直す。関係の無いファイルへ `--fix` を広げない。
4. `uv run ruff format <path>` を実行する。
5. 残す診断には、その行へ `# noqa: CODE` と規則コードを書く。ファイル全体の `# ruff: noqa` や、設定の `ignore` へ規則を足して消さない。
6. `UP` が `typing.List` や `typing.Iterable` を指摘したら、`list` などの組み込み、または `collections.abc` へ直す。

## 出典

- https://docs.astral.sh/ruff/tutorial/
- https://docs.astral.sh/ruff/linter/
- https://docs.astral.sh/ruff/formatter/
- https://docs.astral.sh/ruff/configuration/
- https://docs.astral.sh/uv/guides/projects/
