# Hooks

- 함수형 컴포넌트에서 상태관리



- `useState`

- `useEffect`
  
  - 리렌더링 될때마다 특정 작업을 수행
  
  - `componentDidMount` + `componentDidUpdate`
  
  - `useEffect(() => { console.log('렌더링'} )` 시 매번 실행
  
  - `useEffect(() => { console.log('렌더링'}, [])` 시 한 번만 실행
  
  - `useEffect(() => { console.log('렌더링'}, [감시할 것])` 시 대상이 변경될 때 실행
  
  - `return() => {cleanup함수}` return값으로 업데이트되기 직전에 작업 수행 가능

- `useReducer`
  
  - 현재 상태, 업데이트를 위해 필요한 정보를 담은 액션 값을 전달받아 새로운 상태를 반환하는 Hook
  
  - 새로운 상태를 만들 때 반드시 불변성 유지 필요
  
  - ```javascript
    function reducer(state, action) {
        return nextState
    // 새로운 상태를 만드는 로직
    }
    
    
    const [state, dispatch] = useReducer(reducer, initialState)
    // state는 컴포넌트에서 사용할 수 있는 상태를 가리캄
    // dispatch는 액션을 발생시키는 함수
    ```

- `useMemo`
  
  - vue에서 computed랑 비슷한듯
  
  - 렌더링 과정에서 특정 값이 바뀌엇을때만 연산하고 원하는 값이 바뀌지 않으면 이전에 연산했던 결과를 다시 사용하는 방식
  
  - `const value = useMemo(() => { return calculate() }, [item]`
    
    - 첫번째 인자 콜백함수
    
    - 두번 째 인자 의존성 배열
  
  - 꼭 필요할 때만 사용

- `useCallback`
  
  - 최적화 할 때 사용
  
  - useMemo랑 비슷
    
    - useMemo는 메모이제이션 된 값을 반환
    
    - useCallback은 메모이제이션 된 함수를 반환
  
  - 부모 컴포넌트만 렌더링 하고 싶을 때
  
  - 외부에서 값을 가져오는 api를 호출하는 경우

- `useRef`
  
  - 함수형컴포넌트에서 ref를 쉽게 사용할 수 있도록 해줌
  
  - ```javascript
    const inputEl = useRef(null)
    ...
    <input name="name" onChange={onChange} value={text} ref={inputEl}/>
    ```
  
  - 로컬 변수 관리 가능
    
    - ```javascript
      const id = useRef(1)
      const setId = (n) => {
          id.current = n
      }
      ```
    
    - 렌더링이 일어나지 않음
