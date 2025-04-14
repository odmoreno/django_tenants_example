### Migrations
```
python manage.py makemigrations
```

```
python manage.py migrate_schemas --shared
```	
Aplica migraciones solo al schema `público` (y prepara tenant y dominio)


```
python manage.py migrate_schemas
```
✅ Aplica migraciones a:
 1. El schema public
 2. Cada tenant registrado en el modelo Client

```
python manage.py migrate_schemas --schema=bigco
```
Eso aplicará las migraciones solo al schema bigco (por ejemplo, si solo hiciste cambios que afectan a ese cliente).


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

## otra forma de crear un tenant 

````
python .\manage.py create_tenant --domain-domain=smallco.localhost --schema_name=smallco --name=smallco
```