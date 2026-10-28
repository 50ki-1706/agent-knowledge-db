# agent-knowledge-db

TypeScript / Next.js を中心に、uv と devenv も使う開発で、AI エージェントへ渡す知識を置く場所です。中身はプロジェクトの規約そのものではなく、必要なものだけを自分のリポジトリへコピーするための原文です。

## 目的

エージェントは、近くにある `AGENTS.md` と、`SKILL.md` の `name` / `description` から手順を拾います。このリポジトリは、その原文を用途別に分けておきます。

- `agents-md/` は、プロジェクトへ置く指示文です。最寄りのファイルが優先され、チャットの指示はそれより優先されます。
- `skill/` は、特定の作業に入ったときだけ読む手順です。`name` は、`SKILL.md` があるディレクトリ名と一致させます。

各ファイルは次の3節だけを持ちます。

1. 説明
2. 本文
3. 出典

出典は、公式ドキュメントか、内容の根拠になった公開記事の URL です。

## ディレクトリ構成

トップレベルは `agents-md/` と `skill/` です。その下を `common/` と、言語・フレームワーク・ツールのディレクトリに分け、さらに用途ごとのディレクトリにファイルを1つ置きます。

```text
agents-md/
  common/   typescript/   nextjs/   react/   python/   nix/
    <用途>/AGENTS.md
skill/
  common/   typescript/   nextjs/   react/   python/   nix/
    <用途>/SKILL.md
```

`common/` は特定のスタックに寄らない作業です。`python/` は uv と Ruff、`nix/` は devenv を扱います。

## 索引

### agents-md

- [agents-md/common/follow-project-checks/AGENTS.md](agents-md/common/follow-project-checks/AGENTS.md) — 完了前に、リポジトリが既に定義している確認コマンドを実行する
- [agents-md/common/git-safety/AGENTS.md](agents-md/common/git-safety/AGENTS.md) — 秘密の混入、hook の迂回、公開履歴の強制上書きを避ける
- [agents-md/nextjs/cache-and-mutations/AGENTS.md](agents-md/nextjs/cache-and-mutations/AGENTS.md) — Cache Components の有無に合わせて、読み取りキャッシュと更新を書く
- [agents-md/nextjs/server-client-boundary/AGENTS.md](agents-md/nextjs/server-client-boundary/AGENTS.md) — Server Component と Client Component の境界を保つ
- [agents-md/nix/activate-shell/AGENTS.md](agents-md/nix/activate-shell/AGENTS.md) — 信頼したプロジェクトだけで devenv のシェルを有効にする
- [agents-md/nix/declare-environment/AGENTS.md](agents-md/nix/declare-environment/AGENTS.md) — パッケージ、言語、スクリプト、プロセスを `devenv.nix` に宣言する
- [agents-md/python/ruff/AGENTS.md](agents-md/python/ruff/AGENTS.md) — Ruff をリンター兼フォーマッタとして使う
- [agents-md/python/uv-project/AGENTS.md](agents-md/python/uv-project/AGENTS.md) — uv の依存関係とロックファイルを崩さない
- [agents-md/react/effects-versus-events/AGENTS.md](agents-md/react/effects-versus-events/AGENTS.md) — Effect は表示による同期に限り、操作と派生値は別の場所に書く
- [agents-md/react/list-keys/AGENTS.md](agents-md/react/list-keys/AGENTS.md) — リストの `key` にデータの安定した ID を使う
- [agents-md/typescript/strict-catch/AGENTS.md](agents-md/typescript/strict-catch/AGENTS.md) — `strict` を維持し、`catch` を `unknown` として絞り込む
- [agents-md/typescript/verbatim-module-syntax/AGENTS.md](agents-md/typescript/verbatim-module-syntax/AGENTS.md) — 型だけの import / export に `type` 修飾子を付ける

### skill

- [skill/common/block-secret-commits/SKILL.md](skill/common/block-secret-commits/SKILL.md) — コミット前に秘密と強制 push を止める
- [skill/common/explain-before-shorten/SKILL.md](skill/common/explain-before-shorten/SKILL.md) — 日本語の説明を、口頭で伝わる文章にしてから意味を保って短くする
- [skill/common/read-nearest-agents/SKILL.md](skill/common/read-nearest-agents/SKILL.md) — 最も近い `AGENTS.md` を読んでから変更する
- [skill/nextjs/add-server-action/SKILL.md](skill/nextjs/add-server-action/SKILL.md) — 認証付きの Server Action を追加する
- [skill/nextjs/cache-a-read/SKILL.md](skill/nextjs/cache-a-read/SKILL.md) — 読み取りを Cache Components の有無に合わせてキャッシュする
- [skill/nix/enable-python-uv/SKILL.md](skill/nix/enable-python-uv/SKILL.md) — devenv で uv と仮想環境を有効にする
- [skill/nix/enable-typescript/SKILL.md](skill/nix/enable-typescript/SKILL.md) — devenv で Node.js と TypeScript を有効にする
- [skill/python/add-dependency-with-uv/SKILL.md](skill/python/add-dependency-with-uv/SKILL.md) — `uv add` / `uv remove` で依存とロックを更新する
- [skill/python/run-ruff/SKILL.md](skill/python/run-ruff/SKILL.md) — 変更箇所を Ruff で検査して整形する
- [skill/react/fix-list-key/SKILL.md](skill/react/fix-list-key/SKILL.md) — リストの `key` を安定した ID に付け替える
- [skill/react/remove-derived-effect/SKILL.md](skill/react/remove-derived-effect/SKILL.md) — 派生値の Effect を描画中の計算か `key` に置き換える
- [skill/typescript/fix-verbatim-imports/SKILL.md](skill/typescript/fix-verbatim-imports/SKILL.md) — `verbatimModuleSyntax` の import を `type` 修飾子で直す
- [skill/typescript/narrow-unknown-catch/SKILL.md](skill/typescript/narrow-unknown-catch/SKILL.md) — `catch` の `unknown` を絞り込んでからプロパティを読む

## 使い方

`AGENTS.md` は、適用させたいディレクトリへコピーします。リポジトリ全体ならルート、パッケージだけならそのパッケージのルートです。エージェントは編集するファイルに最も近い `AGENTS.md` を読みます。すでにファイルがあるときは、節を足して統合し、ファイルごと置き換えないでください。

`SKILL.md` は、そのファイルがあるディレクトリごとコピーします。ディレクトリ名は frontmatter の `name` と一致させます。Cursor は次の場所を再帰的に見ます。

- `.agents/skills/<name>/SKILL.md`
- `.cursor/skills/<name>/SKILL.md`

このリポジトリの `common/` や `nextjs/` は分類用です。コピー先では、`SKILL.md` の親ディレクトリが `name` と一致していれば、その上に分類ディレクトリがあっても読み込まれます。例: `.cursor/skills/nextjs/add-server-action/SKILL.md`。

個人のどのプロジェクトでも使う技能は、`~/.agents/skills/` または `~/.cursor/skills/` に置きます。環境によってクラウドへ同期される場所が違うので、プロジェクトに含めるか、次の文書で確認してください。

- https://agents.md/
- https://agentskills.io/specification
- https://cursor.com/docs/skills

## 追加方法

1. `agents-md/` か `skill/` を選ぶ。
2. `common/` か、既存のスタックディレクトリを選ぶ。新しいスタックが必要なら、小文字のディレクトリを足す（例: `go/`）。
3. 用途をケバブケースのディレクトリにする。skill では、この名前が frontmatter の `name` になる。
4. 下のテンプレートで `AGENTS.md` または `SKILL.md` を作る。節は「説明」「本文」「出典」の3つだけにする。
5. 出典には、自分で開いた公式ドキュメントか公開記事の URL を書く。ページが存在しない URL は書かない。
6. この README の索引に、パスへのリンクを1行足す。
7. 索引と実ファイルが一致することを確認する。

```bash
python3 - << 'PY'
import pathlib, re, sys
root = pathlib.Path(".")
files = sorted(
    list(root.glob("agents-md/**/AGENTS.md")) + list(root.glob("skill/**/SKILL.md"))
)
readme = (root / "README.md").read_text()
linked = set(re.findall(r"\(((?:agents-md|skill)/[^)\s]+\.md)\)", readme))
actual = {str(p) for p in files}
missing = actual - linked
extra = linked - actual
errors = []
if missing or extra:
    errors.append(f"index mismatch missing={sorted(missing)} extra={sorted(extra)}")
for path in files:
    text = path.read_text()
    body = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S)
    headings = re.findall(r"^## .+$", body, flags=re.M)
    if headings != ["## 説明", "## 本文", "## 出典"]:
        errors.append(f"{path}: headings {headings}")
    if path.name == "SKILL.md":
        name = path.parent.name
        if not re.search(rf"(?m)^name:\s*{re.escape(name)}\s*$", text):
            errors.append(f"{path}: name must match {name}")
        if "description:" not in text.split("---", 2)[1]:
            errors.append(f"{path}: missing description")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"ok {len(files)} files")
PY
```

## ファイルテンプレート

`AGENTS.md`:

```markdown
## 説明

この知識が何のためのものかを短く書く。

## 本文

エージェントが従う判断と手順を書く。

## 出典

- https://example.com/official-page
```

`SKILL.md`:

```markdown
---
name: purpose-directory-name
description: >-
  何をする手順かと、どの作業のときに使うかを書く。
  name は SKILL.md の親ディレクトリ名と一致させる。
---

## 説明

この手順の目的を短く書く。

## 本文

1. 最初に確認すること。
2. 変更する場所と、変更しない場所。
3. 終わったことの確認。

## 出典

- https://example.com/official-page
```
