## class형 컴포넌트, 함수형 컴포넌트

- state와 render, liferecycle의 차이

- react-hook으로 어느정도 커버됨

```javascript
import React, { Component } from 'react'

class Counter extends Component {
    constructor(props) {.  // 컴포넌트 생성자 함수
        super(props)    // 필수 호츌, 현재 클래스형 컴포넌트가 상속하고 있는 
                        //리액트의 Component클래스가 지닌 생성자 함수를 호출   
        this.state = {
            number : 0 // 초기값 설정
        }
    }
}
render() {
    const { number } = this.state
    return (
        <div>
            <h1>{number}</h1>
            <button onClick={() => {
                this.setState({ number: number + 1})
            }
            </button>
        </div>
    )
}
```

- `constructor` 안쓰고 state 지정하기

```javascript
import React, { Component } from 'react'

class Counter extends Component {
    state = {
        number: 0,
        fixedNumber: 0
    }
}
render() {
    const { number, fixedNumber } = this.state
    return (
        <div>
            <h1>{number}</h1>
            <button onClick={() => {
                this.setState({ number: number + 1})
            }
            </button>
        </div>
    )
}
```

- 이전 값 받기

```javascript
onclick={() => {
    this.setState(prevState => {
        return {
            number: prevState.number + 1
    })
    this.setState(prevState => {
        number: prevState.number + 1
    }) // 위의 코드와 같음
}
```

- 함수형 컴포넌트에서 useState 여러개 쓰기

```javascript
import React, { useState } from 'react'

const EventPractice = () => {
    const [form, setFrom] = useState({
        username: '',
        message: ''
    })
    const { username, message } = form
    const onChange = e => {
        const nextForm = {
            ...form, //기존의 form 복사
            [e.target.name]: e.target.value
        }
    }
    const onClick = () => {
        aler(username + ': ' + message)
        setForm({
            username: '',
            message: '',
        })
    }
}
```
