#!/usr/bin/env python
# coding: utf-8

# # How to Use

# In[1]:


#b
# run: shift + enter
45


# markdown space
# 
# # Heading 1
# ## Heading 2
# ### Heading 3

# - markdown: blue(left) + m
# - item 1
# - item 2

# In[ ]:


delete: (block) + D, D


# In[4]:


print(45) #주석처리


# # Week 01

# ## 프로그래밍 정의
#    - 프로그래밍 언어를 사용하여 프로그램을 개발하는 것
# 
# ## 프로그래밍 의의
#    - 논리적 사고 학습 가능
#    
# ## Programming Language
#    - 프로그램 개발 시 사용하는 도구
#    - 인간이 원하는 것을 컴퓨터에게 명령 시, 사용하는 컴퓨터가 이해할 수 있는 언어
# 
# ## 파이썬?
#    - 쉽고 간결
#    - 다양한 라이브러리

# ## Chapter 02. Data: Types, Values, Variables, and Names

# In[2]:


a=2
a


# In[3]:


a==2


# - 변수(variable) : 특정 값 저장하는 공간
#     a
# - 값(value)
#     2
# - 할당하다(assign): 변수에 값을 넣는 과정
#     "2를 a에 넣었다."
#     cf. a는 2다. => a == 2
#     
# - 자료형(type): 데이터의 형태
#     a 데이터의 형태? integer (int 타입)

#   *변수 사용 이유: 값 변경 필요 시, 간단하게 변경할 수 있음.

# In[4]:


print(a)


# In[6]:


a


# In[5]:


#type
type(a)


# In[7]:


type(2)


# In[8]:


type(a==2)  #bool, boolean T/F


# ### Type
# - integer|정수 : 1, 2, 3, ...
# - floating point number|부동소수점: 1.0, 2.0, ...
# - string|문자열: "1", 'apple'  **따옴표로 감싸면 string type
# - boolean|불리언: True/False (bool)

# In[10]:


type("1")


# In[11]:


type('apple')


# In[12]:


type(apple)  #변수명으로 인식됨


# In[13]:


name = 'Yeo'
name


# In[14]:


print(name)


# In[15]:


print('Yeo')  #지양


# ### 할당
# - = 기호 사용
# - 수학에서는 '양변이 같다'라는 의미로 사용되지만, 프로그래밍에서는 '할당하다'라는 의미가 추가된다.
# - "오른쪽의 값을 왼쪽에 할당한다"
# - 1. 오른쪽에 있는 모든 것은 값을 가져야 한다.(초기화해야 한다.)
# - 2. 같은 변수에 다른 값을 넣을 수 있다.

# In[21]:


x = 4      #초기화: 값을 처음 정해주는 것
y = x + 3  #대입연산자 오른쪽의 값은 정해져 있어야 함


# In[22]:


x, y


# In[23]:


name = 'kim'
name = 'lee'
name = 'park'
name = 4   #최종 정해지는 값은 마지막에 선언한 값


# delete: (block) + D, D

# In[24]:


print(name)  #변수명 동일하게 사용하지 말 것


# In[ ]:


text = 'abc'
text = 'cde'


# ### 변수명 정하기
# - 나쁜 변수명: a, b, c, a1, b1, ... 
# - 남이 이해할 수 있는 의미있는 이름으로 선언해야 함.
# - 소문자, 대문자, 언더바 사용 
#   e.g. name, name2, my_name, Name, NAME

# In[26]:


name = 'juliette'
name1 = 'jessica'
my_name = 'laura'
# myName : camel case

print(name, name1, my_name, sep=',')


# - 안 되는 것
#    - 숫자로 시작 불가능
#     e.g. 22name, 22_name
#    - 예약어(문법에서 사용하는 이름)로 선언 불가능
#     e.g. def, False, ...

# In[29]:


#if = 'kim'
help("keywords")   #변수 이름으로 사용 불가능


# - 조심할 것 : 특별한 용도가 있기 때문
#   - 언더바로 시작하는 변수명: _name #클래스 내부 변수 지칭
#   - 더블 언더바로 시작하는 변수명: __name__
#   - 대문자로 시작하는 변수명: Name
#   - 전체 대문자: NAME

# In[30]:


#변수명은 대소문자 구분됨
num = 43
Num = 44


# In[31]:


num==Num


# In[32]:


num = 'number'
Nume = 'Number'

num == Num


# In[33]:


num != Num  #'다르다'

