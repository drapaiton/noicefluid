# heroku-polls-backend

This repo contains Python backend code and configuration files for Heroku.

## Local setup

To develop locally create `.env` file within `./src` directory and add following code to it:  
```
DEBUG=True
SECRET_KEY=<insert_secret_key_here>
ALLOWED_HOSTS=*,
```

Once container is up and running apply migrations (a one-time operation) and create superuser by executing:  
`docker ps` -> to list all running containers and retrieve id or name of running backend container  
`docker exec -it <id_or_name_of_running_container> /bin/bash` -> to enter the container  
`python manage.py migrate` -> to execute migrations  
`python manage.py createsuperuser` -> to create superuser  
`exit` -> to exit the container  