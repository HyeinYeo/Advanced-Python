"""
텍스트 파일에서 회문인 단어를 찾아 출력하는 프로그램.

입력: dictionary.txt 텍스트 파일
출력: 회문인 단어 리스트 ***회문| r-a-d-a-r과 같이 거꾸로 돌려도 동일한 단어

주요 변수:
    FILE_NAME(str): 사용할 파일명(또는 파일 경로)
    data(list): 텍스트 파일을 한 줄씩 읽어들인 단어 리스트
    word_list(list): 회문 판단을 위해 data의 각 단어를 글자 단위로 순회하며 공백, 특수문자를 제거 후 담는 리스트
    palindromes(list): word_list를 순회하며 글자 수가 1보다 큰 회문을 발견하면 담는 리스트

세부 기능 및 특징:
    회문 판단 시엔 보통 낱말 사이에 있는 띄어쓰기나 문장부호는 무시한다.
    따라서, dictionary.txt 파일에 포함된 단어들에 대해 띄어쓰기와 문장부호를 모두 제거하고 알파벳만 남긴다.
    회문 판단 시, 한 글자로 이루어진 단어는 회문으로 판단하지 않는다.
    단어를 역순으로 뒤집은 단어가 원 단어와 같으면 회문으로 판단하고, 해당 단어를 회문 리스트에 추가한다.
    최종 회문 리스트를 출력한다.
"""
# 1. 파일을 불러온다.
FILE_NAME = 'dictionary.txt'
with open(FILE_NAME, 'rt', encoding='UTF8') as file:
    # 2. 파일 내의 단어를 하나씩 읽어들여 리스트에 담는다.
    data = file.readlines()

# 3. 회문은 단어 사이의 띄어쓰기나 문장부호를 무시하므로, 단어에서 알파벳 이외의 문자를 제외하고 알파벳만 남긴다.
word_list = [''.join([ch for ch in word if ch.isalpha()]) for word in data]

# 4. 단어의 길이가 1보다 크고, 단어를 역순으로 뒤집은 단어가 원 단어와 같다면 회문이므로 회문 리스트에 단어를 추가한다.
palindromes = [word for word in word_list \
               if len(word) > 1 and word == word[::-1]]

# 5. 회문인 단어만을 담은 리스트를 출력한다.
print(palindromes)
