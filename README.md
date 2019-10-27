# 테코브러리 희망도서 알림봇

## 이후

* tecobrary express 의 .env 에
```
SLACK_BOT_URL=http://127.0.0.1:5000/
```
를 추가해준다.

slack bot 은 외부 요청을 받을 일이 없어서 ec2 인스턴스 내부에서의 요청만 처리하면 되므로

Docker container 에 포트포워딩 되어 있는 5000 포트로 요청을 보내면 된다.

## Dockerfile

1. 빌드
```
docker build -t tecobrary-slackbot:latest .
```

2. 실행
```
docker run -e LC_ALL=C.UTF-8 -e SLACK_AUTH_TOKEN=[슬랙_토큰] -e REQUESTED_CHANNEL=[희망도서_요청_알림_채널_ID] -e ENROLLED_CHANNEL=[희망도서_도착_알림_채널_ID] -p 5000:5000 --name tecobrary-slackbot tecobrary-slackbot:latest
```