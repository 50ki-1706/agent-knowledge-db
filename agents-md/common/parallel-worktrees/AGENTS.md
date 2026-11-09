## 説明

同じリポジトリで複数のセッションやサブエージェントが並行して編集するとき、書き込みの衝突を避けるための指示。

## 本文

同じチェックアウトで2つのセッションが編集すると、互いの未コミット作業を上書きする。編集するセッションには、それぞれ別の worktree を割り当てる。

`claude --worktree <名前>`（短縮形 `-w`）で、`<リポジトリ>/.claude/worktrees/<名前>/` に worktree を作り、ブランチ `worktree-<名前>` でセッションを始める。名前を省くと Claude Code が付ける。

worktree は新しいチェックアウトなので、依存関係の導入など開発環境の初期設定は worktree の中で行う。`.env` のような ignore 対象ファイルを新しい worktree へ自動で運ぶには、プロジェクトのルートに `.worktreeinclude` を置く。

`.claude/worktrees/` は `.gitignore` に載せ、worktree の中身がメインのチェックアウトで未追跡ファイルとして見えないようにする。

worktree の中からメインのチェックアウトを編集しない。Claude Code は worktree 内のセッションからメインのチェックアウトへの編集やコマンドを止めるが、シェルの書き込み（`cp` やリダイレクト）は止められないため、自分でも行わない。

作業が終わったら worktree を残さない。終了時の確認に従い、残す場合は `claude --worktree <名前> --resume` で戻る。手で消すときは `git worktree remove` を使い、未コミットの変更がある worktree には `--force` が要る。

サブエージェントにも worktree を割り当てるときは、カスタムサブエージェントの frontmatter に `isolation: worktree` を書く。

1つのセッションだけが静かなリポジトリを編集するときは、worktree は要らない。

## 出典

- https://code.claude.com/docs/en/worktrees
- https://git-scm.com/docs/git-worktree
