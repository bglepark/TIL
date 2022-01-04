# 모듈 참조

# 1) 모듈의 전체 참조
# import 모듈명
import random

# import 모듈명 as 줄임말
# 모듈명이 길거나 모듈명이 동일한 경우 별칭으로 사용

import pandas as pd

# 모듈 내 함수를 참조
# import 모듈
# 모듈.함수명

import random
random.randint(3,10)


# 2) 모듈 내에서 일부만 참조
# 형식 1. from 모듈명 import 변수명 or 함수명
from random import randint , randrange

# 형식 2. from 모듈명 import *
     # 모듈 내에서 __로 시작하는 스페셜변수나 매직메소드 를 제외한 모든 것을 참조한다 (* 표시)

# 형식 3. from 모듈명 import 변수명 or 함수명 as 별칭
# from random import randint , randrange as rnd

