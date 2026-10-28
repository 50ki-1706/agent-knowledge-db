---
name: enable-python-uv
description: >-
  devenv の Python モジュールで uv と仮想環境を有効にし、進入時に uv sync する。
  devenv.nix に uv が無く、pyproject.toml があるプロジェクトで使う。
---

## 説明

`languages.python` で、devenv が用意する Python を uv に使わせ、`uv sync` をシェル進入時に走らせる手順。

## 本文

1. `pyproject.toml` の位置を確認する。ルートに無ければ `languages.python.directory` でそのディレクトリを指す。
2. `poetry.install.enable` が有効なら、uv の sync と同時には有効にしない。Poetry をやめる変更は依頼範囲を確認する。
3. 次を `devenv.nix` の `languages.python` に設定する。

```nix
languages.python = {
  enable = true;
  venv.enable = true;
  uv = {
    enable = true;
    sync.enable = true;
  };
};
```

4. 特定の Python 版が必要なときだけ `languages.python.version` を `"3.11"` や `"3.11.3"` のように設定し、`devenv.yaml` に `nixpkgs-python` 入力を足す。版の指定が不要なら、この入力は足さない。devenv は設定された Python を uv に使わせ、uv 自身に別の Python を取得させない。
5. 依存グループをシェル進入時に入れる要件があるときは `uv.sync.allGroups` か `uv.sync.groups` を、文書の例に従って設定する。
6. タスクが同期後の環境を使うときは `after = [ "devenv:python:uv" ];` を付ける。`devenv tasks run` はシェル進入時の初期化を自動では実行しない。
7. 依存の追加自体は `uv add` で行い、`pyproject.toml` と `uv.lock` を更新する。ロックは手で編集しない。`devenv shell` で `uv` と `python` が見えることを確認する。

## 出典

- https://devenv.sh/languages/python/
- https://devenv.sh/tasks/
- https://docs.astral.sh/uv/guides/projects/
- https://docs.astral.sh/uv/concepts/projects/sync/
