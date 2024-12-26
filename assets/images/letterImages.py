from PIL import Image, ImageDraw, ImageFont
import os

# 자음/모음 리스트
letters = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ",
           "ㅏ", "ㅑ", "ㅓ", "ㅕ", "ㅗ", "ㅛ", "ㅜ", "ㅠ", "ㅡ", "ㅣ"]

# 이미지 저장 디렉토리 생성
output_dir = "assets/images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 폰트 경로 설정 (MacOS 기준 예제)
font_path = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"

# 이미지 생성 함수
def create_image(text, filename):
    img = Image.new("RGB", (200, 200), color="white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, 100)

    # 텍스트 크기 계산 (textbbox 사용)
    text_bbox = draw.textbbox((0, 0), text, font=font)  # 텍스트의 경계 상자 반환
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # 텍스트 위치 계산 (중앙 정렬)
    position = ((200 - text_width) // 2, (200 - text_height) // 2)
    draw.text(position, text, fill="black", font=font)

    img.save(filename)
    print(f"Image saved to {filename}")

# 자음/모음 각각 이미지 생성
for letter in letters:
    file_path = f"{output_dir}/{letter}.png"
    create_image(letter, file_path)
