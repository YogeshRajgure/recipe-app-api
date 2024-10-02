# recipe-app-api

<h3>Commands used</h3>
<ol>
<li>docker build .</li>
<li>docker-compose build</li>
</ol>


```powershell
docker-compose run --rm app sh -c "flake8"
```

**create djano project under app**
```powershell
docker-compose run --rm app sh -c "django-admin startproject app ."
```

**If we rin into any error while migrating**\
eg.
```powershell
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate
```
may sometimes give error for incosistant migrations, at that time, just do follwing
```powershell
docker volume ls
docker-compose down
# find you volume and run the remove command 2 times
docker volume rm recipe-app-api_dev-db-data
docker volume rm recipe-app-api_dev-db-data
# verify
docker volume ls
```