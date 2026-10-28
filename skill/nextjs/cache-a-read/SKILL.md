---
name: cache-a-read
description: >-
  Next.js の読み取りを、Cache Components の有無に合わせてキャッシュする。
  use cache、cacheLife、cacheTag、Suspense、cookies、searchParams を扱うときに使う。
---

## 説明

`cacheComponents` が有効なアプリにだけ `'use cache'` を足し、リクエスト時のデータは Suspense に置く手順。

## 本文

1. `next.config` を開く。`cacheComponents` が無い、または `false` なら、この手順で `'use cache'` を足さない。Cache Components 以前のキャッシュ文書に従い、既存の `fetch` cache と route segment config を崩さない。
2. `cacheComponents: true` で `partialPrefetching` が未設定なら、警告を消すためだけに削除しない。移行中でなければ明示的に有効にする。
3. データが `cookies()`、`headers()`、`searchParams`、リクエストごとの動的 `params` に依存するなら、`'use cache'` を付けない。読み取りをコンポーネントに分け、`<Suspense>` で包み、Promise は `await` する。実行時データに寿命を付けて prefetch へ含める要件があるときだけ `'use cache: private'` を検討する。
4. リクエスト間で再利用してよい取得は、非同期関数の本体先頭に `'use cache'` を書き、`cacheLife('hours')` のようにプロファイルを明示する。ファイル先頭に書くと、そのファイルの export 全部がキャッシュされる。更新で無効化するものには `cacheTag` を付ける。
5. 引数と閉じ込めた値はキャッシュキーになる。ユーザー固有の値を公開キャッシュの関数へ閉じ込めない。
6. 開発サーバーまたはプロジェクトの既存の型検査で、blocking prerender の指摘が残っていないことを確認する。

```tsx
import { cacheLife, cacheTag } from "next/cache";

export async function getProducts() {
  "use cache";
  cacheLife("hours");
  cacheTag("products");
  return db.query("SELECT * FROM products");
}
```

## 出典

- https://nextjs.org/docs/app/getting-started/caching
- https://nextjs.org/docs/app/getting-started/revalidating
- https://nextjs.org/docs/app/guides/caching-without-cache-components
- https://nextjs.org/docs/app/api-reference/directives/use-cache
- https://nextjs.org/docs/app/api-reference/directives/use-cache-private
- https://nextjs.org/docs/app/api-reference/functions/cacheLife
- https://nextjs.org/docs/app/api-reference/functions/cacheTag
- https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents
