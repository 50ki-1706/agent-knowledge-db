---
name: prune-agents-md
description: >-
  AGENTS.md と CLAUDE.md を新しく作るとき、肥大化したものを整理するとき、
  指示が守られない原因を調べるときに使う。
  コードを読めば分かる行を外し、確認できる指示だけを残す。
---

## 説明

指示ファイルを短くし、コードを読めば分かることを書かず、毎回守らせたい規則は別の仕組みへ移す手順。

## 本文

各行に「コードを読めば分かるか」と問う。分かるなら書かない。Claude Code の `/doctor` は、コードから分かるディレクトリ構成、依存の一覧、アーキテクチャの概要を削る提案をする。落とし穴、理由、ツールの既定と違う規約は残す。

残すものは次のとおり。

- このリポジトリのテスト、型検査、lint の正確なコマンドと、1ファイルだけテストする方法
- 誤解を招くコード。広く残っている古いパターンを新しいコードが真似してはいけない箇所や、使われていないように見えて生きているディレクトリ
- リポジトリに書かれていない決定。どのやり方に決めたか、デプロイの手順、何にレビューが要るか
- すでに2回訂正した内容

書くときは、確認できる文にする。インデントは「2スペースでインデントする」、テストは「コミット前に `npm test` を実行する」のように、コマンドと結果が分かる形で書く。`IMPORTANT` を足しても、無視される行は直らない。無視されるときは、ファイルが長いか、例外を許さない規則である。

振り分ける。

1. 複数の手順からなる作業や、特定の作業でだけ要る知識は skill へ移す。skill も、コードを読めば分かることは書かない。
2. 一部のディレクトリにだけ効く規則は、そのディレクトリの `AGENTS.md` へ移す。近いファイルが優先される。Claude Code では、パスを絞った `.claude/rules/` か、そのディレクトリの `CLAUDE.md` に置く。
3. 例外を許さない規則は、hook、deny ルール、CI へ移す。指示ファイルに残しても、毎回は守られない。

短くする。Claude Code では 1 ファイル 200 行未満を目安にする。長いと従い方が落ちる。Codex は、ルートから作業ディレクトリまで連結したサイズが `project_doc_max_bytes`（既定 32 KiB）に達すると、それ以降のファイルを足さない。上限に当たったら、近いディレクトリへ分ける。階層のあいだで矛盾する指示は消す。Claude Code はどちらに従うか決まらない。Codex は近いファイルが後から連結されて優先される。同じ規則を矛盾したまま残さない。矛盾や、存在しないファイルを指す指示は、Claude Code の `/doctor prompt-audit` で洗う。

Claude Code と Codex を併用するとき、作業ディレクトリかその上位に `CLAUDE.md`、`.claude/CLAUDE.md`、`CLAUDE.local.md` があると、Claude Code は既定では `AGENTS.md` を読まない。`~/.claude/CLAUDE.md` はこの条件に入らない。`AGENTS.md` を両方の正本にするときは、隣の `CLAUDE.md` に、囲みのない1行として次を書く。

@AGENTS.md

`CLAUDE.md` の中でこの行をバッククォートやコードブロックに入れると、import にならない。Claude 固有の指示は、その行の後に書く。両方を直接読ませる設定は、Project instructions の `claude-md-and-agents-md` である。

確認する。Claude Code のセッションで `/context` を実行し、Memory files に載っているか見る。`AGENTS.md` を直接読んだかは `/memory` でパスを確認する。

## 出典

- https://code.claude.com/docs/en/best-practices
- https://code.claude.com/docs/en/claude-md
- https://developers.openai.com/codex/guides/agents-md
- https://agents.md/
