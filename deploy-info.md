# debug mode (no production)

Default [Settings.py] will be used

overriden configs

> sqlite3  
> redis  
> default secret_key  
> debug = True

needed steps

**1.-**

- set [REDIS_URL] using powershell
<!-- not persistent method -->

```powershell
$Env:REDIS_URL="<put your URI here>"
```

- linux

```bash
i dont know, help
```

# production mode

Default [Settings_production.py] will be used

- set [DATABASE_URL] in heroku credentials
- set [REDIS_URL] in heroku credentials
- set environment variables if needed from environment-example.txt

# END

> note: REDIS_URL can be the same for production mode and debug mode

### License

---

MIT

[//]: # "These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - https://dillinger.io"
[redis_url]: https://drapaiton.github.io/terminology/redis_url/
[database_url]: https://drapaiton.github.io/terminology/database_url/

<!-- .py files -->

[settings_production.py]: https://github.com/drapaiton/noicefluid/blob/master/noicefluid/settings_production.py
[settings.py]: https://github.com/drapaiton/noicefluid/blob/master/noicefluid/settings.py
