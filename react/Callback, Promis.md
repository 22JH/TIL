# Callback, Promis

```javascript
function increase(number, callback) {
    setTimeout(() => {
        const result = number + 10
        if (callback) {
            callback(result)
        }
    }, 1000)
}

increase(0, result => {
    console.log(result)
)
```

- callback 예시

- 콜백 지옥 벗어나기 (Promise)

- ```javascript
    function increase(number) {
      const promise = new Promise((resolve, reject) => {
        setTimeout(() => {
          const result = number + 10
          if (result > 50) {
            const e = new Error('numberToobig')
            return reject(e)
          }
          resolve(result)
        }, 1000)
      })
      return promise
    }
  
    increase(0)
    .then(number =>{
      console.log(number)
      return increase(number)
    })
    .then(number =>{
      console.log(number)
      return increase(number)
    })
    .then(number =>{
      console.log(number)
      return increase(number)
    })
    .then(number =>{
      console.log(number)
      return increase(number)
    })
    .then(number =>{
      console.log(number)
      return increase(number)
    })
    .catch(e => {
      console.log(e)
    })
  ```

- `.then`을 사용함으로써 콜백 지옥 벗어나기
  
  - `return increase(number)` 을 통해 promise를 리턴해야 계속해서 .then 사용가능

- async/await
  
  - ```javascript
      async function runTasks() {
        try {
          let result = await increase(0)
          console.log(result)
          result = await increase(result)
          console.log(result)
          result = await increase(result)
          console.log(result)
          result = await increase(result)
          console.log(result)
          result = await increase(result)
          console.log(result)
        } catch(e) {
          console.log(e)
        }
      }
    ```
  
  - try , catch 로 에러 처리
