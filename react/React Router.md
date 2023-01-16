# React Router

- 사용법
  
  ```javascript
  import {
    BrowserRouter as Router,
    Routes,
    Route
  } from 'react-router-dom'
  function App() {
    return <Router>
      <Routes>
        <Route path="/" element={ <Home /> } />
        <Route path="movie" element= { <Detail /> } />
      </Routes>
    </Router>
  }
  ```
  
  - Routes
    
    - 이전버전까지 'Switch'
    
    - Route 는  Url을 의미
    
    - 찾으면 컴포넌트 렌더링
    
    - `<Route path="url이름" element={ <컴포넌트/> } />`
  
  - Link
    
    - view의 router Link 

- 다이나믹 라우팅
  
  - `<Route path="/movie/:id"`
  
  - vue 와 똑같음
  
  - `import { useParams } from "react-router-dom`
  
  - userParams 로 사용
  
  - const x = useParamas()

- props
  
  - ```javascript
     return (
          <div>
            <h1>The movies!</h1>
            {loading ? <strong>Loading...</strong> : 
            movies.map((movie) => (
              <Movie coverImg={movie.medium_cover_image}
                key={movie.id}
                id={movie.id}
                title={movie.title}
                summary={movie.summary}
                genres={movie.genres}
              />
              ))}
          </div>
        )
    ```
  
  - ```javascript
    <컴포넌트이름
        prop할 변수 이름 = {prop할 데이터}
    ```
