---
name: add-workspace-member
description: >-
  uv workspace へパッケージを追加し、メンバー間の依存を workspace から取るようにする。
  モノレポへ新しいパッケージを増やすときに使う。
---

## 説明

uv workspace へ新しいパッケージを追加し、他のメンバーから workspace の依存として使えるようにする手順。

## 本文

1. workspace のルートを確認する。`[tool.uv.workspace]` を持つ `pyproject.toml` のある場所がルートである。無ければ、この手順で workspace を作らない。依頼が workspace 化を含んでいるときだけ、ルートの `[tool.uv.workspace]` と `members` を作る。
2. メンバーを作る。ルートの中で `uv init packages/<名前>` を実行する。workspace の中では、作ったパッケージが自動でメンバーに入る。ライブラリにするときは `uv init --lib packages/<名前>` を使う。
3. 依存を足す。あるメンバーが別のメンバーを使うときは、使う側で `uv add --package <使う側> <使われる側>` を実行する。`pyproject.toml` に依存が追加される。`[tool.uv.sources]` には `{ workspace = true }` が書かれる。手で書くときは、依存と source の両方を書く。
4. `uv sync` をルートで実行する。workspace 全体が1つの `.venv` に入る。`uv.lock` を手で編集しない。
5. 実行と確認は `--package` を使う。`uv run --package <名前> <コマンド>` を使うと、そのメンバーの環境で実行できる。テストは各メンバーで実行し、通ることを見る。
6. 依存が衝突する、環境を分けたい、といった理由があるメンバーは追加しない。workspace に向かないときは、path 依存でつなぐ方法を提案する。

## 出典

- https://docs.astral.sh/uv/concepts/projects/workspaces/
