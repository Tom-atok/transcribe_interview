# transcribe_interview README

## 1. 概要

このプロジェクトは、OpenAI の Whisper モデルを用いて音声ファイルの文字起こしを行うシンプルな Python プログラムです。  
初心者でも手順に沿って環境構築や実行ができるように、以下の手順に従ってセットアップしてください。  
（Whisper の詳しい使い方は [gihyo.jp](https://gihyo.jp/article/2024/12/monthly-python-2412) や [aiacademy.jp](https://aiacademy.jp/media/?p=3512) を参考にしています。）

---

## 2. ファイル構成

プロジェクトのディレクトリ構成は以下の通りです。  
各フォルダの役割についても記載していますので、そのままコピー＆ペーストして利用してください。

```
transcribe_interview/
├── code/
│   └── transcribe.py      # 文字起こしのメインコード
├── data/
│   ├── input/             # ここに処理したい音声ファイル（例: .m4a ファイル）を配置します
│   └── output/            # 文字起こしの結果が出力されます（必要に応じてコードを拡張できます）
└── README.md              # このマニュアル
```

このような構成は、ファイル管理がしやすくなるため、初心者にもおすすめです ([jp.minitool.com](https://jp.minitool.com/lib/m4a.html)).

---

## 3. 環境構築

### 3.1. Python のダウンロード

- Python の公式サイト ([Python.org](https://www.python.org/downloads/)) から、最新の Python をダウンロードしてインストールしてください。

### 3.2. ffmpeg のインストール

- ffmpeg は、音声ファイルの読み込みや変換に必要なツールです。  
  **macOS** の場合は [Homebrew](https://brew.sh/) を使って以下のコマンドでインストールできます：
  ```bash
  brew install ffmpeg
  ```
- **Windows** や **Linux** の場合は、[ffmpeg の公式サイト](https://ffmpeg.org/download.html) からバイナリをダウンロードし、環境変数にパスを追加してください ([jp.cyberlink.com](https://jp.cyberlink.com/blog/media-converter/1931/best-audio-editing-tool-to-convert-m4a-to-mp3)).

### 3.3. Whisper のインストール

- Whisper は Homebrew 経由ではなく、Python の pip コマンドでインストールします。  
  以下のコマンドを使用してインストールしてください：
  ```bash
  pip install git+https://github.com/openai/whisper.git
  ```
  詳細は [aiacademy.jp](https://aiacademy.jp/media/?p=3512) や [qiita.com](https://qiita.com/daifuku10/items/c170a1361c232914f230) を参照してください。

### 3.4. 仮想環境の作成とパッケージのインストール

- プロジェクトルートディレクトリで仮想環境を作成し、必要なパッケージをインストールします。
  ```bash
  python -m venv .venv
  source .venv/bin/activate  # Windows の場合は .venv\Scripts\activate
  pip install -r requirements.txt
  ```
  ※ requirements.txt には Whisper やその他必要なパッケージのリストを記載してください ([Python公式サイト](https://www.python.org)).

---

## 4. コードの使い方

### 4.1. 音声ファイルの準備

- **data/input** フォルダに、文字起こししたい音声ファイル（例：.m4a ファイル）を配置します。

### 4.2. コードの実行方法

- プロジェクトルートディレクトリ（`transcribe_interview`）に移動し、以下のコマンドを実行してください：
  ```bash
  python code/transcribe.py --file_path {ファイルのpath}
  ```
  例：
  ```bash
  python code/transcribe.py --file_path your_audio_file.m4a
  ```
- このコマンドにより、指定した音声ファイルが読み込まれ、Whisper による文字起こしが実行され、結果がコンソールに出力されます ([aiacademy.jp](https://aiacademy.jp/media/?p=3512)).

---

## 5. 注意事項

- **ファイル名に空白があると問題が発生する場合があります**  
  もしファイル名に空白が含まれていると、コマンドライン上で正しく解釈されないことがあります。ファイル名は空白を避けるか、必要に応じてエスケープ（例：`Your\ File.m4a`）してください ([stackoverflow.com](https://stackoverflow.com/questions/41923492/cant-import-moviepy-due-to-missing-ffmpex-exe)).

- **環境変数とパス**  
  ffmpeg や Python の仮想環境が正しく設定されているかどうか、実行前に必ず確認してください ([jp.easeus.com](https://jp.easeus.com/audio-editing/how-to-convert-m4a-to-mp3-on-windows.html)).

---

## 6. 参考情報

- Whisper モデルの使い方についての詳細は、[gihyo.jp](https://gihyo.jp/article/2024/12/monthly-python-2412) を参照してください。  
- Python での音声処理全般や環境構築については、[aiacademy.jp](https://aiacademy.jp/media/?p=3512) および [qiita.com](https://qiita.com/daifuku10/items/c170a1361c232914f230) が参考になります。  
- ffmpeg の使い方やトラブルシューティングについては、[jp.cyberlink.com](https://jp.cyberlink.com/blog/media-converter/1931/best-audio-editing-tool-to-convert-m4a-to-mp3) や [jp.easeus.com](https://jp.easeus.com/audio-editing/how-to-convert-m4a-to-mp3-on-windows.html) をご覧ください。  
- 仮想環境の作成方法は、Python の公式ドキュメント ([Python公式サイト](https://www.python.org)) を参照してください。

---

この README を参考に、必要な手順を順に実行するだけで、誰でも簡単に音声ファイルの文字起こしができる環境が整います。コピー＆ペーストして実際に試してみてください。