# Описание:
  - Изучение docker, docker-compose
  - По сути, сюда буду кидать рабочие конфиги

### Примечание
#### Тут 4 ветки:
  - master (Содержит все)
  - web (Nginx, Python, Wordpress)
  - GIT_APP (Gitlab, Gitea, Jenkins)
  - Other_APP (Redmine, Draw.io, MySQL)
##### Разбито скорее для изучения Git, а не для пользы 😎

### Docker команды
  ```sh
  # остановить все
  $ docker stop $(docker ps -aq)
  
  # узнать ID конкретного контейнера
  $ docker ps -aqf "name=CONTAINER_NAME"
  
  # войти в bash-shell контейнера
  $ docker exec it $NAME bash

  # Удаление контейнеров со статусом 
  $ docker rm $(docker ps -a -q -f status=exited)
  ```



