# recipe-app-api

<h3>Commands used</h3>
<ol>
<li>docker build .</li>
<li>docker-compose build</li>
</ol>


```cmd
docker-compose run --rm app sh -c "flake8"
```

**create djano project under app**
```
docker-compose run --rm app sh -c "django-admin startproject app ."
```