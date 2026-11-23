## 説明

Claude Code の hook で、文章の指示では守られにくい約束を機械的に強制するための指示。

## 本文

約束を守らせる方法は、文章の指示より hook を優先する。指示は読まれないこともあり、読まれても破られることがある。hook は決まった出来事の前後で必ず走る。

止めたい操作は `PreToolUse` で止める。hook は JSON を標準入力から読み、結果を JSON と終了コードで返す。`hookSpecificOutput` に `permissionDecision: "deny"` を入れるか、終了コード 2 で止める。理由は `permissionDecisionReason` に書く。終了コード 0 以外で 2 でない値は失敗扱いになり、止める保証がない。

止める対象は matcher で絞る。ツール名で絞るには `"Bash"` や `"Edit|Write"` を書く。引数まで絞るときは `if` に `"Bash(git *)"` や `"Edit(*.ts)"` のような条件を書く。`if` の判定は最善努力であり、抜け道がある。確実な禁止は permission の設定で行い、hook だけに頼らない。

終わった操作への後処理は `PostToolUse` で行う。`Write` や `Edit` の後に整形と lint を走らせる。後処理は操作を取り消せないので、止める目的では使わない。

共有する hook は `.claude/settings.json` に書く。リポジトリへ含め、 clone した人にも同じ hook が効く。個人だけの hook は `~/.claude/settings.json` か `.claude/settings.local.json` に書く。

hook は速く、確実に終わるものにする。重い処理は走らせない。入力の JSON は `jq` で読み、無い項目を前提にしない。hook が失敗すると操作の成否にも影響する。

hook の登録は `/hooks` で確認する。壊れた hook や一致しない matcher は `/status` に出る。

## 出典

- https://code.claude.com/docs/en/hooks
- https://github.com/anthropics/claude-code/releases/tag/v2.1.327
