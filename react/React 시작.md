# React 시작

- 시작하기
  
  - `npx create-react-app 프로젝트`
  
  - `npm i react-router-dom`

- 리액트의 동작구조
  
  - Vue와 비슷하나 render 방식이 다름
  
  - 값이 바뀌면 render
  
  - 조건 render =>  `useEffect(함수,[지켜볼 대상])`
  
  - userState로 data 관리
    
    - `const [data이름, data변경 함수] = useState(초기값)`

- css
  
  - inline
    
    - ex: `<h1 style={ { color : ~~~, borderRight: ~~~, marginBottom: ~~~} }`
      
      - 반드시 객체로 작성
      
      - 카멜케이스로 작성
      
      - 세미콜론 X
  
  - 각 컴포넌트마다 적용
    
    - `컴포넌트명.module.css` 파일 생성
    
    - 컴포넌트에 `import styles from "위치"`
    
    - ex: `<h1 className={styles.box}/>`

- axios
  
  - async awit 사용
    
    - ```javascript
      try {
          const data = await axios.get("url")
      } catch {
          오류
      }
      ```
  
  ![](C:\Users\q\AppData\Roaming\marktext\images\2022-12-10-02-35-35-image.png)

- event
  
  - `on"이벤트명''={() => {함수}}`
