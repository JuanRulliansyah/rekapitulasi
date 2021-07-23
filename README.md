### Cara Penggunaan

Pastikan anda sudah menginstall prerequisites

**Step 1 : Jalankan docker-compose.yml**

```
docker-compose up -d
``` 

**Step 2 : Install Depedensi**

```
pip install -r requirements.txt
``` 

**Step 3 : Lakukan Migrasi**

```
python manage.py migrate
``` 

**Step 4 : Jalankan Server**

```
python manage.py runserver
```

### Konfigurasi

| Variable            | Default                               | Required  | Description                  |
| --------------      | ------------------------------------- | --------- | ---------------------------- |
| DB_PRIMARY       | postgresql://admin:admin@db:5432/rekapitulasi  | No        | Postgres URI untuk database utama   |
