## 説明

App Router で Server Component と Client Component の境界を保つための指示。

## 本文

`layout` と `page` は既定で Server Component である。データ取得、秘密情報を使った処理、ブラウザへ送る JavaScript を増やしたくない UI はサーバーに置く。

Client Component は、状態、イベントハンドラ、`useEffect`、`localStorage` や `window` などのブラウザ API、カスタムフックが必要な箇所に限る。ファイルの先頭、import より前に `'use client'` を書く。この指令があるモジュールが import するものはクライアント束縛に入る。インタラクティブな葉にだけ指令を付け、レイアウト全体には付けない。

Server Component から Client Component へ渡す props は、React がシリアライズできる値にする。関数やクラスインスタンスを渡さない。サーバーで描画した UI をクライアントの中に挟むときは、Client Component の `children` など props として Server Component を渡す。Client Component のファイルから Server Component を import しない。

`params` と `searchParams` は Promise である。`const { id } = await params`、`const { q } = await searchParams` のように待つ。

React context は Server Component では使えない。Provider は `'use client'` のコンポーネントにし、`children` を受ける。サーバーで取得した秘密をクライアントへ漏らさないモジュールには `server-only` を import する。クライアントへ出す環境変数は `NEXT_PUBLIC_` 接頭辞の付いたものだけである。

第三者のコンポーネントがクライアント専用機能を使い、パッケージ側に `'use client'` が無いときは、自分の Client Component で包んでから Server Component で使う。

## 出典

- https://nextjs.org/docs/app/getting-started/server-and-client-components
- https://nextjs.org/docs/app/getting-started/caching
- https://react.dev/reference/rsc/use-client
- https://react.dev/reference/rsc/use-server
