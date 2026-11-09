---
name: start-worktree-session
description: >-
  並行して編集するセッションを git worktree で隔離して始める。
  別のセッションと同時に同じリポジトリを編集するときに使う。
---

## 説明

編集するセッションを git worktree の中に作り、他のセッションと書き込みが衝突しないように始める手順。

## 本文

1. 並行して編集するセッションがあるか確認する。1つだけなら worktree を作らず、そのまま始める。
2. `claude --worktree <名前>` でセッションを始める。worktree は `<リポジトリ>/.claude/worktrees/<名前>/` に作られ、ブランチは `worktree-<名前>` になる。名前を省くと Claude Code が付ける。
3. `.claude/worktrees/` が `.gitignore` に無ければ足す。worktree の中身がメインのチェックアウトで未追跡ファイルとして見えないようにする。
4. worktree の中で依存関係を導入するなど、開発環境を初期設定する。`.env` のような ignore 対象ファイルを運ぶには、プロジェクトのルートに `.worktreeinclude` を置く。
5. 既存のブランチで worktree を作るときは、`git worktree add <パス> <ブランチ>` で作ってから、その中で `claude` を起動する。
6. worktree の中からメインのチェックアウトを編集しない。編集や git の向き先を変えるコマンドは Claude Code が止めるが、シェルの書き込みは止められない。
7. 終わったら worktree を残さない。終了時の確認で残すと選んだときは、`claude --worktree <名前> --resume` で戻る。手で消すときは `git worktree remove` を使う。

## 出典

- https://code.claude.com/docs/en/worktrees
- https://git-scm.com/docs/git-worktree
