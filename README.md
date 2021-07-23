### Usage

Make sure you have installed the prerequisites

**Step 1 : Run docker-compose.yml**

```
docker-compose up -d
``` 

**Step 2 : Install Dependencies**

```
pip install -r requirements.txt
``` 

**Step 3 : Run migration**

```
python manage.py migrate
``` 

**Step 4 : Serve Your API**

```
python manage.py runserver
```

### Configuration

| Variable            | Default                               | Required  | Description                  |
| --------------      | ------------------------------------- | --------- | ---------------------------- |
| KA_DB_PRIMARY       | postgresql://dev:dev@db:5432/ka_core  | No        | Postgres URI for master db   |
