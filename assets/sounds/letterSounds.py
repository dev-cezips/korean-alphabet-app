from google.cloud import texttospeech
import os

# 환경 변수에서 API 키 로드
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "famous-robot-445714-j7-a8fcd42ac958.json"

# Text-to-Speech 클라이언트 생성
client = texttospeech.TextToSpeechClient()

# 자음/모음 리스트
letters = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ", "ㅏ", "ㅑ", "ㅓ", "ㅕ", "ㅗ", "ㅛ", "ㅜ", "ㅠ", "ㅡ", "ㅣ"]

# 음성 파일 생성 함수
def generate_audio(text, filename):
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(language_code="ko-KR", name="ko-KR-Standard-A")
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    with open(filename, "wb") as out:
        out.write(response.audio_content)
        print(f"Audio content written to {filename}")

# 자음/모음별 음성 생성
for letter in letters:
    filename = f"assets/sounds/{letter}.mp3"
    generate_audio(letter, filename)