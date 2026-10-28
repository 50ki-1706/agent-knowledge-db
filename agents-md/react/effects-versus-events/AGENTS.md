## 説明

React の Effect を、画面に出たことによる同期に限り、ユーザー操作と派生値は別の場所に書くための指示。

## 本文

Effect は、コンポーネントが画面に表示されたことによって外部と同期する処理に使う。特定の操作が原因の処理は、そのイベントハンドラに書く。ボタンを押したので POST する、といった処理はハンドラ側である。表示されたので検索結果を取り直す、といった処理は Effect 側である。

props や state から計算できる値は、描画中に計算する。その値を state に入れ、Effect で更新しない。

ある識別子が変わったときに状態を初期化したいときは、その識別子を `key` に渡す。React は同じ位置の同じコンポーネントの state を保つ。`key` が変わると、そのコンポーネントと子の state は作り直される。Effect で入力欄を空にしない。

複数のハンドラで同じ処理が要るときは、関数に切り出して各ハンドラから呼ぶ。Effect に集約して、どの操作だったかを後から推測しない。

フックは React の関数コンポーネントかカスタムフックのトップレベルで呼ぶ。条件、ループ、ネストした関数の中では呼ばない。

## 出典

- https://react.dev/learn/you-might-not-need-an-effect
- https://react.dev/learn/preserving-and-resetting-state
- https://react.dev/reference/rules/rules-of-hooks
