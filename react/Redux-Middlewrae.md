# MiddleWare

- 두가지 방식이 있음
  
  - 일반적으로 `actions`, `constants`, `reducers` 세 폴더로 나누어서 관리
    
    - 공식 문서에서 사용되는 기본적인 방법
  
  - Ducks패턴
    
    - `modules` 폴더에 모아서 관리



- 모듈 작성
  
  - 문자열로 액션타입 정의
  
  - `const INCREASE = 'counter/INCREASE`
  
  - '모듈 이름/액션 이름' => 겹치는 것을 방지하기위해

- 액션 생성 함수만들기
  
  - ```javascript
    const INCREASE = 'counter/INCREASE'
    const DECREASE = 'counter/DECREASE'
    
    export const increase = () => ({ type: INCREASE })
    export const decrease = () => ({ type: DECREASE })
    ```


