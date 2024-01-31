### 수정 전
```python
# 할인 이벤트 생성
    def make_discount(self):
      #...
        # 할인율 적용하기
        discount = input('적용할 할인율(0% ~ 100%): ')
        try:
            int(discount)
        except ValueError:
            print('0 ~ 100 사이의 정수만 입력 가능합니다.')
            return self.make_discount()
        if int(discount) < 0 or int(discount) > 100:            # 여기부터
            print('0 ~ 100 사이의 정수만 입력 가능합니다.')
            return self.make_discount()
        item.discount = discount                                # 여기까지
        
        # 할인율 적용 완료
        discount_price = item.prime_cost * (1 - (item.discount * 0.01))
        item.price = int(discount_price)
        print(f"'{item.name}' 상품에 {discount}% 할인율이 적용 완료되었습니다.")

```
```python
# 할인 이벤트 생성
    def make_discount(self):
      #...
        # 할인율 적용하기
        discount = input('적용할 할인율(0% ~ 100%): ')
        try:
            int(discount)
        except ValueError:
            print('0 ~ 100 사이의 정수만 입력 가능합니다.')
            return self.make_discount()
        if int(discount) < 0 or int(discount) > 100:            # 여기부터
            print('0 ~ 100 사이의 정수만 입력 가능합니다.')
            return self.make_discount()
        item.discount = discount                                # 여기까지
        
        # 할인율 적용 완료
        discount_price = item.prime_cost * (1 - (item.discount * 0.01))
        item.price = int(discount_price)
        print(f"'{item.name}' 상품에 {discount}% 할인율이 적용 완료되었습니다.")

```
<details>
<summary>수정 전</summary>
<div markdown="1">
```python
    item.discount = int(discount)
    if item.discount < 0 or item.discount > 100:           
          print('0 ~ 100 사이의 정수만 입력 가능합니다.')
          return self.make_discount()
```

</div>
</details>

<details>
  <summary>코드 보기</summary>

  ```python
  def hello_world():
      print("Hello, World!")
</details>
```

### 문제사항
- item.discount = discount가 0~100 사이 정수 판단하는 조건문 **전**에 있어서 100 이상의 정수가 입력됐을 때 그대로 할인율로 적용되는 문제가 있었음.

### 해결방법
- item.discount = discount를 if 조건문 뒤로 옮기고, if 조건문의 변수를 int(discount)로 변경하였음.
- 만약 if 조건문의 변수가 int(discount)가 아니라 discount라면, 음의 정수(예를 들어 -10)가 입력됐을 때 문자열과 정수를 비교하는 오류가 발생하므로 int(discount)로 해주었음. 
