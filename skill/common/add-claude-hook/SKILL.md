---
name: add-claude-hook
description: >-
  Claude Code に hook を追加し、決まった出来事の前後でスクリプトを走らせる。
  危険な操作を止めるときに使う。
---

## 説明

Claude Code の hook を追加し、決まった出来事の前後でコマンドを自動で走らせる手順。

## 本文

1. 何をいつ行うか決める。操作を止めたいときは `PreToolUse` を選ぶ。終わった操作へ後処理をしたいときは `PostToolUse` を選ぶ。会話の始まりには `SessionStart` を選ぶ。止める目的で `PostToolUse` を選ばない。
2. matcher を決める。ツール名で絞るには `"Bash"` や `"Edit|Write"` を書く。引数まで絞るときは `if` に `"Bash(git *)"` のような条件を付ける。広すぎる matcher は、関係ない操作でも hook を走らせる。
3. スクリプトを書く。`.claude/hooks/<名前>.sh` に置き、実行権限を付ける。標準入力の JSON から必要な項目を `jq` で読む。`rm -rf` を含む Bash を止める例では、コマンドを取り出す。含んでいれば `permissionDecision: "deny"` と理由を JSON で出し、終了コード 0 で終える。含まなければ何も出さず、終了コード 0 で終える。終了コード 2 でも止められるが、理由は標準エラーへ書く。
4. 設定ファイルへ登録する。共有するなら `.claude/settings.json`、個人だけなら `.claude/settings.local.json` に書く。`hooks` の下に出来事、matcher、実行する hook の順で書く。
5. 登録を確認する。`/hooks` で一覧を見て、出来事と matcher が意図どおりか見る。`/status` に壊れた hook が出ていないか見る。
6. 動作を確かめる。止める hook は、対象の操作を実際に試して止まるか見る。後処理の hook は、操作の後で処理が走るか見る。失敗した hook は、設定の見直しとスクリプトの単体実行で原因を切り分ける。

## 出典

- https://code.claude.com/docs/en/hooks
- https://github.com/anthropics/claude-code/releases/tag/v2.1.327
