---
name: write-agent-skill
description: >-
  同じ指示を繰り返し貼り付ける作業を、Agent Skills の仕様に沿った SKILL.md にする。
  新しい skill を作るとき、既存の skill を移植性のある形に直すときに使う。
---

## 説明

繰り返し使う手順を、Agent Skills の open standard に沿った skill フォルダにまとめる手順。Claude Code だけでなく、仕様を読む他のエージェントでも同じフォルダが読める。

## 本文

1. skill にするかを決める。同じ指示、手順、チェックリストを何度もチャットへ貼っているなら skill にする。1回だけの事実や短い方針は `AGENTS.md` に残す。`AGENTS.md` の1節が手順に育ったら、そこから切り出す。
2. `<名前>/SKILL.md` のフォルダを作る。名前はフォルダ名と frontmatter の `name` で一致させる。64文字までで、小文字、数字、ハイフンだけを使い、先頭と末尾、連続するハイフンを避ける。
3. frontmatter に `name` と `description` を書く。`description` は1024文字までで、何をする skill か、どんなときに使うかを書く。エージェントは起動時にこの2つだけを読むので、使う場面が分かる言葉を入れる。
4. 本文は、手順、入出力の例、よくある失敗の順に書く。エージェントは skill を開いたときに全文を読むので、長い資料は `references/` へ分け、繰り返し実行する処理は `scripts/` へ置く。`SKILL.md` は500行以内に収める。
5. 必要なら任意の項目を足す。環境の条件は `compatibility`、ライセンスは `license`、実験的な `allowed-tools` は、使うツールを半角スペース区切りで書く。frontmatter には仕様の6項目だけを書く。
6. 置き場所を選ぶ。自分だけが使うなら `~/.claude/skills/<名前>/`、チームと共有するならプロジェクトの `.claude/skills/<名前>/` に置いてコミットする。
7. 仕様どおりか確かめる。`name` がフォルダ名と一致しているか、frontmatter に仕様外の項目が無いかを見直す。Claude Code では `/doctor` を実行し、使われていない skill や重い skill が無いか診断する。

## 出典

- https://agentskills.io/specification
- https://code.claude.com/docs/en/skills
