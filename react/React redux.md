# React redux

- 시작
  
  - `npm i redux react-redux`
  
  - `import { createStore } from 'redux'`

- 사용
  
  - ```javascript
    function reducer(currentState, action) {
        // 첫번째 현재 스테이트 값, 두번째 어떻게 바꿀 것인가
        // redux 각각의 스테이트의 변화를 불변하게 유지해야함
        const newState = {...currentState} 
        return newState; // 복제후 반환
    
        if (currentState === undefined){ //state값이 정의 되지 않았으면
            return {
                number:1 //예제
            }
        }
    const store = createStore(reducer)
    ```
    
    ```
    
    ```

- `import { Provider, useSelector, useDispatch, connect} from 'react-redux`
  
  - provider : 어떤 컴포넌트에게 제공할지
    
    - ```javascript
      <Provider stoer={store}
          <컴포넌트>
      </Provider>
      ```
  
  - useSelector: 어떤 state값을 쓸지 선택, 함수를 인자로 받음
    
    - ```javascript
      function Left3() {
          const number = useSelector((state) => state.number)
      }
      ```
  
  - useDispatch: state값을 변경 시킬 때
    
    - ```javascript
      const dispatch = useDispatch()
      
       dispatch({ type: 'PLUS' }) // plus라는 액션을 전달, reduce를 호출
      ```
      
      ```
      
      ```
