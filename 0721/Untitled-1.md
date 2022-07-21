## 가변 키워드 인자 (**kwargs)

- 두 개의 값을 동시에 필요

- 딕셔너리로 만들어짐

- 매개변수에다 값을 넣는 형식

## 가변 인자 리스트 (*kwargs)

- 정해지지 않은 개수의 인자

## 재귀 스택 제한 풀기

```python
import sys  
sys.setrecursionlimit(1234)
#print(sys.getrecursionlimit())
```

## zip

- 최소 수 만큼 짝을 맞춰준다

## lambda 함수

- 익명함수, 이름이 없음

- 표현식의 값만 리턴

- 값을 표현 하는 식

- ```python
  lambda a. b: a - b if a> b else b - a
  ```
  
  def func(a, b):
  
      return a - b if a> b else b - a

```
## 모듈(module)과 패키지(package)

- 패키지는 모듈의 모음

- from 폴더명.폴더(디렉토리).파일 import 파일 내 데이터

- 끝에 'as' 를 붙여 별명 설정 가능
```
