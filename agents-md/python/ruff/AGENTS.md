## 説明

Ruff をリンター兼フォーマッタとして使っている Python プロジェクトでの指示。

## 本文

プロジェクトに Ruff があるとき、検査は `uv run ruff check`、自動修正は `uv run ruff check --fix`、整形は `uv run ruff format` で行う。対象パスを渡せる。設定は、そのファイルから親へ辿って最初に見つかる `pyproject.toml`、`ruff.toml`、`.ruff.toml` に従う。`pyproject.toml` では `[tool.ruff]` を使う。

既定のルールには `F`、`E`、`B`、`UP`、`RUF` などが含まれる。フォーマッタと重なるスタイル規則は既定では外れている。`UP` が有効なとき、`typing.Iterable` のような非推奨の import は `collections.abc` へ直す。言語自体の新しい書き方として、`list[str]` のような組み込みジェネリクスと、`X | Y` のユニオンを使える。

Ruff は Flake8、isort、Black の代替になる速度で作られている。Ruff が入っているプロジェクトへ Black、isort、Flake8 を重ねて追加しない。Ruff がまだ無いプロジェクトへは、依頼があるときだけ `uv add --dev ruff` で入れる。

行単位で外すときは `# noqa: CODE` のように規則を指定する。ファイル全体の `# ruff: noqa` や、規則を黙って `ignore` に足すことでエラーを消さない。新しい規則を既存コードへ広げるときは、依頼の範囲に限る。

## 出典

- https://docs.astral.sh/ruff/
- https://docs.astral.sh/ruff/tutorial/
- https://docs.astral.sh/ruff/linter/
- https://docs.astral.sh/ruff/formatter/
- https://docs.astral.sh/ruff/configuration/
- https://peps.python.org/pep-0585/
- https://peps.python.org/pep-0604/
- https://docs.python.org/3/library/typing.html
- https://github.com/astral-sh/ruff
