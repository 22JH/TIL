# Redux

- 상태에 어떠한 변화가 있으려면 ***액션(action)***  있어야함

- 액션은 객채로 표현됨

- ex) 
  
  ```javascript
  {
      type: 'TOGGLE_VALUE'
  }
  ```
  
  - 액션 객체는 `type` 필드가 필수
  
  - 이 값이 액션의 이름이라 생각하면됨
  
  - 이 외의 값은 상태를 업데이트 할 때 참고할 것이며 마음대로 작성 가능
  
  ```javascript
  {
      type: 'ADD_TODO',
      data: {
          id: 1,
          text: '리덕스 배우기'
      }
  }
  ```

- 액션 생성 함수
  
  - ```javascript
    function addTodo(data) {
        return {
        type: 'ADD_TODO',
        data
        }
    }
    
    const changeInput = text =({
        type: 'CHANGE_INPUT',
        text
    })
    ```
  
  - 액션 객체를 만드는 함수
  
  - 매번 액션 객체를 작성하면 비효율, 실수 할 수도 있어서 함수로 관리



- Redux 규칙
  
  - 단일 스토어
    
    - 하나의 어플리케이션 안에는 하나의 스토어
  
  - 읽기 전용 상태
    
    - 리덕스의 상태는 읽기전용
    
    - 불면성을 지키기 위해 spread(...) 등을 사용
    
    - 왜냐하면 내부적으로 데이터가 변경되는 것을 감지하기 위해 얕은 비교 검사를 하기 때문
    
    - 얕게 검사해서 좋은 성능을 유지
  
  - 변화를 일으키는 `reducer` 함수는 순수한 함수
    
    - 순수한 함수란?
      
      - 이전 상태와 액션 객체를 파라미터로 받는다
      
      - 파라미터 외의 값에는 의존하면 안된다.
      
      - 이전상태는 절대 건드리면 안되고 변화를 준 새로운 상태 객체를 ***만들어서*** 반환
      
      - 똑같은 파라미터로 호출된 리듀서 함수는 언제나 똑같은 결과를 반환해야함
