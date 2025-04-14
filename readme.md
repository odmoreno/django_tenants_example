```
python manage.py makemigrations
```

### Create tenant example

```
python manage.py shell
```

```
from app.models import Client, Domain
tenant = Client(schema_name="public", name="Public")
tenant.save()
domain = Domain(domain="localhost", tenant=tenant, is_primary=True)
domain.save()

exit()
```
