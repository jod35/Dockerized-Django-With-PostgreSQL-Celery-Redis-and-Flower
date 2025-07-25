# Dockerized Django With PostgreSQL Celery Redis and Flower
This is source code for the [video series](https://www.youtube.com/playlist?list=PLEt8Tae2spYmsfui0pD4497Hy28VTEMA3) where we use Docker compose to containerize a Django app with the components.

## How to run the app
Of course you have to clone and write the env file according to the example in [.env.example](.env.example)

Finally run the services with 
```bash
$ docker compose up
```

## Run migrations and collectstatic
```
$ docker compose exec -it app bash
```

followed by (inside the container)

```bash
python3 manage.py migrate
```

collect static files with
```bash
python3 manage.py collectstatic
```

Enjoy!
