---
name: add-server-action
description: >-
  Next.js App Router に、認証付きの Server Action を追加する。
  フォーム送信、データ更新、use server、revalidate、updateTag を扱うときに使う。
---

## 説明

`'use server'` の関数を、クライアントの外に定義し、関数の中で認可してからキャッシュを無効化する手順。

## 本文

1. `next.config` の `cacheComponents` を確認する。無効なら `'use cache'` や `updateTag` を導入せず、そのプロジェクトが既に使っている無効化（Cache Components 以前の文書）に合わせる。
2. Server Function は専用ファイルの先頭の `'use server'`、または Server Component 内の非同期関数本体の `'use server'` で定義する。Client Component の中では定義できない。クライアントからはその関数を import し、`<form action>` か `formAction`、または `startTransition` 経由で呼ぶ。
3. 関数の中で認証と認可を行う。ボタンを隠すだけでは境界にならない。Server Function は UI を経由しない POST でも届く。`FormData` の値は検証し、所有権はセッションから引き直す。
4. 更新のあと、キャッシュの無効化を `redirect` より前に行う。`cacheComponents` が有効で、ユーザー自身の書き込みをすぐ見せるときは `updateTag`。遅れが許される一覧は `revalidateTag(tag, 'max')`。タグが無い経路だけ `revalidatePath`。`updateTag` は Server Action の中だけで使う。
5. クライアントから複数の Server Action を `Promise.all` で並列にしない。並列の処理は 1 つの関数の中で行う。
6. 変更した経路の型検査と、プロジェクトの既存テストを実行する。

## 出典

- https://nextjs.org/docs/app/getting-started/mutating-data
- https://nextjs.org/docs/app/guides/server-actions
- https://nextjs.org/docs/app/getting-started/revalidating
- https://nextjs.org/docs/app/guides/data-security
- https://nextjs.org/docs/app/api-reference/directives/use-server
- https://nextjs.org/docs/app/api-reference/functions/updateTag
