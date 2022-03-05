## 인문사회학회 웹페이지


### 웹 프로그램 개발 목적  
한 학기에 약 100편 정도의 글이 이 학회에서 만들어지고 있다. 다양한 인문사회학적 주제에 대한 여러 생각이 담긴 소중한 글이다. 기존에는 구글 드라이브로 글을 공유했었다. 하지만 이런 방식은 글을 체계적으로 관리하는데 좋지 않았다. 따라서 웹 프로그램을 활용하여 글을 보다 체계적으로 관리 및 공유 더 나아가 활용할 수 있도록 하려고 한다. 이에 더해, 학회 활동의 범위를 오프라인에서 온라인으로 확장함으로써 코로나 시대 비대면 활동의 한계를 해결하고 학회활동을 더더욱 다채롭게 하려고 한다. 

---

### 웹 프로그램 구조  
<figure  style="text-align: center;">

![web_structure](https://raw.githubusercontent.com/habibi03336/Hannuri/master/asset/web_structure.png?raw=true)

1. React를 활용하고, 트랜드에 맞는 개발 경험을 쌓기 위해서 프론트엔드와 백앤드를 구분하여 개발하였다. 서버 쪽에서는 Django REST Framework, 프론트 쪽에서는 React를 중심으로 개발하였다.

2. 회원정보 관리를 쉽게 하기 위해 Google Oauth를 활용하였다. 서버 쪽에서 회원의 이메일 정보만 관리를 하고 구글 Oauth를 통해서 해당 이메일이 들어오면 사용자 인증을 해주는 구조로 만들었다. 

3. 임원진의 학회원 글 관리 편의성을 위해 학회원이 업로드한 PDF파일을 서버에서만 관리하는 것이 아니라, 공유된 구글 드라이브에도 연동되게 하였다. 

---

#### 주요 기능
1. 학기/학회원/세션 관리 기능
2. 글 upload 및 delete 기능
3. 댓글 기능
4. 자주쓰인 단어 통계 시각화 기능
5. 익명 박명록 기능

<br>

#### 개발 log  
<ul>
<li>웹페이지 Beta 버전 테스트 (2021.02 ~ 2021.07)</li>
<li>웹페이지 정식오픈 (2021.08 ~ )</li>
</ul>
