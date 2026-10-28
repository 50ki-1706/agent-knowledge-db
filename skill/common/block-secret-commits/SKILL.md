---
name: block-secret-commits
description: >-
  コミットと push の前に秘密情報と履歴の強制上書きを止める。
  git commit、git push、.env、トークン、認証情報、pre-commit の失敗を扱うときに使う。
---

## 説明

ステージした差分から秘密を外し、hook の迂回と強制 push で検査を通さない手順。

## 本文

1. `git status` と `git diff`、`git diff --cached` を見る。API キー、秘密鍵、トークン、パスワード、`.env` の実値が含まれていたら、その行を追跡対象から外す。
2. 秘密ファイルが今後も混ざる経路なら、リポジトリの `.gitignore` にパターンを足す。すでにコミットされている秘密は、値を無効化したうえで履歴から取り除く必要があることを報告する。
3. pre-commit や GitHub の push protection が秘密で止めたとき、フラグで検査を飛ばさない。`git commit --no-verify` は pre-commit と commit-msg hook を迂回する。`git push --no-verify` は pre-push hook を迂回する。
4. 公開済みブランチへ `git push --force` しない。書き換えが明示されたときは `--force-with-lease` を使う。
5. 秘密を含む差分を、ログやチャットの引用で繰り返さない。

## 出典

- https://git-scm.com/docs/git-commit
- https://git-scm.com/docs/git-push
- https://git-scm.com/docs/gitignore
- https://docs.github.com/en/code-security/concepts/secret-security/command-line-push-protection
- https://docs.github.com/en/code-security/how-tos/secure-your-secrets/work-with-leak-prevention/push-protection-on-the-command-line
