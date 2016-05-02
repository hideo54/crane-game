# crane-game

2016年灘校文化祭のNPCA(灘校パソコン研究部)ブースにて展示されたクレーンゲームです。

## バージョン

Ver 1.0

## 遊び方

1. まず、このリポジトリをcloneします。

### バックエンドの準備

1. ブレッドボードにワイヤーをつないでもいい状態にします。6Vのアルカリ電池と2つのモータードライバ(L293Dなど)を使用してください。
2. Raspberry Piとブレッドボードとを正しく配線してください。
3. どこに配線したかについてpins.jsonに記録してください。
4. 準備完了です! 正しいコマンドが実行された時、プログラムによってモーターが制御されます。

### Webサーバーの準備

1. `npm install`
2. `node server.js`

### 遊ぶ

http://[RPi-address]:3000 にアクセスしてお楽しみください。

## 環境

* Raspberry Pi
* Jessieベースの Raspbian OS (Wheezyベース以前のものとは違い、非sudoユーザーでもGPIOを制御できます)
* Python 2.6 以降 (Python 3.* でも同様に対応可能かもしれません)
* Node.js (あまり古いものは対応していません)

## ライセンス

Apache 2.0

## 連絡先

* E-mail: contact@hideo54.com
* Twitter: @hideo54
