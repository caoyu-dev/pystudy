#https://dmoj.ca/problem/coci08c3p2

def decode(sentence):
    vowels = "aeiou"
    i = 0
    n = len(sentence)
    decoded_sentence = ""

    while i < n:
        if sentence[i] in vowels:
            decoded_sentence += sentence[i]
            i += 3  # 모음 뒤에 'p' 와 같은 모음을 추가했으므로, 3개 문자를 건너뜁니다.
        else:
            decoded_sentence += sentence[i]
            i += 1  # 모음이 아닌 경우에는 다음 문자로 진행합니다.

    return decoded_sentence

# 입력 받기
coded_sentence = input()
# 암호 해독
decoded_sentence = decode(coded_sentence)
# 결과 출력
print(decoded_sentence)

