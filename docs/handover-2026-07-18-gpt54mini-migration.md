# GPT-5.4 mini独立版 移行申し送り（2026-07-18）

## 目的

運用中の `AichiroFunakoshi/Bridge-TTS-Codex-` を変更せず、内容コピーから別アプリ・別リポジトリを作り、翻訳モデルを `gpt-5.4-mini-2026-03-17` へ移行する。

## ローカルとGit

- 作業フォルダ: `/Users/inaminetetsuo/Documents/BrigeTTS(5.4-mini)`
- main基準コミット: 元リポジトリmain（`3f290fd`）の内容を独立Gitへコピー
- 作業ブランチ: `codex/gpt-5-4-mini`
- 新規GitHub予定: `AichiroFunakoshi/BrigeTTS-5.4-mini`
- 元リポジトリへremoteやpush先を設定しないこと

## 変更した固定値

| 項目 | 独立版 |
|---|---|
| モデル | `gpt-5.4-mini-2026-03-17` |
| Bundle ID | `com.a16.bridgetts.gpt54mini` |
| AltStore Source ID | `com.a16.bridgetts.gpt54mini.source` |
| Xcode Product | `BridgeTTS54Mini` |
| IPA | `BridgeTTS-5.4-mini-unsigned.ipa` |
| Actions Artifact | `BridgeTTS-5.4-mini-unsigned-ipa` |
| 予定版数 | `2.9.4` |

## モデル設定

Chat CompletionsとSSEストリーミングを維持し、`reasoning_effort: none`、`temperature: 0`、`verbosity: low`、`stream_options.include_usage: true` を使用する。Responses API、音声認識、TTS方式は変更しない。

## 残作業

1. ローカル構文、dry-run、Playwright、配布識別情報テストを完走する。
2. `OPENAI_API_KEY` が利用可能なら通常評価と石畳評価を実APIで実行する。
3. GitHub CLIを再認証し、新規リポジトリを作成してmain基準コミットと作業ブランチをpushする。
4. PRを作成し、CIとCodeRabbitレビューを待つ。ユーザーの「確認して」指示まではマージしない。
5. リリース指示後にのみタグをpushし、生成IPAのInfo.plistを実検査する。
