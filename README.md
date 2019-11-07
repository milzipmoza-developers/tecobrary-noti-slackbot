# 테코브러리 희망도서 알림봇

## 개발 목적

* 테코브러리 희망 도서 신청 시, 별도의 알림 기능이 존재하지 않던 문제를 해결하기 위해 개발

## 개발 스택

* [Docker](./Dockerfile)
    - 애플리케이션 배포에 특화되어 있다고 하여 테코브러리 배포에 활용하기 위해 미리 체험하기 위해 적용
     
* [Flask 1.1.1](./requirements.txt)
    - 단순한 기능(DB 접근 X, 테코브러리 메인 서버에서 요청을 받아 Slack API 로 요청을 보내는 기능)을 빠르게 개발하기 위한 목적으로 선정
    
## 패키지 파일 설명
```
tecobrary-noti-slackbot
+-- app.py                  // flask 앱 진입점 
+-- slack_api.py            // slack_api 에 요청을 보내는 기능
+-- message_parser.py       // slack 메시지 템플릿
+-- settings.py             // 환경 변수로부터 private 하게 관리할 상수 주입
+-- requiremets.txt         // app dependency
+-- Dockerfile
+-- .env                    // 개발 환경에서만 필요, 내용은 아래를 참고한다.
```

## 개발 환경 세팅

1. ``.env`` 파일을 생성한다. 내용은 다음과 같다.
    ```
    SLACK_AUTH_TOKEN=[slack_api_token]

    REQUESTED_CHANNEL=[희망도서 요청시 메시지를 보낼 채널 ID]
    ENROLLED_CHANNEL=[희망도서 처리시 메시지를 보낼 채널 ID]
    ```

## Dockerfile 및 배포

1. 빌드
```
docker build -t tecobrary-slackbot:latest .
```

2. 실행
```
docker run -e LC_ALL=C.UTF-8 -e SLACK_AUTH_TOKEN=[슬랙_토큰] -e REQUESTED_CHANNEL=[희망도서_요청_알림_채널_ID] -e ENROLLED_CHANNEL=[희망도서_도착_알림_채널_ID] -p 5000:5000 --name tecobrary-slackbot tecobrary-slackbot:latest &
```

## slack bot mention event

nginx setting

```
location /slackbot/ {
    proxy_pass http://127.0.0.1:5000/;
}
```

tecobrary server 에 요청 url 에 ``/slackbot`` 을 붙여서 요청을 보내면 됩니다.

## slack bot settings

1. event subscription 설정

배포된 도메인의 ``/slackbot/infos`` 로 요청을 보내도록 event subscription 에 등록한다.
