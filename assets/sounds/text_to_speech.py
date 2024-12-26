from google.cloud import texttospeech

# 클라이언트 생성
client = texttospeech.TextToSpeechClient()

# 텍스트 요청
synthesis_input = texttospeech.SynthesisInput(text="안녕하세요. 구글 TTS 서비스입니다.")

# 음성 요청 구성
voice = texttospeech.VoiceSelectionParams(
    language_code="ko-KR",
    name="ko-KR-Standard-A"
)

# 오디오 설정
audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

# 음성 합성 요청
response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

# 오디오 저장
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print("오디오 파일이 output.mp3로 저장되었습니다.")
