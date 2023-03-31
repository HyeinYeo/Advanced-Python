"""
편의점에서 사람이 물건을 구매하는 프로그램.

추가 기능:
    회원 등급제: 등급별 차등 할인율
    장바구니
    포인트 결제
    랜덤 포인트 리워드 이벤트
    구매 일시별 이용내역 열람
    편의점 매출 그래프로 조회
    고객별 누적 금액 그래프로 조회

프로그램 설명:
    다음과 같은 방식으로 '편의점에서 사람이 물건을 구매'할 수 있도록 한다.
    0. 편의점 생성
    1. 고객 캐릭터(사람) 등록
    2. 고객 관점
        1) 등록된 캐릭터 중 편의점을 이용하고자 하는 캐릭터를 선택한다.
        2) 선택한 캐릭터로 다음과 같은 행동을 할 수 있다.
            - 돈 벌기
            - 편의점에서 물건 사기
                - 장바구니에 담기
                - 장바구니에서 삭제
                - 장바구니 비우기
                - 장바구니 조회
                - 결제하기
                - 편의점 나가기
            - 잔액 조회하기
            - 편의점 이용 정보 조회하기
    3. 편의점 관리자 관점
        1) 편의점 관리하기에서 다음과 같은 행동을 할 수 있다.
            - 물건 등록
            - 할인 이벤트 생성
            - 재고 목록 조회
            - 수입 조회
            - 매출 현황 분석
            - 고객 명단 조회
            - 고객 현황 분석       
    
기능:
    클래스:
        InputError:
            사용자 정의 에러를 생성하기 위해 사용되는 클래스.
        CartItem:
            장바구니 내 아이템 객체를 생성하기 위해 사용되는 클래스.
        Product: 
            상품 객체를 생성하기 위해 사용되는 클래스.
        Store: 
            편의점 객체를 생성하기 위해 사용되는 클래스.
        Customer: 
            사람 객체를 생성하기 위해 사용되는 클래스.
        Cart:
            장바구니 객체를 생성하기 위해 사용되는 클래스.
        Main: 
            프로그램 구동 객체를 만들기 위한 메인 클래스.
    함수:
        main: 프로그램을 실행하는 메인 함수.
        
의사코드:
    편의점 이름을 입력받는다.
    입력 받은 이름으로 Store(편의점) 객체를 생성한다.
    
    메인 메뉴를 실행한다.
    while (True) do
        메인 메뉴를 입력받는다.
        
        if (1번 메뉴(사람 생성)) then
            생성할 사람의 이름을 입력받는다.
            입력 받은 이름으로 Person(사람) 객체를 생성한다.
            생성한 객체를 person 리스트에 담는다.
            
        elif (2번 메뉴(사람 선택)) then
            생성된 사람 리스트를 보여준다.
            사람 코드를 입력받는다.
            
            if (선택한 사람이 person 리스트에 존재하는 경우) then
            
                사람 입장에서의 행동(기능)을 선택하는 메뉴를 실행한다.
                while (True) do
                    if (1번(돈 벌기) 선택) then
                        번 돈을 입력받아 사람 객체의 잔액에 더한다.
                    elif (2번(편의점 이용) 선택) then
                        장바구니를 생성한다.
                        while (True) do
                            편의점 재고 목록을 보여준다.
                            장바구니에 담긴 상품을 보여준다.
                            if (q(편의점 나가기) 선택) then
                                장바구니를 모두 비운다.
                                사람 입장에서의 행동을 선택하는 메뉴로 되돌아간다.
                            elif (1번(장바구니 담기) 선택) then
                                편의점 재고목록에서 장바구니에 담을 상품과 수량을 선택해 입력한다.
                                입력한 정보로 장바구니 물품 객체를 생성한다.
                                장바구니 객체의 장바구니 딕셔너리에 장바구니 물품 객체를 저장한다.
                            elif (2번(장바구니에서 삭제)) then
                                장바구니에서 제거할 상품 코드를 입력받는다.
                                제거할 개수를 입력받는다.
                                제거할 개수가 장바구니에 존재하는 수량과 같거나 많은 경우,
                                    편의점 내 해당 상품의 재고량을 장바구니에 담긴 수량만큼 증가시킨다.
                                    장바구니에서 해당 상품을 제거한다.
                                제거할 개수가 장바구니에 존재하는 수량보다 적은 경우,
                                    장바구니 내 해당 상품의 수량을 제거할 개수만큼 감소시킨다.
                                    편의점 내 해당 상품의 재고량을 제거한 개수만큼 증가시킨다.
                                장바구니에 담은 상품의 총액을 계산한다.
                            elif (3번(장바구니 비우기) 선택) then
                                장바구니 내 모든 상품들에 대해,
                                    편의점 내 상품들의 재고량을 장바구니에 담은 수량만큼 증가시킨다.
                                장바구니 딕셔너리 내 요소를 모두 삭제한다.
                            elif (4번(장바구니 조회) 선택) then
                                장바구니 내 모든 상품들에 대해,
                                    '상품코드 | 상품명 | 단가 | 담은수량'을 출력한다.
                            elif (5번(결제하기) 선택) then
                                if 잔액 < 장바구니에 담은 상품 총액 then
                                    결제를 취소한다.
                                else
                                    사용할 포인트를 입력받는다.
                                    장바구니에 담은 상품 총액을 입력받은 사용 포인트만큼 감소시킨다.
                                    
                                    현재 시간 정보를 장바구니 객체의 시간 변수에 저장한다.
                                    구매 영수증을 보여준다.
                        
                                    구매 정보를 바탕으로 항목들을 재조정한다.
                                    {
                                        편의점 객체의 편의점 수입을 구매액만큼 증가시킨다.
                                        편의점의 상품 판매액과 판매량을 구매 상품 가격, 구매 수량만큼 증가시킨다.
                                        고객 객체의 잔액을 구매액만큼 감소시킨다.
                                        구매액에 포인트 적립 비율을 곱해 포인트를 계산한다.
                                        고객 객체의 누적 포인트를 새로운 포인트만큼 증가시킨다.
                                        고객 객체의 누적 구매액을 구매액만큼 증가시킨다.
                                        고객 객체의 구매 내역 리스트에 장바구니 객체를 추가시킨다.
                                        고객 객체의 등급을 누적 구매액 기준으로 갱신한다.
                                        편의점 객체의 고객 리스트에 고객 객체를 추가시킨다.
                                    }
                                    고객 객체의 잔액을 출력한다.
                                    
                                    랜덤 포인트 리워드를 받을지 여부를 입력받는다.
                                    if 수령 여부 == 'Y' then
                                        포인트 리워드를 수령하여 고객 객체의 누적 포인트에 적립한다.
                                    endif
                                    
                            else
                                while-loop를 재실행한다.
                            endif
                        endwhile
                        
                    elif (3번(잔액 조회하기) 선택) then
                        고객 객체의 잔액을 출력한다.
                    
                    elif (4번(편의점 이용 정보 조회) 선택) then
                        조회할 항목의 메뉴를 입력받는다.
                        
                        if (1번(구매 내역) 선택) then
                            고객 객체의 구매 내역 리스트를 출력한다.
                        elif (2번(누적 구매액 & 회원 등급) 선택) then
                            고객 객체의 누적 구매액과 고객 등급을 출력한다.
                        elif (3번(누적 포인트) 선택) then
                            고객 객체의 구매 내역을 출력한다.
                        elif (q 선택) then
                            편의점 이용 정보 조회에서 나간다.
                        else
                            없는 메뉴를 입력했음을 출력한다.
                        endif
                        편의점 이용 정보 조회를 재실행한다.
                    
                    elif (q 선택) then
                        사람 입장에서의 행동을 선택하는 메뉴에서 나가서 메인 메뉴로 돌아간다.
                    else
                        메뉴를 잘못 선택했음을 출력한다.
                    endif
                endwhile
            else # 선택한 사람이 person 리스트에 존재하지 않는 경우
                없는 사람임을 출력한다.
            endif
            
        elif (3번 메뉴(편의점 관리하기)) then
            if (1번(물건 등록) 선택) then
                등록할 물건 이름, 단가, 수량을 입력받는다.
                (이름, 단가, 수량)으로 Product(물건) 객체를 생성한다.
                새로 생성한 물건 객체를 편의점 객체의 재고 목록에 추가한다.
                
            elif (2번(할인 이벤트 생성) 선택) then
                if (편의점 객체의 재고 목록이 비어있으면) then
                현재 재고 목록을 보여준다.
                할인 이벤트를 적용할 상품 코드를 입력 받는다.
                상품 코드로 재고 목록의 물건 객체를 찾는다.
                적용할 할인율을 입력받는다.
                물건 객체의 상품 원가에 할인율을 적용한 가격을 계산한다. 
                물건 객체의 단가를 할인 가격으로 갱신한다.
                
            elif (3번(재고 목록 조회) 선택) then
                편의점 객체의 재고 목록을 출력한다.
                
            elif (4번(수입 조회) 선택) then
                편의점 객체의 총 수입을 출력한다.
                
            elif (5번(매출 현황 분석) 선택) then
                편의점 객체 재고목록 내 상품들에 대해,
                    (상품코드, 상품명, 판매량, 판매액)의 튜플을 원소로 하는 매출 정보 리스트를 생성한다.
                
                while (Ture) do
                    if (q 선택) then
                        매출 현황 조회를 종료한다.
                        편의점 관리 메뉴로 되돌아간다.
                    elif (1번(판매량 기준) 선택) then
                        판매량에 따라 매출 정보 리스트를 오름차순 정렬한다.
                        x축을 상품명, y축을 판매량으로 하는 횡형 막대 그래프를 출력한다.
                    elif (2번(판매액 기준) 선택) then
                        판매액에 따라 매출 정보 리스트를 오름차순 정렬한다.
                        x축을 상품명, y축을 판매액으로 하는 횡형 막대 그래프를 출력한다.
                    elif (3번(전체 상품 현황) 선택) then
                        매출 정보 리스트를 출력한다.
                    else
                        옵션을 잘못 선택했음을 출력한다.
                        while-loop를 재실행한다.
                    endif
                endwhile
            
            elif (6번(고객 명단 조회) 선택) then
                편의점 객체의 고객 명단을 출력한다.
                
            elif (7번(고객 현황 분석) 선택) then
                편의점 객체의 고객 리스트 내 고객 객체에 대해,
                    (고객 코드, 고객명, 누적 구매액, 고객 등급)의 튜플을 원소로 하는 고객 정보 리스트를 생성한다.
                    누적 구매액에 따라 고객 정보 리스트를 내림차순 정렬한다.
                    x축을 고객명, y축을 누적 구매액으로 하는 세로형 막대 그래프를 출력한다.
                    
            elif (q 선택) then
                편의점 관리에서 나가서 메인 메뉴로 돌아간다.
            else
                메뉴를 잘못 선택했음을 출력한다.
            endif
        
        elif (q 선택) then
            프로그램을 종료한다.
        else
            메뉴를 잘못 선택했음을 출력한다.
        endif
    endwhile
"""

from abc import abstractmethod, ABCMeta
from datetime import datetime
from dataclasses import dataclass
import platform
import sys
import random
import time
import matplotlib.pyplot as plt
import numpy as np

# 그래프 이용 시 한글 폰트 깨짐 문제해결용 코드
if platform.system() == 'Windows': # Window
    plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin': # Mac
    plt.rc('font', family='AppleGothic')
else: #linux
    plt.rc('font', family='NanumGothic')
    
# 사용자 정의 에러
class InputError(Exception):
    """사용자 정의 에러를 생성하기 위해 사용되는 클래스."""
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

def test_error(func):
    """
    input() 에러를 관리하고 원하는 메시지를 출력하기 위한 함수.
    """
    def inner(msg, *option):
        value = func(msg, *option)
        if option and value == 'q': # 옵션이 활성화되어 있고, 입력이 q인 경우
            return 'q'
        try:
            if not str(value).isdigit() or int(value) == 0:
                raise InputError('1 이상의 자연수만 입력 가능합니다.')
        except InputError as err:
            print(err)
            return func(msg, *option)
        return int(value)
    return inner

@test_error
def input_num(msg):
    """
    입력을 받고 에러 검사 후 에러가 없으면 입력값을 리턴하는 함수.
    
    msg: 어떤 입력값인지 알려주는 메시지
    """
    value = input(f'{msg}: ')
    return value

@test_error
def input_num_quit(msg, option):
    """
    입력을 받고 에러 검사 후 에러가 없으면 입력값을 리턴하는 함수.
    q 입력 시 나가기 기능을 지원한다.
    
    msg: 어떤 입력값인지 알려주는 메시지
    option: 나가기 기능 활성화 여부
    """
    value = input(f'{msg}: ')
    return value.lower()

@dataclass 
class CartItem:
    """
    장바구니에 담은 상품을 관리하기 위한 클래스.
    """
    name: str
    price: int
    quantity: int

class Product:
    """
    상품 객체를 생성하기 위해 사용되는 클래스.
    
    속성:
        cnt: int, 상품의 고유코드를 생성하기 위한 클래스 변수. 객체가 생성될 때마다 1씩 값이 증가함.
        cnt: int, 상품의 고유코드를 나타내는 인스턴스 변수. 객체 생성 시 클래스 변수인 cnt값을 전달받음.
        name: str, 상품 이름.
        price: int, 상품 단가.
        quantity: int, 상품 수량.
        discount: int, 상품 할인율.(기본값=0)
        prime_cost: int, 상품 원가.
        sales: int, 판매액
        sale_quantity: int, 판매량

    메서드:
        register(info): (상품 이름, 가격, 수량) 정보가 포함된 튜플을 인자로 받아 상품을 등록한다.
    """
    cnt = 0
    
    def __init__(self, name, price, quantity, discount=0):
        """
        상품의 고유코드(code), 이름(name), 가격(price), 
        수량(quantity), 할인율(discount)을 초기화하는 생성자 함수.

        입력:
            name: str, 상품 이름.
            price: int, 상품 단가.
            quantity: int, 상품 수량.
            discount: int, 상품 할인율.(기본값=0)

        기능:
            객체가 새롭게 생성될 때 마다 Product.cnt의 값을 1 만큼 증가시킨 후 상품 고유 코드(code)로 할당한다.
        """
        Product.cnt += 1
        self.code = Product.cnt
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount = discount
        self.prime_cost = price # 원가
        
        # new ------------
        self.sales = 0 # 판매액
        self.sale_quantity = 0 # 판매량
    
    @classmethod
    def register(cls, info):
        """
        상품의 이름, 가격, 수량 정보를 가지고 상품을 등록하는 클래스 메서드.
        
        입력:
            info: tuple, (상품명, 가격, 수량 정보)로 구성된 튜플.
    
        출력:
            Product 객체
    
        기능:
            튜플 형식으로 전달 받은 상품 정보 인자로 Product 객체를 생성한다.
        """
        return cls(info[0], info[1], info[2])

    def __str__(self):
        """
        상품 정보를 가독성 있게 출력하기 위한 함수.

        출력:
            상품코드, 상품명, 단가, 수량, 할인율이 포함된 문장

        기능:
            기존 __str__의 문자열 반환기능을 오버라이딩하여 return 값의 형식대로 출력되도록 한다.        
        """
        return f'  상품코드: {str(self.code)} | 상품명: {self.name} | 단가: \
{str(self.price)}원 | 수량: {str(self.quantity)}개 | 할인율: {str(self.discount)}%'

class AbstractStore(metaclass=ABCMeta):
    """
    Store 클래스의 추상 클래스.
    """
    store = '이름'
    income = '총 수입'
    customer = '고객 명단'
    inventory = '재고 목록'
    pay_point = '차감할 고객의 포인트'
    tier_rate = '고객 등급별 할인율'
    tier_criteria = '고객 등급 기준선'
    
    
    @abstractmethod
    def register_stock(self):
        """물건 객체를 생성하여 재고 목록에 등록"""
        pass
    
    @abstractmethod
    def make_discount(self):
        """특정 상품에 할인 적용"""
        pass

    @abstractmethod
    def show_income(self):
        """현재 총 수입 출력"""
        pass

    @abstractmethod
    def register_customer(self, member):
        """인자로 받은 고객 객체를 명단에 등록"""
        pass

    @abstractmethod
    def show_customer(self):
        """고객 명단 출력"""
        pass
    
    @abstractmethod
    def show_customer_ranking(self):
        """누적 구매액에 따른 고객 순위 그래프로 표현"""
        pass
    @abstractmethod
    def show_sales_statement(self):
        """매출 현황을 판매량, 판매액, 전체 상품 등의 기준으로 그래프 표현"""
        pass    

class Store(AbstractStore):
    """
    편의점 객체를 생성하기 위해 사용되는 클래스.

    속성:
        store_name: str, 편의점 이름. 총 수입(income), 고객 명단(customer), 재고목록(inventory)
        __income: int, 편의점의 총 수입. 은닉된 정보. 0으로 초기화
        customer: list, 고객 명단. 고객 객체가 리스트에 저장됨. 
        inventory: dict, 재고목록. 각 재고의 정보는 '상품코드:상품객체' 쌍으로 딕셔너리에 저장됨. 
        pay_point: int, 고객들이 포인트 결제한 총액
        tier_rate: dict, 고객 등급별 할인율.
        tier_criteria: dict, 고객 등업 누적 구매액 기준

    메서드:
        register_stock: 상품에 관한 정보를 입력받은 뒤 Product 객체를 생성하고 상품을 재고 목록에 등록한다.
        is_empty: 재고 목록이 비었는지 확인한다.
        show_inventory: 재고 목록을 출력한다.
        search_item: 상품 코드를 인자로 받아, 해당 코드를 가진 상품을 찾는다. 
        make_discount: 특정 상품에 할인 이벤트를 적용한다. 
        show_income: 편의점의 총 수입을 출력한다.
        register_customer: 고객 리스트에 고객 객체를 등록한다.
        show_customer: 고객 명단을 출력한다.
        is_stock_lack: 구매하고자 하는 상품의 재고가 부족한지 체크한다.
        update_sale_info: 고객등급별 할인율을 고려하여 특정 상품의 매출액과 매출량을 갱신한다.
        show_customer_ranking: 누적 구매액에 따른 고객 순위를 그래프로 나타낸다. 
        show_sales_statement: 매출 현황을 다양한 기준(판매량, 판매액, 전체 상품 현황)으로 나타낸다.
    """
    
    def __init__(self, store_name):
        """
        편의점 이름(store_name), 총 수입(income), 고객 명단(customer), 
        재고 목록(inventory)을 초기화하는 생성자 함수.
        
        입력:
            store_name: str, 편의점 이름.

        기능:
            편의점 이름은 객체 생성 시 전달 받은 인자로 초기화한다.
            총 수입의 초기값은 0으로 초기화한다.
            고객 명단과 재고 목록은 빈 리스트와 빈 딕셔너리로 초기화한다.
            고객들이 포인트 결제한 총액을 0으로 초기화한다.
            고객 등급에 따라 할인율을 차등 설정한다. (10%, 6%, 3%, 0%, 0%)
            누적 구매액에 따른 등급 변경 기준을 설정한다. (10만원, 5만원, 3만원, 1원, 0원)
            
        """ 
        self.store_name = store_name # 편의점 이름
        self.__income = 0            # 총 수입 
        self.customer = []           # 고객 명단
        self.inventory = dict()      # 재고 목록
        
        # new 기능 --------------------------------------------------
        self.pay_point = 0           # 포인트 결제 총액
        self.tier_rate = {'Gold':10, 
                          'Silver':6, 
                          'Bronze':3, 
                          'Iron':0, 
                          'NonMember': 0} # 등급별 할인율
        
        self.tier_criteria = {'Gold':100000, 
                              'Silver':60000, 
                              'Bronze':30000, 
                              'Iron':1,
                              'NonMember': 0} # 등업 누적구매액 기준

    @property
    def income(self):
        """
        보안을 위해 은닉된 총 수입(income)을 조회하기 위한 함수.

        기능:
            은닉된 총 수입 변수에 접근해 리턴 받을 수 있게 한다.
        """
        return self.__income
    
    @income.setter
    def income(self, input_income):
        """
        보안을 위해 은닉된 총 수입(income)을 변경하기 위한 함수.
        
        기능:
            은닉된 총 수입 변수에 접근해 입력받은 함수의 인자(input_income)로 값을 변경한다.
        """
        self.__income = input_income

    # 상품 입고
    def register_stock(self):
        """
        상품에 관한 정보를 입력받은 뒤 Product 객체를 생성하고 상품을 재고 목록에 등록하는 함수.
        
        기능:
            상품 이름(name), 단가(price), 수량(quantity) 정보를 입력받는다.
            입력 받은 정보를 튜플 형태로 만든다.
            튜플을 Product 클래스의 register 함수의 매개변수로 전달하여 Product 객체를 생성한다.
            만들어진 상품 객체를 재고 목록에 추가한다.
            이미 있는 상품일 경우 수량만 추가한다.
        """
        name = input('입고할 물건: ')
        input_price = test_error(input_num)
        input_quantity = test_error(input_num)
        
        for code in self.inventory:
            if self.inventory[code].name == name:
                print(f'{name}(은/는) 재고 목록에 존재하는 상품입니다.')
                quantity = input_quantity('추가 입고 수량(개)')
                self.inventory[code].quantity += quantity
                print(f'{name}(이/가) {quantity}개 추가 입고 완료되었습니다.')
                return
            
        price = input_price('물건 단가(원)')
        quantity = input_quantity('입고 수량(개)')
        
        stock_info = name, price, quantity
        new_product = Product.register(stock_info)
        self.inventory[new_product.code] = new_product
        print(f'단가 {price}원의 {name}(이/가) {quantity}개 새로 입고 완료되었습니다.')

    
    # 재고 목록 비어있는지 확인(편의점에 상품 목록이 하나라도 존재하는지)
    def is_empty(self):
        """
        재고 목록이 비어있는지 확인하는 함수.
        
        기능:
            재고가 비어있으면 비어있음이(is empty) 참이라는 뜻의 True를 반환함.
        """
        if not self.inventory:
            print(f'{self.store_name}에 아무 상품도 없습니다.')
            return True
        return False
    
    # 재고 목록 조회
    def show_inventory(self):
        """
        재고 목록을 출력하는 함수.

        기능:
            재고 목록에 있는 상품 정보들을 모두 출력한다.
        """
        line = '-' * 70
        print('\n<재고 목록>')
        print(line)
        for item in self.inventory.values():
            print(item)
        print(line)
            
    # 상품코드로 재고 목록에 상품 존재 여부 확인
    def search_item(self, code):
        """
        특정 상품을 재고 목록에서 찾는 함수.

        기능:
            인자로 받은 찾고자 하는 상품의 코드를 재고 목록 내 상품들의 코드와 비교한다.
            해당 코드를 가진 상품이 있으면 그 상품의 객체를 반환값으로 리턴한다.
            해당 코드를 가진 상품이 없으면 None을 리턴한다. 
        """
        if code in self.inventory:
            return self.inventory.get(code)
        print('상품을 찾지 못했습니다.')
        return None
    
    # 할인 이벤트 생성
    def make_discount(self):
        """
        특정 상품에 할인 이벤트를 적용하는 함수.

        기능:
            할인 이벤트를 적용하고 싶은 상품을 상품 코드로 입력받는다. 
            원하는 할인율을 입력받는다.(0~100% 가능)
            해당 상품의 원가에 할인율을 적용한 가격으로 단가를 갱신한다.
            잘못된 값을 입력할 시 0~100 사이의 정수만 입력하라는 메시지를 출력하고 재실행한다.
        """
        # 편의점 내에 상품이 없을 경우
        if self.is_empty(): 
            print('할인 이벤트를 할 수 있는 상품이 존재하지 않습니다.')
            return
        
        self.show_inventory()
        
        # 상품 찾기
        code = input('할인 이벤트를 할 상품 코드를 입력하세요(q-취소): ')
        if code == 'q':
            print('할인 이벤트를 적용하지 않습니다.')
            return None
        if not code.isdigit():
            print('상품코드를 정확히 입력해주세요.')
            return self.make_discount()
        item = self.search_item(int(code))
        if not item:
            return self.make_discount()
        
        # 할인율 적용하기
        discount = input('적용할 할인율(0% ~ 100%): ')
        try:
            int(discount)
        except ValueError:
            print('0 ~ 100 사이의 정수만 입력 가능합니다.')
            return self.make_discount()
        item.discount = int(discount)
        if item.discount < 0 or item.discount > 100:
            print('0 ~ 100 사이의 정수만 입력 가능합니다.')
            return self.make_discount()
        
        # 할인율 적용 완료
        discount_price = item.prime_cost * (1 - (item.discount * 0.01))
        item.price = int(discount_price)
        print(f"'{item.name}' 상품에 {discount}% 할인율이 적용 완료되었습니다.")
    
    # 총 수입 조회
    def show_income(self):
        """현재 총 수입을 출력하는 함수."""
        print(f'{self.store_name} 총 수입: {self.income}원', file=sys.stderr)
    
    # 고객 등록
    def register_customer(self, member):
        """
        고객 리스트에 고객 객체를 등록하는 함수.
        
        기능:
            인자로 받은 고객 코드를 고객 명단 내 고객들의 코드와 비교한다.
            동일한 코드를 가진 고객이 있으면, 고객 명단에 추가하지 않고 함수를 종료한다.
            동일한 코드를 가진 고객이 없다면, 고객 객체를 명단에 추가한다.
        """
        for customer in self.customer:
            if member.code == customer.code:
                return
        self.customer.append(member)
    
    # 고객 명단 조회
    def show_customer(self):
        """
        고객 명단을 출력하는 함수.

        기능:
            고객 명단에 존재하는 고객의 고객 코드와 고객명, 등급을 코드순으로 출력한다.
        """
        line = '-' * 25
        members = [(member.code, member.name, member.tier) \
                  for member in self.customer]
        # 고객 코드 오름차순 정렬
        code_members = sorted(members, key = lambda x : x[0]) 
        print(f'{self.store_name} <고객 명단>')
        print(line)
        print(' <코드>')
        for member in code_members:
            print(f'  {member[0]:0>4} | {member[1]} | {member[2]}')
        print(line)
        
    # 재고 부족한지 조회
    def is_stock_lack(self, code, amount):
        """
        재고가 구매하려는 물품의 수량보다 적은지 체크하는 함수.

        기능:
            구매하려는 상품의 수량보다 재고량이 적으면, 
            구매 가능한 최대 수량(재고)을 출력하고 True를 반환한다.
        """
        item = self.inventory[code]
        if amount > item.quantity:
            print(f'재고 부족! {item.name}(은/는) 최대 {item.quantity}개 구매 가능합니다.')
            return True
    
    # 판매 내역 갱신
    def update_sale_info(self, cart, tier):
        """
        고객등급별 할인율을 고려하여 특정 상품의 매출액과 매출량을 갱신하는 함수.
        """
        cart_item = cart.cart
        ratio = (100 - self.tier_rate[tier]) * 0.01
        for code in cart_item:
            item = self.inventory[code]
            item.sales += int(item.price * ratio) * cart_item[code].quantity
            item.sale_quantity += cart_item[code].quantity
    
    # 고객 현황 분석
    def show_customer_ranking(self):
        """
        누적 구매액에 따른 고객 순위를 그래프로 나타내는 함수.

        기능:
            누적 구매액에 따라 고객 정보가 내림차순으로 정렬된다.
            정렬된 순서에 따라 고객별 누적 구매액이 그래프로 표현된다.
            x축에는 고객명, y축에는 누적구매액이 표기된다.
        """
        customer_info = [(member.code, member.name, \
                          member.accum_money, member.tier) \
                         for member in self.customer]
        
        # 누적 구매액으로 내림차순 정렬
        members = sorted(customer_info, key = lambda x : -x[2])
        
        names = [f'{member[0]} {member[1]}\n({member[3]})'\
                       for member in members]
        accum_money = [member[2] for member in members]
        

        # 그래프로 표현
        plt.bar(names, accum_money, color ='palegreen', width=0.4)
        plt.xlabel("고객명", labelpad=20)
        plt.ylabel("누적 구매액", labelpad=20)
        plt.title("고객별 누적 구매액", pad=20, fontdict={'fontsize': 16})
        plt.show()
    
    
    
    #매출 현황 분석
    def show_sales_statement(self):
        """
        매출 현황을 다양한 기준(판매량, 판매액, 전체 상품 현황)으로 나타내는 함수.

        기능:
            판매량 기준을 택할 시, 판매량에 따라 상품을 오름차순 정렬하여 횡형 막대 그래프로 나타낸다.
            판매액 기준을 택할 시, 판매액에 따라 상품을 오름차순 정렬하여 횡형 막대 그래프로 나타낸다.
            전체 상품 현황을 택할 시, 전체 상품의 (상품코드, 상품명, 판매량, 판매액)를 출력한다.       
        """
        line = '-' * 60
        sales_info = [(item.code, item.name, item.sale_quantity, item.sales) \
                     for item in self.inventory.values()] #(상품코드, 상품명, 판매량, 판매액)
        y = np.arange(len(sales_info))
        
        # 정보별로 리스트 생성
        def make_list(info_list): 
            name = [f'{info[0]} {info[1]}' for info in info_list]
            sale_quantity = [info[2] for info in info_list]
            sales = [info[3] for info in info_list]
            return name, sale_quantity, sales
            
        while True:
            print(f'''
<{self.store_name} 매출 현황 분석>
----------------------------------
      1) 판매량 기준
      2) 판매액 기준
      3) 전체 상품 현황
      q) 나가기
----------------------------------''')
            option = input('입력>>> ')
            if option == 'q':
                print('매출 현황 조회를 종료합니다.')
                return
            elif option == '1':
                sale_quantity = sorted(sales_info, key = lambda x : x[2])
                names, quantities, sales = make_list(sale_quantity)
                plt.barh(y, quantities, height=0.4, color='cornflowerblue')
                plt.yticks(y, names)
                plt.title('판매량 기준 분석', pad=20, fontdict={'fontsize': 16})
                plt.xlabel('총 판매량(개)', labelpad=20)
                plt.ylabel('상품명', labelpad=20)
                plt.show()
                
            elif option == '2':
                sale = sorted(sales_info, key = lambda x : x[3])
                names, quantities, sales = make_list(sale)
                plt.barh(y, sales, height=0.4, color='lightpink')
                plt.yticks(y, names)
                plt.title('판매액 기준 분석', pad=20, fontdict={'fontsize': 16})
                plt.xlabel('총 판매액', labelpad=20)
                plt.ylabel('상품명', labelpad=20)
                plt.show()
                
            elif option == '3':
                print('<전체 상품 매출 현황>')
                print(line)
                for info in sales_info:
                    print(f'  상품코드: {info[0]} | 상품명: {info[1]} | 판매량: {info[2]} | 판매액: {info[3]}')
                print(line)
                
            else:
                print('잘못 입력하셨습니다.')
                continue

class Human(metaclass=ABCMeta):
    """
    Customer 클래스의 추상 클래스.
    """
    code = '고객 코드'
    name = '이름'
    money = '잔액'
    accum_money = '누적 구매액'
    point = '포인트'
    
    @abstractmethod
    def work(self):
        """일 해서 돈 벌기"""
        pass

    @abstractmethod
    def get_money(self):
        """현재 잔액을 출력"""
        pass
    
    @abstractmethod
    def enter_the_store(self, store):
        """편의점 이용하기 - 메뉴 출력"""
        pass

    @abstractmethod
    def purchase(self, store, cart):
        """물건 구매"""
        pass

    @abstractmethod
    def use_point(self, store, cart):
        """누적 포인트 차감하여 물건 구매"""
        pass

    @abstractmethod
    def save_point(self, new_point):
        """포인트 적립"""
        pass

    @abstractmethod
    def readjust_info(self, store, cart):
        """구매 정보를 바탕으로 편의점 상태와 고객 정보 재조정"""
        pass
    @abstractmethod
    def get_point_lottery(self, total_price):
        """이벤트 포인트 수령"""
        pass

    @abstractmethod
    def get_customer_info(self, store):
        """매장 이용 정보 조회 메뉴 제시, 실행"""
        pass

    @abstractmethod
    def generate_history(self):
        """구매 히스토리 생성"""
        pass
    
    @abstractmethod
    def show_history(self, store):
        """구매 내역 출력, 이전 구매 내역 열람"""
        pass

class Customer(Human):
    """
    사람(고객) 객체를 생성하기 위해 사용되는 클래스.
    
    속성:
        cnt: int, 사람(고객)의 고유 코드. 
        name: str, 사람 이름.
        money: int, 잔액.
        point: int, 누적(보유) 포인트.
        accum_money: int, 누적 구매액.
        purchase_list: dict, 누적 구매 내역.
        tier: str, 고객 등급

    메서드:
        create: 사용자의 입력을 받아 사람(캐릭터)가 생성된다.(클래스 메서드)
        work: 일을 해서 돈을 번다.
        get_money: 사용자의 현재 잔액을 출력한다.
        select_item: 담고자하는 상품의 코드와 수량을 입력받아, 재고가 있을 시 장바구니에 상품을 담아준다.
        enter_the_store: 메뉴에서 편의점 입장을 선택할 시 실행되는 서브메뉴를 구동한다. 
                        장바구니 생성, 담기, 삭제, 비우기, 조회 및 장바구니 내 물건 결제가 가능함.
        purchase: 편의점에서 상품을 구매한다.
        use_point: 누적된 포인트를 활용하여 상품을 구매한다. 
        is_money_lack: 사용자의 잔액으로 상품을 구매할 수 있는지 확인한다.
        calc_point: 구매 시 적립할 포인트를 계산한다. 
        save_point: 결제 시 포인트를 적립한다.
        add_purchase_item: 구매한 상품 정보를 구매 내역 리스트에 추가한다.
        add_accum_money: 결제액을 누적 구매액에 추가한다.
        show_receipt: 구매 내역 영수증을 출력한다.
        adjust_tier: 누적구매액에 따른 고객등급을 재조정한다.
        readjust_info: 구매 정보를 바탕으로 편의점 수입, 잔액, 고객 정보를 재조정한다.
        get_customer_info: 매장 이용 정보 조회 메뉴를 출력하고, 입력 받은 메뉴를 수행하기 위한 다른 함수를 호출한다.
        generate_history: 구매내역들을 최신순으로 생성한다. 
        get_history: 구매내역들을 구매처, 구매 일시, 구매 상품, 사용 포인트, 합계 금액, 고객등급 등의
                    정보를 포함하여 반환한다.
        show_history: 구매내역이 존재할 시, 내역을 최신순으로 출력해주고 이전 구매내역을 열람하게 해준다.
        get_accum_money: 사용자의 누적구매액을 반환한다.
        get_point: 사용자의 누적 포인트를 반환한다.    
    """
    
    cnt = 0 # 사람 코드
    def __init__(self, name):
        """
        사람의 고유 코드(code), 이름(name), 잔액(money), 누적 구매액(accum_money), 
        보유 포인트(point), 구매목록(purchase_list), 고객등급(tier)을 초기화하는 생성자 함수.
        
        입력:
            name: str, 고객명
        
        기능:
            객체가 새롭게 생성될 때마다 Person.cnt의 값을 1만큼 증가시킨 후 사람의 고유 코드(code)로 할당한다.
            이름을 인자로 입력받은 이름으로 초기화한다.
            잔액, 누적 구매액, 포인트를 0으로 초기화한다.
            고객등급의 초기값은 'NonMember'로 설정한다. 
            구매목록은 빈 리스트로 초기화한다.
        """
        Customer.cnt += 1
        self.code = Customer.cnt
        self.name = name
        self.money = 0       
        self.accum_money = 0
        self.point = 0
        self.purchase_list = []
        
        # new 기능 ------------------------------
        self.tier = 'NonMember'
        
    
    # 사람(캐릭터) 생성
    @classmethod
    def create(cls, name):
        """
        Customer(사람(고객)) 객체를 생성해주는 클래스 메서드.
    
        기능:
            인자로 들어온 이름으로 Customer 클래스를 호출해서 Customer 객체를 생성한다.
        """
        return cls(name)    
    
    # 일해서 돈 벌기
    def work(self):
        """
        일을 해서 돈을 버는 함수.
        
        기능:
            일해서 번 돈을 입력 받는다.
            입력받은 액수만큼 잔액을 증가시킨다.
            get_money()를 호출하여 현재 잔액 현황을 보여준다. 
        """
        earn_money = test_error(input_num)
        money = earn_money('일해서 번 돈(원)')
        self.money += money
        print(f'{money}원을 벌었습니다!')
        self.get_money()
        
    # 잔액 조회
    def get_money(self):
        """
        현재 잔액을 가독성 있게 출력하는 함수.
        """
        print()
        print(f'잔액(가용 금액): {self.money}원')
    
    # 장바구니 담을 물건 선택
    def select_item(self, store):
        """
        장바구니에 담을 상품을 고르는 함수.
        
        기능:
            장바구니에 담고자 하는 상품의 코드를 입력받는다.
            해당 상품이 재고 목록에 있는지 확인한다.
            재고목록에 있음이 확인되면, 담을 수량을 입력받는다.
            재고가 충분한지 확인한다.
            모든 조건이 충족되면 담을 상품 객체와 개수를 반환한다.
        """
        store.show_inventory()
        input_code = test_error(input_num_quit)
        code = input_code('장바구니에 담을 상품코드를 입력하세요(q-종료)', 'q')
        if code == 'q': 
            return 'q'
        item = store.search_item(code)
        
        # 재고목록에 해당 상품 없을 때
        if not item: 
            return self.select_item(store)
        input_amount = test_error(input_num_quit)
        amount = input_amount('구매할 수량을 입력하세요(q-종료)', 'q')
        if amount == 'q':
            return 'q'
        
        # 재고 부족 체크
        if store.is_stock_lack(code, amount):
            return self.select_item(store)
        
        return item, amount
    
    # 편의점 입장
    def enter_the_store(self, store):
        """
        편의점에 입장해 편의점을 이용하는 함수.

        기능:
            편의점에 입장하면 장바구니 객체를 생성한다.
            '1' 입력: 장바구니에 상품을 담기 위한 함수를 호출한다. 
            '2' 입력: 장바구니에서 특정 상품을 빼기 위한 함수를 호출한다. 
            '3' 입력: 장바구니를 비우기 위한 함수를 호출한다. 
            '4' 입력: 장바구니를 조회하기 위한 함수를 호출한다. 
            '5' 입력: 빈 장바구니, 잔액 부족 여부를 확인하고 장바구니에 담긴
                    상품을 결제하는 함수를 호출한다. 
            'q' 입력: 편의점 이용하기 메뉴를 종료한다.
        """
        
        if store.is_empty():
            print('구매할 수 있는 상품이 없습니다.')
            return
        
        # 장바구니 생성
        cart = Cart(store, self.tier) 
        while True:
            line = '-' * 30
            store.show_inventory()
            cart.show_cart()
            
            # 장바구니 이용 메뉴 선택
            print(line)
            print(
'''      1) 장바구니에 담기
      2) 장바구니에서 삭제
      3) 장바구니 비우기
      4) 장바구니 조회
      5) 결제하기
      q) 편의점 나가기''')
            print(line)
            
            menu = input('입력 >>> ')
            if menu == 'q':
                cart.clear_cart()
                print('편의점에서 나왔습니다.', file=sys.stderr)
                break
                
            elif menu == '1':
                selection = self.select_item(store)
                if selection == 'q':
                    continue
                item, amount = selection
                cart_item = CartItem(item.name, item.price, amount)
                cart.add_to_cart(item, cart_item)
                
            elif menu == '2':
                if cart.remove_from_cart() == 'q':
                    continue
                cart.remove_from_cart()
                continue
                
            elif menu == '3':
                cart.clear_cart()
                
            elif menu == '4':
                cart.show_cart()
                
            elif menu == '5':
                if cart.is_empty():
                    continue

                # 잔액 부족 체크
                if self.is_money_lack(cart.total):
                    continue
                    
                self.purchase(store, cart)
                return self.enter_the_store(store)
            
            else:
                print('메뉴를 정확히 입력해주세요')
                continue
                
    # 물건 구매
    def purchase(self, store, cart):
        """
        장바구니 내 상품을 구매하는 함수.

        기능:
            누적된 포인트를 사용하는 함수를 호출한다.
            구매 영수증을 출력한다.
            재고 수량, 포인트, 잔액 등의 정보를 재조정한다.
            상품 구매 이후의 잔액을 출력한다.
            이벤트 포인트를 랜덤으로 수령한다.
        """
        # 구매 성공
        self.use_point(store, cart)
        cart.time = datetime.now()
        print('구매가 완료되었습니다.')
        
        self.show_receipt(store, cart) # 영수증
        self.readjust_info(store, cart) # 재조정
        self.get_money() # 잔액 출력
        lottery = self.get_point_lottery(cart.total)
        print('\N{egg}', '포인트 리워드가 도착했습니다!')
        print('리워드 받기(y) / 거절하기(아무 키나 누르세요)')
        choice = input('입력>>> ')
        lottery(choice)
        
   
    # 포인트 사용
    def use_point(self, store, cart):
        """
        누적된 포인트를 활용하여 상품을 구매하는 함수.

        기능:
            사용할 포인트를 입력받는다.
            입력된 포인트만큼 결제 총액을 차감한다.
            포인트 사용 후 남은 포인트를 출력한다. 
        """
        if self.point == 0:
            return
        line = '-' * 20
        input_point = test_error(input_num_quit)
        print(line)
        print(self.get_point())
        print(line)
        point = input_point('사용할 포인트를 입력해주세요(q-사용 안 함)', 'q')
        
        if point == 'q':
            return
        if self.point < point:
            print(f'최대 {self.point}P까지 사용 가능합니다!')
            return self.use_point(store, cart)
        store.pay_point += point
        cart.using_point = point
        cart.total -= point
        self.point -= point
        print(f'{point}P 차감되어 {self.point}P 남았습니다.')
        
        
    # 잔액이 부족하지 않은지 체크
    def is_money_lack(self, total):
        """
        잔액이 구매 총액보다 부족한지 체크하는 함수.
        
        입력:
            total: int, 결제 총액
        """
        if self.money < total:
            print(f'잔액 부족! {total - self.money}원 부족합니다.')
            return True  
   
    # 포인트 계산
    @staticmethod
    def calc_point(purchase_price):
        """
        적립할 포인트를 계산하는 정적 메서드.
        
        입력:
            purchase_price: int, 구매 총액.

        기능:
            결제액에 적립 비율을 곱해 포인트를 계산한다.
            계산한 포인트를 int형으로 반환한다.
        """
        saving_ratio = 0.05
        return int(purchase_price * saving_ratio)
    
    # 포인트 적립
    def save_point(self, new_point):
        """
        포인트를 적립하는 함수.
        
        입력:
            new_point: int, 새로 적립할 포인트.

        기능:
          새로 적립할 포인트를 해당 객체의 누적 포인트에 더한다.
        """
        self.point += new_point
    
    # 구매 내역에 추가
    def add_purchase_item(self, cart):
        """
        구매 당시의 장바구니 객체를 구매 내역 리스트에 추가하는 함수.
        
        입력:
            cart: class object, 결제 시의 장바구니 객체
        """
        self.purchase_list.append(cart)
    
    # 누적 구매액 증가
    def add_accum_money(self, purchase_price):
        """
        결제 액수만큼 누적 구매액을 증가시키는 함수.

        입력:
            purchase_price: int, 결제 액수.

        기능:
            누적 구매액에 결제 액수를 더한다.
        """

        self.accum_money += purchase_price
       
    # 구매 영수증 출력
    def show_receipt(self, store, cart):
        """
        결제 내역에 대한 영수증을 출력하는 함수.

        기능:
            구매처(편의점)의 이름을 출력한다.
            구매한 고객명을 출력한다.
            구매 일시를 출력한다.
            구매 상품의 이름과 단가, 구매한 수량을 출력한다.
            결제 시 사용한 포인트를 출력한다.
            구매 총액을 출력한다.
            새로 적립할 포인트와 적립 후 누적 포인트를 출력한다.
        """
        wave_line = '~' * 50
        new_point = self.calc_point(cart.total)
        print(wave_line)
        print(f'''
    <구매 영수증>
    
    구매처: {store.store_name}
    고객명: {self.name}
    구매 일시: {cart.time.strftime('%Y-%m-%d %H:%M:%S')}

    구매 상품:''')
        for code in cart.cart:
            item = cart.cart[code]
            print(f'      {item.name} | 단가: {item.price}원 | 수량: {item.quantity}개')
        print(f'''
    사용 포인트: - {cart.using_point}P
    
    구매 총액:
      {cart.total}원({self.tier} 등급: {store.tier_rate[self.tier]}% 할인)
      
    적립 포인트:
      + {new_point}P (총 {self.point + new_point}P)
        ''')
        print(wave_line)
        
    # 구매 후 등급 조정(new)
    def adjust_tier(self, tier_criteria):
        """
        누적 구매액에 따라 고객 등급을 재조정하기 위한 함수.
        """
        if self.accum_money >= tier_criteria['Gold']:
            self.tier = 'Gold'
        elif self.accum_money >= tier_criteria['Silver']:
            self.tier = 'Silver'
        elif self.accum_money >= tier_criteria['Bronze']:
            self.tier = 'Bronze'
        else: 
            self.tier = 'Iron'
        
    
    # 구매 후 재고 수량, 포인트, 잔액 등 정보 수정
    def readjust_info(self, store, cart):
        """
        구매 정보를 바탕으로 편의점 수입, 잔액, 고객 정보를 재조정하는 함수.

        기능:
            편의점 수입을 구매액만큼 증가시킨다.
            편의점의 상품 판매 정보를 갱신한다.
            고객의 잔액을 구매액만큼 감소시킨다.
            고객의 누적 포인트를 새로운 포인트만큼 증가시킨다.
            고객의 누적 구매액을 구매액만큼 증가시킨다.
            장바구니 객체를 고객의 구매 내역 리스트에 추가시킨다.
            상품 구매 이후 누적 구매액을 기준으로 고객의 등급을 재조정한다.
            편의점의 고객 리스트에 해당 고객을 추가시킨다.
        """ 
        store.income += cart.total # 편의점 수입 증가
        store.update_sale_info(cart, self.tier)
        self.money -= cart.total # 잔액 감소
        self.save_point(self.calc_point(cart.total)) # 포인트 적립
        self.add_accum_money(cart.total) # 누적 구매액 증가
        self.add_purchase_item(cart) # 구매 내역에 추가
        # new
        self.adjust_tier(store.tier_criteria) # 구매 후 등급 재조정
        
        store.register_customer(self) # 고객 등록
    
    # 포인트 로또 이벤트
    def get_point_lottery(self, total_price):
        """
        이벤트 포인트를 수령하는 함수.
        
        입력:
            total_price: int, 결제 총액
        
        기능:
           이벤트 포인트를 생성하고 적립하는 함수를 반환한다. 
        """
        bound_set = {'Gold':0.02, 'Silver':0.015, 'Bronze':0.01, 'Iron':0}
        bound = bound_set[self.tier]
        total = total_price
        
        def make_lottery(choice):
            """
            이벤트 포인트를 생성하고 적립하는 함수.
            
            입력:
                choice: str, 이벤트 포인트 수령 여부
            
            기능:
                이벤트 포인트를 수령하고자 하면('Y' 입력),
                    고객 등급별로 이벤트 포인트 하한을 결정한다.
                    결제 총액을 기준으로 이벤트 포인트 상한을 결정한다.
                    랜덤으로 이벤트 포인트를 생성한다.
                    누적 포인트에 이벤트 포인트를 적립한다.
            """
            nonlocal bound, total
            sec = 3
            if choice == 'y':
                lower_bound = int(total * bound) + 1
                upper_bound = int(total * 0.2)
                point = random.randrange(lower_bound, upper_bound)
                while (sec != 0):
                    print(f'{sec}...')
                    sec = sec-1
                    time.sleep(1)
                print('\N{hatching chick}', f'{point}P를 받았습니다!')
                self.point += point
                print(f'{point}P가 적립되어 현재 포인트는 {self.point}P입니다.')
                return
            print('리워드를 거부하셨습니다.')
            return
        return make_lottery
            
    
    # 구매 정보 조회
    def get_customer_info(self, store):
        """
        매장 이용 정보 조회 메뉴를 출력하고,
        입력 받은 메뉴에 대한 정보를 조회하는 다른 함수를 호출하는 함수.

        기능:
            '1' 입력: 고객의 구매 내역을 출력한다.
            '2' 입력: 고객의 누적 구매액과 고객 등급을 출력한다.
            '3' 입력: 고객의 누적 포인트를 출력한다.
            'q' 입력: 매장 이용 정보 조회를 종료한다.
        """
        
        wave_line = '~' * 30
        info_menu_msg = f'''
<{self.name} 고객님 매장 이용 정보 조회>
조회할 항목의 메뉴를 입력해주세요.
--------------------------------------
      1) 구매 내역
      2) 누적 구매액 & 회원 등급
      3) 누적 포인트
      q) 나가기
--------------------------------------
입력 >>> '''
        info_menu = input(info_menu_msg)
        
        if info_menu == '1':
            self.show_history(store)
            return self.get_customer_info(store)
        elif info_menu == '2':
            info = self.get_accum_money()
        elif info_menu == '3':
            info = self.get_point()
        elif info_menu == 'q':
            print('정보 조회를 종료합니다.')
            return       
        else:
            print('없는 메뉴를 입력하셨습니다.')
            return self.get_customer_info(store)
        print(wave_line)
        print(info)
        print(wave_line)
        return self.get_customer_info(store)

    # 구매 내역 조회
    def generate_history(self):
        """
        구매 내역을 최신순으로 정렬하여 생성하는 함수.
        """
        history = reversed(self.purchase_list)
        yield from history
    
    def get_history(self, store, history):
        """
        구매내역을 서식화하여 반환하는 함수.
        """
        wave_line = '~' * 55
        form = ''
        purchase = history.cart.values()
        for item in purchase:
            form += f'{item.name} | 단가: {item.price}원 | 수량: {item.quantity}개\n\t'
        return f'''{wave_line}
        
    구매처: {history.store_info.store_name}
    구매 일시: {history.time.strftime('%Y-%m-%d %H:%M:%S')}
    
    구매 상품: 
        {form}
    사용 포인트: {history.using_point}P
    합계 금액: {history.total}원({history.tier} 등급: {store.tier_rate[history.tier]}% 할인)
    
{wave_line}      
        '''
    def show_history(self, store):
        """
        구매 일시별로 구매 내역을 출력하는 함수.
        
        기능:
            구매 내역이 존재할 시, 내역을 최신순으로 생성한다.
            구매 일시별로 구매 내역을 출력한다.
            'A'를 입력하여 이전 구매내역을 열람한다. 
        """
        if not self.purchase_list:
            print('구매내역이 존재하지 않습니다.')
            return
        history_list = self.generate_history()

        for history in history_list:
            print('구매내역을 최신순으로 조회하실 수 있습니다.')
            print('이전 구매내역을 보시려면 "A"를 입력하세요(q-종료)')
            choice = input('입력 >>> ').lower()
            if choice == 'a':
                print(self.get_history(store, history))
            elif choice == 'q':
                print('구매내역 조회를 종료합니다.')
                return
            else:
                print('잘못 입력하셨습니다.')
                continue
        else:
            print('모든 구매내역을 조회했습니다.')
            print('구매내역 조회를 종료합니다.')
            return
            

    # 누적 구매액 조회
    def get_accum_money(self):
        """
        고객의 누적 구매액과 등급을 서식에 맞추어 반환하는 함수.
        """
        output = '\n<누적 구매액 & 회원 등급>\n'
        return output + f'  누적 구매액: {self.accum_money} 원\n  회원 등급: {self.tier}\n'
    
    # 누적 포인트 조회
    def get_point(self):
        """
        고객의 누적 포인트를 서식에 맞추어 반환하는 함수.
        """
        output = '\n<누적 포인트>\n'
        return output + f'  {self.point} P\n'
        
class Cart:
    """
    장바구니 객체 생성을 위한 클래스.
    
    속성:
        cart: dict, 장바구니
        time: 구매 시간 정보
        total: int, 장바구니에 담은 상품 총액
        tier: str, 고객 등급
        using_point: int, 고객이 사용한 포인트
        store_info: class object, 편의점 객체(정보)
        
    주요 메서드:
        add_to_cart: 장바구니에 상품을 추가하는 함수.
        remove_from_cart: 장바구니에서 특정 물건을 삭제하는 함수.
        get_item_in_cart: 장바구니에 내 찾는 상품의 코드를 반환하는 함수.
        show_cart: 장바구니에 담긴 상품들을 출력하는 함수.
        show_current_total: 장바구니에 담은 상품의 총액을 출력하는 함수.
        calc_current_total: 장바구니에 담은 상품의 총액을 계산하는 함수.
        is_empty: 장바구니가 비어있는지 확인하는 함수.
        clear_cart: 장바구니를 비우는 함수.
    """
    def __init__(self, store, tier):
        """
        장바구니 객체의 초기화 메서드.

        입력:
            store: class object, 편의점 객체(정보)
            tier: str, 고객 등급
            
        초기화 내용: 
            self.cart        -- 담은 물건의 정보 저장 딕셔너리(장바구니)
            self.time        -- 구매 일시 정보
            self.total       -- 장바구니에 담은 상품 총액(0원 초기화)
            self.tier        -- 장바구니 이용 및 결제 당시 고객의 등급(입력 등급으로 초기화)
            self.using_point -- 결제 시 고객이 사용 포인트(0원 초기화)
            self.store_info  -- 구매처(편의점) 정보
        """
        self.cart = dict()
        # cart 구조: {상품코드: 객체(상품명, 단가, 구매수량)}
        self.time = None
        self.total = 0
        self.tier = tier
        self.using_point = 0
        self.store_info = store
    
    
    def add_to_cart(self, item, cart_item):
        """
        장바구니에 물건을 담는 함수.
        
        입력:
            item: class object, Product 객체
            cart_item: class object, CartItem 객체
            
        기능:
            고른 상품이 이미 장바구니에 존재하는 경우,
                CartItem 객체를 제거
                장바구니 내 상품의 수량만 증가시킨다.
            존재하지 않는 경우,
                장바구니 딕셔너리에 CartItem 객체를 추가한다.
            
            편의점 내 해당 상품의 재고량을 고른 수량만큼 감소시킨다.
            장바구니에 담은 상품의 총액을 계산한다.
        """
        amount = cart_item.quantity
        
        if item.code in self.cart:
            del cart_item
            self.cart[item.code].quantity += amount
        
        else:
            self.cart[item.code] = cart_item
        
        item.quantity -= amount
        self.calc_current_total()
        return
        
    def remove_from_cart(self):
        """
        장바구니에서 물건을 빼는 함수.
            
        기능:
            장바구니에서 제거할 상품 코드를 입력받는다.
            제거할 개수를 입력받는다.
            제거할 개수가 장바구니에 존재하는 수량과 같거나 많은 경우,
                편의점 내 해당 상품의 재고량을 장바구니에 담긴 수량만큼 증가시킨다.
                장바구니에서 해당 상품을 제거한다.
            제거할 개수가 장바구니에 존재하는 수량보다 적은 경우,
                장바구니 내 해당 상품의 수량을 제거할 개수만큼 감소시킨다.
                편의점 내 해당 상품의 재고량을 제거한 개수만큼 증가시킨다.
            장바구니에 담은 상품의 총액을 계산한다.
        """
        if not self.show_cart():
            return
        remove_code = test_error(input_num_quit)
        code = remove_code('장바구니에서 제거할 상품 코드(q-종료)', 'q')
        if code == 'q':
            return code
        code = self.get_item_in_cart(code) # 제거할 상품 코드
        if not code:
            return self.remove_from_cart()
        
        item = self.store_info.search_item(code)
        cart_item = self.cart[code]
        remove_num = test_error(input_num)
        num = remove_num('제거할 상품 개수')

        if cart_item.quantity - num <= 0:
            item.quantity += cart_item.quantity
            del self.cart[code]
            print()
            print(f'장바구니의 {item.name}(이/가) 0개가 되어 장바구니에서 상품이 삭제되었습니다.', file=sys.stderr)
        else:
            cart_item.quantity -= num
            item.quantity += num
            print(f'장바구니에서 {cart_item.name}(이/가) {num}개 빠졌습니다.')
        
        self.calc_current_total()
        return
        
    def get_item_in_cart(self, code):
        """
        장바구니에 내 찾는 상품의 코드를 반환하는 함수.
        
        입력:
            code: int, 찾는 상품의 코드
            
        기능:
            인자로 입력받은 코드를 가진 상품이 존재하면, 코드를 그대로 반환
            없으면 None 반환
        """
        if code in self.cart:
            return code
        print('장바구니에 없는 상품입니다.')
        return None
        
    def show_cart(self):
        """
        장바구니에 담은 상품을 보여주는 함수.
        """
        if self.is_empty():
            return
        line = '-'*70
        print('\n<장바구니>')
        print(line)
        for code, cart_item in self.cart.items():
            print(f'  상품코드: {code} | 상품명: {cart_item.name} | 단가: {cart_item.price}원 | 담은 수량: {cart_item.quantity}개')
        print(line)
        self.show_current_total()
        print()
        return True
        
    def show_current_total(self):
        """
        장바구니에 담은 상품의 총액을 출력하는 함수.
        
        기능:
            장바구니에 담은 상품의 총액과
            고객 회원 등급, 적용된 할인율을 동시에 출력한다.
        """
        print(f'장바구니 담은 금액: {self.total}원({self.tier} 등급 회원 {self.store_info.tier_rate[self.tier]}% 할인)')
        
    def calc_current_total(self):
        """
        장바구니에 담은 상품의 총액을 계산하는 함수.
        
        기능:
            고객 등급에 따른 할인율을 적용하여,
            장바구니에 담은 상품의 총액을 계산한다.
        """
        total = 0
        tier_discount = self.store_info.tier_rate[self.tier]
        for cart_item in self.cart.values():
            total += cart_item.price * cart_item.quantity
        total *= (100 - tier_discount) * 0.01
        self.total = int(total)
        return self.total
    
    def is_empty(self):
        """
        장바구니가 비어있는지 확인하는 함수.
        """
        if not self.cart:
            print('장바구니가 비어 있습니다.')
            return True
        return False
    
    def clear_cart(self):
        """
        장바구니를 비우는 함수.
        
        기능:
            장바구니 내 모든 상품들에 대해,
            편의점 내 상품들의 재고량을 장바구니에 담은 수량만큼 증가시킨다.
            장바구니 딕셔너리 내 요소를 모두 삭제한다.
        """
        if self.is_empty():
            return
        for code in self.cart:
            item = self.store_info.search_item(code)
            cart_item = self.cart[code]
            item.quantity += cart_item.quantity
        self.cart.clear()
        print('장바구니를 모두 비웠습니다.')
        
class Main:
    """
    프로그램 구동 객체를 만들기 위한 메인 클래스.

    속성:
        store_name: str, input으로 입력받은 편의점 이름.
        store: class object, Store 클래스 객체
        person: list, 사람(캐릭터) 목록 리스트.

    메서드:
        run_main_menu: 메인메뉴를 실행시키며 q가 입력될 때까지 계속 실행된다.
        create_person: 입력받은 이름으로 Person 클래스 객체를 생성하고, 고객명단에 객체를 추가한다.
        show_person: 사람(캐릭터) 목록에 있는 사람들을 가독성 있게 출력한다. 
        is_empty: 사람(캐릭터) 목록이 비어있는지 확인하고, 비어있으면 True를 반환한다.
        select_person: 사람(캐릭터) 목록 내에 있는 사람을 고유코드 입력을 통해 선택할 수 있게 한다.
        run_menu2: 메인메뉴에서 2를 입력할 시 수행되는 서브메뉴로서, 
                선택된 캐릭터를 통해 편의점 이용을 위한 다양한 기능을 제공한다. 
        run_menu3: 메인메뉴에서 3을 입력할 시 수행되는 서브메뉴로서, 편의점 관리를 위한 다양한 기능을 제공한다. 
    """
    def __init__(self):
        """
        편의점 이름(store_name), 사람 캐릭터 목록(person)을 초기화하고,
        Store 클래스 객체를 생성하는 생성자 함수.
        
        기능:
            편의점의 이름을 input()으로 입력받는다.
            해당 이름으로 Store 클래스 객체를 생성한다.
            사람(캐릭터) 목록은 빈 리스트로 초기화한다.
        """
        store_name = input('편의점 이름: ')
        self.store = Store(store_name)
        self.person = []

    def run_main_menu(self):
        """
        메인메뉴를 실행시키는 함수. q가 입력되기 전까지 실행됨.

        기능:
            '1' 입력: 사람(캐릭터)을 생성한다.(create_person() 호출.)
            '2' 입력: 운용할 사람(캐릭터)을 선택한다. 
                (select_person() 호출한 뒤 조건에 따라 run_menu2()를 호출.)
            '3' 입력: 편의점 관리 기능으로 들어간다.(run_menu3() 호출.)
            'q' 입력: 프로그램을 종료한다.
        """
        while True:
            menu = input('''
[메인 메뉴]
============================
    1) \U0001F4A1 캐릭터 생성
    2) \N{woman} 캐릭터 선택
    3) \N{convenience store} 편의점 관리하기
    q) \N{door} 프로그램 종료하기
============================
입력>>> ''')
            
            if menu == '1':
                self.create_person()
            elif menu == '2':
                person = self.select_person()
                if person:
                    self.run_menu2(person)
            elif menu == '3':
                self.run_menu3()
            elif menu == 'q':
                print('프로그램을 종료합니다.', file=sys.stderr)
                break
            else:
                print('잘못 선택하셨습니다.')
                
    def create_person(self):
        """
        사람(캐릭터)을 생성하는 함수.
        
        기능:
            생성할 사람(캐릭터)의 이름을 input()으로 입력받는다.
            캐릭터 목록에 이미 존재하는 사람일 경우,
                동명이인으로 생성할지 여부를 입력받는다.
                'Y'를  입력하지 않으면 생성을 취소한다.
            해당 이름으로 Person 클래스 객체를 생성한다.
            생성된 클래스 객체를 사람 캐릭터 목록(person) 리스트에 추가한다.
        """
        name = input('생성할 캐릭터 이름 입력(q-취소): ')
        if name == 'q':
            print('캐릭터 생성을 취소합니다.', file=sys.stderr)
            return
        for person in self.person:
            if person.name == name:
                print(f'\n{name}(은/는) 이미 존재하는 이름입니다.')
                print('동명이인으로 생성하시겠습니까?')
                choice = input('입력(Y/N)>>> ').lower()
                if choice == 'n':
                    print('캐릭터 생성을 취소합니다.', file=sys.stderr)
                    return
                elif not choice == 'y':
                    print('잘못 입력하셨습니다.')
                    return
                break
        person = Customer.create(name)
        self.person.append(person)
        print(f"<{name}> 캐릭터 생성에 성공했습니다!")
        
    def show_person(self):
        """
        사람 목록에 있는 사람(캐릭터)들을 출력하는 함수.
        
        기능:
            '사람 코드 | 사람 이름' 형식으로 출력한다.
        """
        line = '-' * 25
        print('캐릭터 코드를 선택하세요')
        print(line)
        print(' <코드>')
        for person in self.person:
            print(f'  {person.code:0>4} | {person.name}')
        print(line)
        
    def is_empty(self):
        """
        사람(캐릭터) 목록이 비어있는지 확인하는 함수.
        """
        if not self.person:
            print('캐릭터가 없습니다.')
            return True
        
    def select_person(self):
        """
        사람(캐릭터) 목록 내의 사람을 사람 코드로 선택하는 함수.
            
        기능:
            선택하고자 하는 사람의 코드를 입력받는다.
            사람(캐릭터) 목록에 해당 사람 코드가 있을 경우,
                해당 사람의 객체를 반환한다.
        """
        if self.is_empty():
            return None
        self.show_person()
        num = input('캐릭터 코드 선택(q-취소): ')
        if num == 'q':
            print('캐릭터 선택을 취소합니다.', file=sys.stderr)
            return None
        for person in self.person:
            if num.isdigit() and person.code == int(num):
                return person
        print('없는 캐릭터입니다.')
        return None
        
    def run_menu2(self, character):
        """
        선택된 사람(캐릭터)으로 사람(고객) 입장의 행동을 하는 함수.
        
        입력:
            character: class object, 선택된 사람(캐릭터)의 객체.
            
        기능:
            '1' 입력: 해당 사람이 돈을 번다.(Customer.work() 호출)
            '2' 입력: 편의점에서 물건을 구매한다. 
                    (Customer.purchase(self.store) 호출)
            '3' 입력: 잔액을 조회한다.(Customer.get_money() 호출)
            '4' 입력: 편의점 이용 정보를 조회한다.
                    (Customer.get_customer_info() 호출)
            'q' 입력: 사람(고객) 행동 메뉴 선택에서 메인 메뉴로 돌아간다.
        """
        while True:
            menu = input(f'''
<현재 캐릭터: {character.code:0>4} {character.name}>
=================================
    1) 돈 벌기
    2) 잔액 조회하기
    3) 편의점 이용하기
    4) 편의점 이용 정보 조회하기
    q) 메인으로 돌아가기
=================================
입력>>> ''')
            if menu == '1':
                character.work()
            elif menu == '2':
                character.get_money()
            elif menu == '3':
                character.enter_the_store(self.store)
            elif menu == '4':
                character.get_customer_info(self.store)
            elif menu == 'q':
                print('캐릭터 플레이를 종료합니다.', file=sys.stderr)
                break
            else: print('잘못 선택하셨습니다.')
            
    def run_menu3(self):
        '''
        편의점을 관리하는 함수.
            
        기능:
            '1' 입력: 편의점에 물건을 등록한다.
                    (Store.register_stock() 호출)
            '2' 입력: 특정 물건에 할인 이벤트를 생성한다.
                    (Store.make_discount() 호출)
            '3' 입력: 편의점 재고 목록을 조회한다.
                    (Store.show_inventory() 호출)
            '4' 입력: 편의점 총 수입을 조회한다.
                    (Store.show_income() 호출)
            '5' 입력: 편의점 매출 현황을 조회한다.
                    (Store.show_sales_statement() 호출)
            '6' 입력: 편의점 고객 명단을 조회한다.
                    (Store.show_customer() 호출)
            '7' 입력: 편의점 고객 현황을 조회한다.
                    (Store.show_customer_ranking() 호출)
            'q' 입력: 편의점 관리에서 메인 메뉴로 돌아간다.
        '''
        while True:
            menu = input('''
<편의점 관리하기>
====================================================================
    1) 물건 등록         2) 할인 이벤트 생성     3) 재고 목록 조회
    
    4) 수입 조회         5) 매출 현황 분석
    
    6) 고객 명단 조회     7) 고객 현황 분석
    
    q) 메인으로 돌아가기
====================================================================
입력>>> ''')
            if menu == '1':
                self.store.register_stock()
            elif menu == '2':
                self.store.make_discount()
            elif menu == '3':
                self.store.show_inventory()
            elif menu == '4':
                self.store.show_income()
            elif menu == '5':
                self.store.show_sales_statement()
            elif menu == '6':
                self.store.show_customer()
            elif menu == '7':
                self.store.show_customer_ranking()
            elif menu == 'q':
                print('편의점 관리를 종료합니다.', file=sys.stderr)
                break
            else: print('잘못 선택하셨습니다.')
            
def main():
    '''
    프로그램을 실행하는 메인 함수.
    
    기능:
        Main 클래스의 객체를 생성하고, 메인 메뉴 메서드를 실행한다.
    '''
    execution = Main()
    execution.run_main_menu()
    
main()
