import math
import random

def get_1_or_0() -> int:
    return int(round(random.random(), 0))

def get_random_element(_list: list) -> int or str:
    '''get_1_or_0()을 활용한 리스트 원소 랜덤 추출 함수'''
    
    if len(_list) <= 1:
        raise ValueError("빈 리스트 혹은 원소 개수가 한개입니다.")
    
    _list_ = []
    while len(_list_) != 1:
        for elm in _list:
            if get_1_or_0() == 1:
                _list_.append(elm)
                
        if len(_list_) > 1:
            _list = _list_
            _list_ = []
    
    return _list_[0]

def get_random(n: int) -> int:
    """
    Linear congruential generator
        Recurrence Relation: Xn+1 = (a * Xn + c) % m
        c: increment, a: multiplier, m: modulus
        
        ** 주기가 최대가 되기위한 계수 조건 ** 
            - c와 n은 서로소 (0<= c < n) 
            - m이 4의 배수이면 a-1도 4의 배수
            - a-1은 m의 모든 소인수*로 나누어 떨어짐
                * 연산 시간 문제와 계수 예측을 막기 위해 랜덤한 소인수로 나누어 떨어지도록 설정함
    """
    

    # 점화식 연산 횟수가 10 ** 7 초과 되는것을 방지
    max_len = 8

    # b = a - 1
    # 4의 배수 조건 체크
    n += 1
    m = n
    if n % 4 == 0:
        b = 4
        n = n // 4
    else:
        b = 1

    flag = True
    factors = []
    c, factor = 1, 2
    while factor**2 <= n:
        if flag:
            # 서로소 판별: c값 설정
            if math.gcd(n, factor) == 1:
                # get random 1 or 0
                if get_1_or_0() == 1:
                    c *= factor
                    if c >= n:
                        flag = False
                        c //= factor
        
        # 소인수 분해: b값 설정
        while n % factor == 0:
            factors.append(factor)
            n = n // factor
            # get random 1 or 0
            if get_1_or_0() == 1:
                b *= factor
                # 계수 크기 조정
                while b >= n or len(str(b)) >= max_len:
                    _factor = get_random_element(factors)
                    b //= _factor    
            
        factor += 1
        
    if n > 1:
        factors.append(n)
        # get random 1 or 0
        if get_1_or_0() == 1:
            b *= factor
            # 계수 크기 조정
            while b >= n or len(str(b)) >= max_len:
                _factor = get_random_element(factors)
                b //= _factor
        
    a = b + 1
    x = get_1_or_0() # seed 

    i = 0
    while i < a:
        x = (a * x + c) % m
        i += 1
        
    return x