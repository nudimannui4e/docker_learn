#Описание:
  - Изучение docker, docker-compose
  - По сути, сюда буду кидать рабочие конфиги

### Docker команды
  ```sh
  # остановить все
  $ docker stop $(docker ps -aq)
  
  # узнать ID конкретного контейнера
  $ docker ps -aqf "name=CONTAINER_NAME"
  
  # войти в bash-shell контейнера
  $ docker exec it $NAME bash
  ```



