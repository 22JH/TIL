# Ref 사용하기

- DOM을 직접 조작해야할 때
  
  - id를 달아도 되지만 유니크 값인 id를 직접 사용하는 것은 권장하지 않음
  
  - 특정 input에 포커스 주기
  
  - 스크롤 박스 조작하기
  
  - canvas 사용하기

- 사용법
  
  - 콜백 함수를 통해 설정
    
    - `<input ref={(ref) => {this.input=ref} />`
    
    - this.input 은 input요소의 DOM을 가리킴
  
  - `createRef`
    
    - ```javascript
      import React, { Compoenet }, from 'react'
      
      
      class RefSample extends Compoenet {
          input = React.createRef()
          
          handleFocus = () => {
              this.input.current.focus()
          }
      
          render() {
              return (
                  <div>
                      <input ref={this.input} />
                  </div>
              )
          }
      }
      ```


