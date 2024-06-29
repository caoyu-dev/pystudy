#(ccc15j2) Happy Or Sad

# 행복, 슬픔 둘 다 없음: `none`
# 행복, 슬픔 갯수 동일: `unsure`
# 행복 > 슬픔: `happy`
# 행복 < 슬픔: `sad`
def determine_mood(message):
    # 행복과 슬픔 이모티콘 갯수 세기
    happy_count = message.count(':-)')
    sad_count = message.count(':-(')

    # 갯수에 따른 글 분위기 결정하기
    if happy_count == 0 and sad_count == 0:
        return "none"
    elif happy_count == sad_count:
        return "unsure"
    elif happy_count > sad_count:
        return "happy"
    else:
        return "sad"

# 실행
input_text = input().strip()
result = determine_mood(input_text)
print(result)
