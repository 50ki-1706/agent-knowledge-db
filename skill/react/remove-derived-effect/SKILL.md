---
name: remove-derived-effect
description: >-
  props や state から計算している useEffect を、描画中の計算か key による状態リセットに置き換える。
  不要な Effect、派生 state、id が変わったら入力を空にする、という修正で使う。
---

## 説明

表示されたこと以外を原因とする `useEffect` を外し、派生値は描画で計算し、識別子の変化は `key` で state を分ける手順。

## 本文

1. Effect の中で行っていることを、原因で分ける。ユーザーの操作が原因ならイベントハンドラへ移す。props や state から計算できる値なら、描画中の式にする。コンポーネントが表示されたので外部と同期する処理だけ Effect に残す。
2. `useEffect` で `setState` し、その state が別の state や props の写しになっているときは、state と Effect を削除して描画中に計算する。
3. 親から渡された id が変わるたびに Effect で入力を空にしているときは、Effect を削除し、その id を子の `key` に渡す。`key` が変わると React はその子の state を作り直す。
4. 複数のボタンから同じ処理を呼ぶときは、関数に切り出して各ハンドラから呼ぶ。Effect に集めて、どの操作だったかを後から判定しない。
5. フックの呼び出しはコンポーネントのトップレベルに残す。条件の中へ移さない。
6. プロジェクトの既存のテストと型検査を実行する。

## 出典

- https://react.dev/learn/you-might-not-need-an-effect
- https://react.dev/learn/preserving-and-resetting-state
- https://react.dev/reference/rules/rules-of-hooks
