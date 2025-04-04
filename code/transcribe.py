#!/usr/bin/env python3
import os
import logging
import argparse
import whisper

def main():
    # コマンドライン引数のパース
    parser = argparse.ArgumentParser(description="Whisperを使った音声文字起こし")
    parser.add_argument("--file_path", required=True, help="音声ファイルのパスを指定します")
    args = parser.parse_args()

    ########
    # 初期設定
    ########
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s'
    )

    # 現在のディレクトリが "transcribe_interview" になるまで上位ディレクトリに移動する
    root_dir = 'transcribe_interview'
    while os.path.basename(os.getcwd()) != root_dir:
        os.chdir('..')
    logging.info("Current working directory: %s", os.getcwd())

    ########
    # Whisper モデルの読み込み
    ########
    logging.info("Loading Whisper model...")
    model = whisper.load_model("base")
    logging.info("Model loaded successfully.")

    ########
    # 音声ファイルの文字起こし処理
    ########
    audio_name = args.file_path
    audio_file = os.path.join('data/input', audio_name)
    logging.info("Audio file path: %s", audio_file)
    
    # 音声ファイルの存在確認
    if not os.path.exists(audio_file):
        logging.error("Audio file does not exist: %s", audio_file)
        raise FileNotFoundError(f"Audio file does not exist: {audio_file}")

    # Whisperによる文字起こし（言語指定と温度の設定）
    result = model.transcribe(audio_file, language="ja", temperature=0.0)
    logging.info("Transcription completed.")

    # data/output.txtに結果を保存
    output_dir = 'data/output'
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'output_{audio_name}.txt')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result['text'])

if __name__ == "__main__":
    main()
