# AttackOnTitan Archive

## 개요

이 프로젝트는 Django 프레임워크를 사용한 Pinterest 타입의 이미지 기반 게시판 웹 애플리케이션입니다.

사용자는 회원가입 및 로그인 후 게시글(이미지 포함)을 등록하고 댓글을 작성할 수 있으며, 게시글은 프로젝트(그룹) 단위로 관리됩니다.

각 게시물은 카드 형식으로 나열되며, `MagicGrid.js`를 사용하여 실제 핀터레스트와 유사한 유동적인 그리드 레이아웃을 구현했습니다.

---

## 주요 기능

### 1. 사용자 인증

* 회원가입, 로그인, 로그아웃 기능 구현
* Django 기본 User 모델 기반
* 사용자 프로필 이미지 및 닉네임 설정 가능

### 2. 프로젝트(그룹) 기능

* 게시물을 프로젝트 단위로 그룹화 가능
* 프로젝트 상세 페이지에서 관련 게시글 확인 가능

### 3. 게시글 CRUD

* 게시글 등록 시 이미지 업로드 지원
* 게시글 상세 페이지에서 수정, 삭제 가능 (작성자 본인만)
* 게시글은 프로젝트에 귀속되며, 해당 프로젝트의 다른 게시글 간 탐색(다음/이전 게시글 버튼) 제공

### 4. card 타입 게시글 리스트 UI

* 게시글 리스트는 카드 형태로 나열
* `card_project.html`과 같은 base snippet 파일을 만들어 재사용 가능한 카드 컴포넌트로 구성
* Bootstrap 기반으로 반응형 UI 구현
<br><br><img width="1331" height="798" alt="image" src="https://github.com/user-attachments/assets/2b3f051e-3851-449b-8982-a83af41ec725" /><br><br>

### 5. 댓글 기능

* 게시글 하단에 댓글 생성, 삭제 기능 구현
* 로그인된 사용자만 댓글 작성 가능
<br><br><img width="669" height="841" alt="image" src="https://github.com/user-attachments/assets/c3e6d8df-3e87-4266-a1b1-892b80b94f7a" /><br><br>

### 6. MagicGrid를 이용한 레이아웃 정렬

* Pinterest 스타일의 비정형 그리드 레이아웃 구현
* `MagicGrid.js`를 이용하여 이미지 크기에 따라 자동 정렬
* 게시물이 동적으로 추가되어도 자연스럽게 정렬 유지

### 7. 페이징 처리

* Django의 `Paginator` 클래스를 활용하여 페이지네이션 구현
* 페이지당 게시글 수 지정 및 페이지 네비게이션 제공

---

## 기술 스택

| 항목       | 내용                                                 |
| -------- | -------------------------------------------------- |
| 백엔드      | Python 3.13, Django 5.2.4                      |
| 프론트엔드    | HTML5, CSS3, JavaScript                            |
| UI 프레임워크 | Bootstrap 4+                                       |
| 레이아웃 정렬  | [MagicGrid.js](https://github.com/e-oj/Magic-Grid) |
| 데이터베이스   | SQLite (개발환경)                                      |

---

## 프로젝트 구조 (일부 발췌)

```
myproject/
├── articleapp/
│   ├── models.py       # 게시글 모델
│   ├── views.py        # 게시글 CRUD + 이전/다음 게시물 처리
│   ├── templates/
│   │   ├── articleapp/
│   │   │   ├── create.html
│   │   │   ├── delete.html
│   │   │   ├── detail.html
|   |   |   ├── list.html
|   |   |   ├── update.html
├── commentapp/         # 댓글 앱
├── projectapp/         # 게시물 그룹화 앱
├── accountapp/         # 사용자 인증 및 프로필 앱
├── templates/
│   ├── base.html        # 전체 레이아웃
│   ├── head.html, header.html, footer.html
└── static/
    ├── js/
    │   └── magicgrid.js
```

---

## 기타 참고 사항

* 게시물 이미지 업로드는 `ImageField`를 사용하여 처리
* 게시물 삭제 후에도 이전/다음 게시물 탐색이 끊기지 않도록 예외 처리 구현
* 댓글 입력창은 textarea 기반으로 자동 줄바꿈 및 입력 길이 증가 지원

---

## 시연

* 프로젝트는 로컬 개발환경 기준 `127.0.0.1:8000`에서 구동되며, 브라우저 탭 이름은 `head.html`에서 설정된 `<title>` 태그에 따라 동적으로 변경 가능

---

## 작성자

* 본 프로젝트는 Django MVT 패턴의 구조를 따라 설계되었으며, 개발자 개인 학습 및 포트폴리오 목적으로 제작되었습니다.
