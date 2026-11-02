## 説明

Next.js のコードを書くとき、インストール済みの版の文書を正とし、動いている dev サーバーで検証するための指示。

## 本文

書く前に、編集するアプリに入っている Next.js のバージョンを見る。モノレポでは、リポジトリのルートではなく、そのアプリのディレクトリから `next` を解決する。

16.2 以降は、`node_modules/next/dist/docs/` の該当ガイドを読んでから書く。同梱文書の API と手順に従い、非推奨の注意も読む。16.2 は文書を同梱するが、指示ブロックは自動では作らない。16.3 以降は、管理された指示が既定で有効である。`next dev` はコーディングエージェントを検知すると、そのブロックを作り、更新する。

16.1 以前には同梱文書が無い。`npx @next/codemod@canary agents-md` を実行し、`.next-docs/` に取得した版の文書を読む。

`<!-- BEGIN:nextjs-agent-rules -->` から `<!-- END:nextjs-agent-rules -->` までは、`next dev` が管理する。中身は削除も書き換えもしない。差分から消しても、次の `next dev` が戻す。ブロックは手を加えずにコミットする。プロジェクト独自の指示は、マーカーの外に書く。生成と更新を止めるには、`next.config` の `agentRules` を `false` にする。このオプションは 16.3 で追加された。16.4 以降では、次の `next dev` が既存のブロックを取り除き、ファイルの中身がそれだけならファイルごと消す。

`next dev` は `.next/dev/lock` に PID、ポート、URL を書く。同じプロジェクトの dev サーバーが既に動いていれば、2つ目を起動しない。表示された既存の URL を使う。

編集の途中でコンパイルを確認するために `next build` を使わない。動いている dev サーバーの `/_next/mcp` にある `get_compilation_issues` と `compile_route` を使う。自前のクライアントから使うときは、`.mcp.json` に `next-devtools-mcp` を足す。

Cache Components のエラーが `[stream]`、`[cache]`、`[block]` の選択肢を出したら、リンク先の `/docs/messages/...` を読んでから選ぶ。各ページには、直し方、他の選択肢との得失、見落としやすい制約がある。修正は失敗しているコードに絞る。範囲を広げるときは、先にユーザーへ確認する。プリレンダーの失敗を調べるときは `next build --debug-prerender` を使う。本番ビルドはサーバーコードを縮小し、1つのルートが失敗すると止まる。このフラグはソースマップを有効にし、他のルートの確認を続ける。

公式ドキュメントは、URL の末尾に `.md` を付けると Markdown で取れる。`Accept: text/markdown` でも Markdown が返る。`/docs/messages` のエラーページは同梱されないので、ネットワーク経由で読む。索引は `/docs/llms.txt`、全ページを1つにまとめたものは `/docs/llms-full.txt` にある。

## 出典

- https://nextjs.org/docs/app/guides/ai-agents
- https://nextjs.org/blog/next-16-3-ai-improvements
- https://nextjs.org/docs/app/api-reference/config/next-config-js/agentRules
