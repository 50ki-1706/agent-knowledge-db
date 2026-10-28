## 説明

Cache Components の有無を見て、読み取りのキャッシュと Server Function の更新を書くための指示。

## 本文

最初に `next.config.ts` を見る。`cacheComponents` が有効なときと無効なときで、従う文書が違う。

`cacheComponents: true` のとき:

- 新しいアプリの推奨設定では Cache Components と Partial Prefetching が有効である。`cacheComponents` を既存アプリで有効にするときは `partialPrefetching` も明示する。未設定は警告になる。移行中だけ `false` にし、警告消しのために黙って削除しない。
- リクエスト間で再利用してよい非同期処理には、関数本体の先頭で `'use cache'` を書く。同じファイルの先頭に書くと、そのファイルの export すべてがキャッシュされる。`cacheLife` を一緒に呼び、暗黙の `default` プロファイルに頼らない。更新でまとめて無効化するものには `cacheTag` を付ける。引数と閉じ込めた値はキャッシュキーに入る。
- `cookies()`、`headers()`、`searchParams`、動的な `params` はリクエスト時の情報である。これらを読むコンポーネントは `<Suspense>` で包む。毎リクエスト新しいデータが必要な取得にも `'use cache'` を付けず、`<Suspense>` で流す。実行時データに寿命を付けて prefetch に含めたいときだけ `'use cache: private'` を検討する。
- 更新後にユーザー自身の書き込みをすぐ見せるときは Server Action から `updateTag` を呼ぶ。少し遅れてもよい一覧は `revalidateTag(tag, 'max')` のようにプロファイル付きで呼ぶ。第2引数は stale-while-revalidate の窓である。タグが分からない経路だけ `revalidatePath` を使う。`redirect` より前に無効化する。
- `updateTag` と `revalidatePath` はアクションの応答に現在のルートの再描画を含める。プロファイル付きの `revalidateTag` はバックグラウンド更新で、同じ応答には再描画を含めない。

`cacheComponents` が無いプロジェクトでは `'use cache'`、`cacheLife`、`cacheTag`、`updateTag` を導入しない。fetch の cache オプションと route segment config は、Cache Components 以前の文書に従う。

データ更新は Server Function で行う。`'use server'` を非同期関数の本体、または専用ファイルの先頭に置く。Client Component の中では定義できない。クライアントからは、そのファイルを import して `<form action>` か `startTransition` 経由で呼ぶ。

Server Function は UI を経由しない POST でも届く。関数の内部で認証と認可を行い、`FormData` は検証する。描画時にボタンを隠すだけでは境界にならない。クライアントから複数の Server Action を `Promise.all` で並列にしない。Next.js はクライアントごとにアクションを順に送る。並列にしたい処理は、1 つの Server Function の中で行う。

## 出典

- https://nextjs.org/docs/app/getting-started/caching
- https://nextjs.org/docs/app/getting-started/revalidating
- https://nextjs.org/docs/app/getting-started/mutating-data
- https://nextjs.org/docs/app/guides/server-actions
- https://nextjs.org/docs/app/guides/caching-without-cache-components
- https://nextjs.org/docs/app/guides/data-security
- https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents
- https://nextjs.org/docs/app/api-reference/config/next-config-js/partialPrefetching
- https://nextjs.org/docs/app/api-reference/directives/use-cache
- https://nextjs.org/docs/app/api-reference/directives/use-cache-private
- https://nextjs.org/docs/app/api-reference/functions/cacheLife
- https://nextjs.org/docs/app/api-reference/functions/cacheTag
- https://nextjs.org/docs/app/api-reference/functions/updateTag
