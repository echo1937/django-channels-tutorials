## Django Channels tutorials, Django Real-time apps with WebSockets

### 1、Django Channels Tutorial 🔥: the most minimal Real Time app (not Chat) | Django WebSockets

- [YouTube Link](https://www.youtube.com/watch?v=R4-XRK6NqMA&list=PLe4mIUXfbIqYEOgfh4X_Yz767IntYUSvg)

### 2、Django Channels Tutorial 🔥: Real Time Graph with Chart.js | Django Websocket

- [YouTube Link](https://www.youtube.com/watch?v=tZY260UyAiE&list=PLe4mIUXfbIqYEOgfh4X_Yz767IntYUSvg)

### 3、Django Channels, Celery, Redis: Real Time Broadcasting API response App (Jokes) | Django WebSockets

- [YouTube Link](https://www.youtube.com/watch?v=AZNp1CfOjtE&list=PLe4mIUXfbIqYEOgfh4X_Yz767IntYUSvg)

- Using

    ```shell
    # 在django project目录下:
    celery -A django_channels_tutorials worker -l DEBUG
    celery -A django_channels_tutorials beat -l DEBUG
    ```

- Periodic Tasks
    - 利用beat_schedule设置celery定时任务