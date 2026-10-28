---
name: fix-list-key
description: >-
  React のリスト key を、データの安定した ID に付け替える。
  key={index}、key={Math.random()}、並べ替えで入力が消える、という修正で使う。
---

## 説明

リストの `key` を描画ごとに変わらない ID へ替え、インデックスと乱数キーを外す手順。

## 本文

1. `key={Math.random()}` や、レンダーのたびに新しい値になる式を探す。データの ID に替える。
2. `key={index}` は、そのリストが挿入、削除、並べ替え、フィルタをしないときだけ残す。それ以外は項目の ID を使う。
3. 項目に ID が無く、同じ親の中で値が重複しないと分かっているときは、その値を `key` にする。重複するならデータに ID を足す。ID を足す変更が依頼範囲を超えるときは、範囲を確認する。
4. `key` は props として子に渡らない。子が ID を使うなら `<Row key={row.id} id={row.id} />` のように別に渡す。
5. リストの state や入力が、並び替えのあと正しい項目に残ることを、既存のテストか操作で確認する。

## 出典

- https://react.dev/learn/rendering-lists
- https://react.dev/learn/preserving-and-resetting-state
