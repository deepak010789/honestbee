Please follow these steps to start this project:

1. Clone this repo
2. Go to repo dir
3. cd project2/
4. sudo apt install docker-compose
5. sudo dockerd -H 0.0.0.0:2375 &
6. export DOCKER_HOST=127.0.0.1:2375
7. docker-compose build
8. docker-compose up
9. docker start honestbee_web_app
10. Hit browser: http://<IP/Hostname>:8000/
