## 컴포넌트 반복 (map), 라이프사이클(life-cycle)

- 반복할 때는 map함수 사용

- 반드시 key값 넣어줘야함

- ```javascript
  const Inter = () => {
      const names = ['눈사람', '사람', '눈']
      const namesList = names.map((name, idx) => <li key={idx}>{name}</li>)
      return <ul>{nameList}</ul>
  
  ```

---

- 메서드(접두사)
  
  - Will : 작업(동작) 전
  
  - Did : 작업(동작) 후
  
  - 사이클 
    
    - Mount : Dom이 생성되고 브라우저에 나타나는 것
      
      - `constructor` : 컴포넌트를 새로 만들 때마다 호출되는 클래스 생성자 메서드
      
      - `getDerivedStateFromProps` :  props에 있는 값을 state에 넣을 때 사용하는 메서드
      
      - `render` : 우리가 준비한 UI를 렌더링하는 메서드
      
      - `componentDidMount` : 컴포넌트가 웹브라우저상에 나타난 후 호출하는 메서드
    
    
    
    - Update : [props가 바뀔 때] , [state가 바뀔 때], [부모 컴포넌트가 리렌더링될 때], [`this.forceUpdate`로 강제로 리렌더링을 트리거 할 때]
      
      - `getDerivedStateFromprops` : 업데이트때도 호출 됨
      
      - `shouldComponentUpdate` : 컴포넌트가 리렌더링을 해야할지 말아야할지를 결정하며 `true`, `false`를 반환해야함
      
      - `render` : 컴포넌트를 리렌더링
      
      - `getSnapshotBeforeUpdate` : 컴포넌트 변화를 DOM에 반영하기 직전에 호출
      
      - `componentDidUpdate` : 작업 후 호출
    
    - Unmount : DOM에서 제거
      
      - `componentWillUnmount` : 컴포넌트가 사라지기 직전에 호출하는 메서드



- `render()`
  
  - 가장 중요한 메서드
  
  - `this.props`와`this.state`에 접근가능
  
  - 아무것도 보여주고 싶지 않으면 null, false
  
  - 이 메서드 안에서 `setState`사용 금지
  
  - DOM에 접근 금지 (가져오는것도 안됨)
  
  - 위의 두 가지는 `componentDidMount`에서 해야함

- `constructor(props) {...}`
  
  - 초기 state를 설정할 수 있음

- `getDerivedStateFromProps`
  
  - ```javascript
    static getDerivedStateFromProps(nextProps, prevState) {
        if(nextProps. value !== prevState.value) {
            return { value: nextProps.value}
        }
        return null // state를 변경할 필요 없으면 Null 반환
    
    }
    ```
  
  - props를 state에 동기화 할 때 사용

- `componentDidMount() {...}`
  
  - 컴포넌트를 만들고 첫 렌더링을 마친 후 실행
  
  - 다른 자바스크립트 라이브러리, 프레임워크의 함수호출
  
  - 이벤트 등록, setTimeout, setInterval, 네트워크 요청같은 `비동기 작업` 

- `shouldComponentUpdate(nextProps, nextState) {...}`
  
  - props, state 변경시 리렌더링 여부 결정
  
  - 따로 생성하지 않을 시 항상 true
  
  - 현재 props와 state는 `this.props, this.state`로 접근
  
  - 성능 최적화할 때 false 쓸지 결정

- `getSnapshotBeforUpdate`
  
  - 업데이트 직전에 참고할 일 있을 때 활용 ex) 스크롤바 위치 유지 등
  
  - ```javascript
    getSnapshotBeforUpdate(prevProps, prevState) {
        if(prevState.array !== this.state.array) {
            const { scrollTop, scrollHeight } = this.list
            return { scrollTop, scrollHeight }
        }
    }
    ```

- `componentDidUpdate(prevProp, prevState, snapshot) {...}`
  
  - 이 때부터 DOM 관련 처리 해도됨
  
  - prevProps, prevState로 이전에 가졌던 데이터에 접근 가능
  
  - `getSnapshotBeforeUpdate`에서 반환 값이 있으면 여기서 `snapshot`값 전달받을 수 있음

- `componentWillUnmount() {...}`
  
  - `componentDidMount`에서 등록한 이벤트, 타이버, 직접 생성한 DOM 제거 해야함

- `componentDidCatch`
  
  - 컴포넌트 렌더링 도중에 에러시 오류 UI를 보여줌
  
  - ```javascript
    componentDidCatch(error, info) {
        this.setState({
            error: true
        })
        console.log ({ error, info })
    }
    ```
  
  - 여기선 자신의 컴포넌트가 아니라 prop, children으로 전달되는 컴포넌트에서 발생하는 에러만 잡을 수 있음

- 
