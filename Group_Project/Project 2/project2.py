"""이름으로 구문 만들기 프로그램.

프로그램 개요: 
    1) 이름을 입력하면, 사전 파일의 단어 중 이름의 철자를 활용하여 만들 수 있는 단어의 목록을 보여줌.
    2) 그 중 한 단어를 입력하면 선택한 단어를 1의 목록에서 제외하고, 
       그 단어의 알파벳 개수를 제외한 알파벳들로 만들 수 있는 단어 목록을 보여줌.
    3) 선택할 수 있는 단어가 없을 때까지 과정 2를 반복함.
    3-1) 반복 도중 'q'를 입력하면 프로그램을 종료할 수 있음.
    3-2) 선택할 수 있는 단어가 더이상 없으면 다시 시작하거나, 종료할 수 있음.

구성 함수:
    filter_words:
        가용한 알파벳 개수 내에서 만들 수 있는 단어 목록을 재조정하는 함수. 
        단어 목록에서 기준에 부합하지 않는 빈도수의 알파벳을 포함한 단어를 탈락시킴.
    display_words:
        단어 목록을 한 줄에 7개씩 가독성 있게 출력하는 함수
    modify_chars_dict:
        선택한 단어의 알파벳 개수를 제외시킨 후 가용한 알파벳 개수를 재조정하는 함수.
    make_phrase:
        이름을 입력 받고, 위의 두 함수를 활용하여 구문을 만드는 함수.

의사코드:
    만들어진 구문을 레드라인으로 출력하기 위해 sys 모듈을 import 한다.
    dictionary.txt 파일을 append 모드로 연다.
        [i, a]를 개행(\n)으로 join하여 파일에 추가한다.
    dictionary.txt 파일을 읽기 모드로 가져온다.
        한 줄(한 단어)씩 읽어들여 리스트 형태로 data에 저장한다.
    data에 있는 단어에서 '%'와 '!', 개행문자(\n)를 제거한 후 dictionary에 저장한다.
    
    make_phrase(dictionary) 호출
    {
        영문 full name을 입력받는다.
        입력 받은 이름을 구성하는 알파벳과 그 개수로 딕셔너리를 만든다.
        사전 내 단어 중 이름을 구성하는 알파벳으로 만들 수 있는 단어(알파벳 부분집합)를 고른다.
        filter_words(가용 알파벳 딕셔너리, 부분집합 단어 리스트) 호출
        {
            부분집합의 단어 중 가용한 알파벳 개수 내에서 만들 수 있는 단어를 선정한다.
        }
        display_words(선정한 단어 리스트) 호출
        {
            선택 가능한 모든 단어(단어 리스트)를 출력한다.
        }
        while (선택할 수 있는 단어가 없을 때까지) do
            q 또는 단어들 중 하나를 입력 받는다.
            if (q를 입력한 경우) then
                프로그램을 종료한다.
            else if (단어 리스트 내 단어를 고른 경우) then
                modify_chars_dict(가용 알파벳 딕셔너리, 선택한 단어) 호출
                {
                    가용 알파벳 딕셔너리에서 선택한 단어의 알파벳 개수를 제외한다.
                }
                구문 리스트에 선택한 단어를 추가한다.
                선택한 단어를 단어 리스트에서 제거한다.
                filter_words(가용 알파벳 딕셔너리, 선택한 단어를 제외한 단어 리스트) 호출
                {
                    선택 단어를 제외한 단어들 중 가용한 알파벳 개수 내에서 만들 수 있는 단어(남은 단어)를 선정한다.
                }
                선택한 단어를 구문으로 출력한다.
            else
                잘못 선택했음을 출력한다.
            endif
            display_words(선정한 단어 리스트) 호출
            {
                선택 가능한 남은 단어들을 출력한다.
            }            
        endwhile

        선택할 수 있는 단어가 없음을 출력한다.

        while (true) do
            다시 시작할지, 그만둘지 묻는 메시지를 출력한다.
            의사를 입력받는다.
            if (다시 시작을 입력할 경우) then
                make_phrase(dictionary)를 재호출한다.
            endif

            if (그만두기를 입력할 경우) then
                프로그램을 종료한다.
            else
                잘못 선택했음을 출력한다.
            endif
        endwhile
    }
"""
import sys
def filter_words(char_counts, word_list):
    """
    사용 가능한 알파벳 개수 내에서 만들 수 있는 단어 목록을 재조정하는 함수.
        입력: 
            char_count: dict, {가용한 알파벳 : 해당 알파벳의 개수} 쌍으로 이루어진 딕셔너리.
            word_list: list, 재조정 전 단어 리스트.
        출력:
            list, 가용한 알파벳 개수 내에서 만들 수 있는 단어들이 정렬된 리스트.

    주요변수:
        target_words: 
                현재 가용한 알파벳 개수로는 만들 수 없는 단어로 이루어진 리스트. 
                삭제될 대상(target)이기 때문에 target_words이라는 변수명을 가짐.
    """
    target_words = [word for word in word_list\
                    for ch in set(word)\
                    if word.count(ch) > char_counts[ch]]
    return sorted(set(word_list) - set(target_words))

def display_words(msg, word_list):
    """
    단어 목록을 한 줄에 7개씩 가독성 있게 출력하는 함수.
    입력:
        msg: str, 단어 목록의 종류를 알려주는 메시지.
        word_list: list, 가용한 알파벳을 활용하여 만들어진 단어 목록이 담긴 리스트. 

    주요변수:
        line: '-' 75개로 이루어진 대시라인. 대시('-')의 하드코딩을 피하기 위함.
    """
    line = '-' * 75
    print(f"\n{msg}")
    print(line)
    for idx, word in enumerate(word_list):
        if idx > 0 and idx % 7 == 0:
            print()
        print(f'{word:10s}', end=' ')
    print()
    print(line)
def modify_chars_dict(char_counts, word):
    """
    선택한 단어의 알파벳 개수를 제외시킨 후 가용한 알파벳 개수를 재조정하는 함수. 
    
    입력: 
        char_counts: dict, 가용한 알파벳 딕셔너리.
        word: str, 선택한 단어.
    출력: 
        char_counts: dict, 조정된 가용 알파벳 딕셔너리.
    """
    for char in set(word):
        char_counts[char] -= word.count(char)
    return char_counts

def make_phrase(dict_words):
    """
    이름을 입력 받고, 사전 파일 내 단어 목록에서 이름으로 만들 수 있는 단어를 선택해 구문을 만드는 함수.
    
    입력:
        dict_words: list, 사전 파일 내 단어 목록이 담긴 리스트. 해당 목록을 활용해 선택 가능한 단어를 출력함.

    주요변수:
        name: 사용자가 입력한 full name. 모두 소문자화하여 저장함.
        name_chars: name에서 알파벳인 단어만 골라 '{알파벳:알파벳 개수}' 쌍을 저장한 딕셔너리.
        name_subset_words: name에 사용된 알파벳의 종류보다 적거나 같은 알파벳으로 구성된 단어 리스트.
        phrase: 사용자가 선택한 단어를 담는 리스트.
        filtered_words: 현재 가용한 알파벳 개수를 가지고 만들 수 있는 단어 리스트.
        choice: 사용자가 목록에 있는 단어 중 하나를 택하여 입력한 값. 모두 소문자화된 스트링.
        restart: 프로그램 재시작 여부에 관한 의사를 저장한 값. 1이면 재시작, 2이면 종료.
    """
    print('\n<이름으로 구문 만들기 프로그램>')
    name = input('영문 성명(full name)을 입력하세요 >>> ').lower()
    
    # 특수문자, 공백 등을 제외한 알파벳만으로 '알파벳:알파벳 개수'의 키:값 쌍 생성
    name_chars = {ch:name.count(ch) for ch in set(name) if ch.isalpha()}
    
    # 사전 내 모든 단어의 알파벳을 조사하지 않기 위해
    # 이름의 알파벳으로만 만들 수 있는 단어를 먼저 사전에서 뽑는다.(부분집합 단어)
    name_subset_words = [word for word in dict_words \
                         if set(word) <= set(name)]
    filtered_words = filter_words(name_chars, name_subset_words)
    display_words('선택 가능 단어 목록', filtered_words)
    
    phrase = [] # 선택한 단어를 담을 리스트
    while filtered_words:
        print("목록의 단어 중 하나를 입력하세요(종료하려면 'q'를 입력하세요)")
        choice = input('입력 >>> ').lower()
        
        # 'quit'은 dictionary에 존재하는 단어라 부득이하게 'q'로 변경하였다.
        if choice == 'q':
            sys.exit()
        elif choice in filtered_words:
            name_chars = modify_chars_dict(name_chars, choice)
            phrase.append(choice)
            filtered_words.remove(choice)
            filtered_words = filter_words(name_chars, filtered_words)
            print('만들어진 구문: ', *phrase, file=sys.stderr)
        else: 
            print('잘못 입력하셨습니다. 다시 입력하세요.')
        display_words('선택 가능 단어 목록(남은 단어)', filtered_words)
    print('\n남은 단어가 없습니다.')
    while True:
        print('''원하는 메뉴를 입력하세요.
-----------------------------------------
   1) 처음부터 다시시작      2) 그만두기 
-----------------------------------------''')
        restart = input('입력 >>> ')
        if restart == '1':
            return make_phrase(dictionary)
        if restart == '2':
            sys.exit()
        else:
            print('\n잘못 입력하셨습니다. 다시 입력하세요.')

FILE_NAME = 'dictionary.txt'
# i, a를 파일에 추가하기 위해 추가 모드로 열고 write하였다.
with open(FILE_NAME, 'a') as file:
    file.writelines('\n'.join(['i', 'a']))
with open(FILE_NAME, 'rt', encoding='UTF8') as file:
    data = file.readlines()
dictionary = [word.replace('%', '').replace('!', '').strip() for word in data]
# 반복 실행 시 같은 사전 파일을 사용하기 때문에,
# 파일 R/W를 한 번만 하기 위해 main 부분에서 파일을 읽고 함수의 인자로 넘겨주었다.
make_phrase(dictionary)
