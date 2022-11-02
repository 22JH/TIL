## 11/2 Vue.js : Vue CLI

- Node.js
  
  - 자바스크립트는 *브라우저 밖에서는 구동할 수 없었음*
  
  - 런타임 환경인 Node.js로 인해서 서버에서도 사용할 수 있게 됨
  
  - 자바스크립트 패키지 관리자
    
    - python - pip
    
    - node.js - npm (node.js를 설치했다면 이미 설치 돼있음)

- Vue CLI
  
  - Vue 개발을 위한 표준 도구
  
  - 프로젝트의 구성을 도와주는 역할
  
  - 확장 플러그인, GUI 등 다양한 tool 제공\
  
  - 설치
    
    - `npm install -g @vue/cli`
    
    - `vue create vue-cli` - vscode 터미널에서 진행 (프로젝트 생성)
  
  - 구조
    
    - node_modules
      
      - 파이썬에서의 가상환경과 같은 역할
    
    - babel
      
      - es6+ 코드를 구버전으로 번역/변환 해주는 도구 - 컴파일러
  
  - module 의존성 문제
    
    - 모듈 수가 너무 많아짐. 문제 파악 힘듦
    
    - `bundler`이 해결해줌, 여기선 `webpack`
    
    - bundler
      
      - 모듈들을 하나로 묶어주고 묶인 파일은 하나 혹은 여러개로 만들어짐
      
      - 이 모든 것은 Vue CLI가 알아서 초기 셋팅 해놓음

- package.json

- package-lock.json
  
  - 파이썬의 requirements.txt 의 역할

- Component
  
  - 유지 보수를 위한 구조
  
  - 트리 형태
  
  - 재사용성
  
  - 확장가능



- public
  
  - favicon - 첫 아이콘
  
  - index
    
    - vue 앱의 뼈대가 되는 html 파일
  
  

- SFC
  
  - vue에서 말하는 component란
    
    - 이름이 있는 재사용 가능한 Vue instance
    
    - `const app = new Vue()`
    
    - 1. component 폴더에 파일 만들기
      
      2. script에 이름 등록
      
      3. template에 요소 추가 (하나의 요소만 추가 가능,  비어있어도 안됨)
    
    - component 등록 3단계
      
      - 1. 불러오기
           
           - import {instance name} from {위치}
           
           - `import MyComponent from './components/MyComponent.Vue`
           
           - `import MyComponent from '@/components/MyComponent`
        
        2. 등록하기
        
        3. 보여주기


