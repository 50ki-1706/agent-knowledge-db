## 説明

コミットと push で、秘密情報の混入、hook の迂回、公開済み履歴の強制上書きを避けるための指示。

## 本文

秘密情報はコミットしない。API キー、秘密鍵、トークン、パスワード、`.env` に入った実値は、追跡対象に入れず、プロジェクトの ignore 規則に載せる。GitHub の push protection は、対応している秘密を含む push を止める。止まった内容はコミットから取り除く。すでに露出した実値は、無効化したうえで履歴から外す。

`git commit --no-verify` は pre-commit hook と commit-msg hook を迂回する。hook や push protection が秘密や検査で止めたとき、このフラグで通さない。hook を外す指示がチャットに明示されているときだけ使う。

`git push --force` は、リモート ref がローカルの祖先でないときに git が行う更新拒否を無効にする。公開済みの履歴を、依頼なしにこのフラグで上書きしない。履歴の書き換えが明示されたときは `--force-with-lease` を使い、期待するリモートの値と一致するときだけ更新する。

仮想環境、依存関係のキャッシュ、ビルド成果物は、リポジトリの `.gitignore` に従って扱う。ignore されていないことだけを理由に、秘密や生成物を追加しない。

## 出典

- https://git-scm.com/docs/git-commit
- https://git-scm.com/docs/git-push
- https://git-scm.com/docs/gitignore
- https://git-scm.com/docs/githooks
- https://docs.github.com/en/code-security/concepts/secret-security/command-line-push-protection
- https://docs.github.com/en/code-security/how-tos/secure-your-secrets/work-with-leak-prevention/push-protection-on-the-command-line
- https://docs.github.com/en/get-started/git-basics/ignoring-files
