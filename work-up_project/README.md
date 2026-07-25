# Work-up Project

학교와 데이원컴퍼니가 함께 진행하는 4주 직무부트캠프 과정의 학습 기록입니다.

현재는 강의를 들으며 Python 기초 문법과 예제 코드를 정리하고 있습니다. 이 저장소는 완성된 서비스 프로젝트라기보다, 데이원컴퍼니가 제공한 강의에서 나온 코드를 직접 따라 치고 실행해 보면서 개념을 복습하기 위한 공간입니다.

## 코드 출처

이 폴더 안의 모든 코드는 학교와 데이원컴퍼니가 함께 진행하는 직무부트캠프 강의에서 제공된 예제 코드를 학습 목적으로 직접 작성한 내용입니다.

개인 학습 기록과 복습을 위한 저장소이며, 강의 내용을 이해하기 위해 예제 코드를 따라 작성하고 일부 실행 환경 설정을 정리했습니다.

## 학습 목적

- Python 기본 문법을 코드로 직접 실습하기
- 자료구조, 흐름 제어, 함수, 모듈, 객체지향 프로그래밍 개념 익히기
- 강의 중 작성한 예제와 과제를 주제별로 정리하기
- GitHub에 학습 과정을 기록하며 개발 습관 만들기

## 폴더 구조

```text
work-up_project/
├── 1주차/
│   ├── 자료구조/
│   │   ├── variable1.py
│   │   ├── variable2.py
│   │   ├── list.py
│   │   ├── tuple.py
│   │   ├── dictionary.py
│   │   ├── set.py
│   │   └── todo_list.py
│   ├── 흐름제어/
│   │   ├── condition.py
│   │   ├── loop.py
│   │   ├── loop_score.py
│   │   └── exception_handling.py
│   ├── 함수와모듈/
│   │   ├── function.py
│   │   ├── function2.py
│   │   ├── dt_library.py
│   │   ├── rand_library.py
│   │   ├── req_library.py
│   │   ├── module/
│   │   └── calc/
│   ├── 객체지향프로그래밍/
│   │   ├── person.py
│   │   ├── programmer.py
│   │   ├── farmer.py
│   │   ├── actor.py
│   │   ├── account.py
│   │   ├── user.py
│   │   ├── scenario1.py
│   │   ├── scenario2.py
│   │   ├── bank_system.md
│   │   ├── inheritance.py
│   │   └── main.py
│   ├── 알고리즘/
│   │   └── quick_sort.py
│   └── 챗봇/
│       ├── scraper.py
│       └── bot.py
└── my_env/
```

## 학습 내용

### 자료구조

Python에서 데이터를 다루는 기본 방법을 학습합니다.

- 변수 선언과 값 할당
- 리스트, 튜플, 딕셔너리, 집합 사용법
- 간단한 할 일 목록 관리 프로그램 작성

### 흐름 제어

조건문과 반복문을 사용해 프로그램의 실행 흐름을 제어하는 방법을 학습합니다.

- `if`, `elif`, `else` 조건문
- `for`, `while` 반복문
- 점수 처리 예제
- 예외 처리와 `try`, `except`, `else`, `finally`

### 함수와 모듈

반복되는 코드를 함수로 분리하고, 모듈을 활용해 코드를 구조화하는 방법을 학습합니다.

- 함수 정의와 호출
- 표준 라이브러리 사용
- 외부 라이브러리 `requests` 사용
- 직접 만든 모듈과 패키지 불러오기

### 객체지향 프로그래밍

클래스와 객체를 사용해 코드를 구조화하는 방법을 학습합니다.

- 클래스와 인스턴스
- 생성자
- 속성과 메서드
- 상속
- 직업별 클래스 예제 작성
- 은행 계좌 시스템 시나리오 실습

### 알고리즘

기본 정렬 알고리즘을 직접 구현하며 동작 방식을 학습합니다.

- 퀵 정렬 구현

### 챗봇

웹 스크래핑과 Discord 봇 연동을 실습합니다.

- `requests`, `BeautifulSoup`을 사용한 상품 정보 수집
- `discord.py`를 사용한 Discord 봇 메시지 전송
- 봇 토큰을 환경변수로 관리

## 실행 방법

Python 3.12 기준으로 학습을 진행하고 있습니다.

개별 파일은 아래처럼 실행할 수 있습니다.

```bash
python 파일경로.py
```

예시:

```bash
python 1주차/자료구조/todo_list.py
python 1주차/흐름제어/exception_handling.py
python 1주차/함수와모듈/req_library.py
python 1주차/객체지향프로그래밍/inheritance.py
```

가상환경을 사용하는 경우:

```bash
source my_env/bin/activate
python 1주차/함수와모듈/req_library.py
```

Discord 봇을 실행하는 경우 봇 토큰을 환경변수로 설정한 뒤 실행합니다.

```bash
export DISCORD_BOT_TOKEN="본인_디스코드_봇_토큰"
python 1주차/챗봇/bot.py
```

## 현재 상태

- 4주 직무부트캠프 강의 수강 중
- Python 기초 문법과 예제 코드 작성 중
- 학습 내용은 강의 진행 상황에 따라 계속 추가 예정

## 정리 방향

앞으로 학습이 진행되면 다음 내용을 추가로 정리할 예정입니다.

- 수업별 핵심 개념 요약
- 실습 코드 개선
- 과제 및 미니 프로젝트 정리
- 배운 내용을 바탕으로 한 응용 예제 작성
