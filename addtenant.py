import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "django_tenants_example.settings"
)  # AJUSTA esto al nombre real de tu proyecto
django.setup()

from app.models import Client, Domain

tenant = Client(schema_name="public", name="Public")
tenant.save()
domain = Domain(domain="localhost", tenant=tenant, is_primary=True)
domain.save()

tenant = Client(schema_name="bigco", name="Big Company")
tenant.save()
domain = Domain(domain="bigco.localhost", tenant=tenant, is_primary=True)
domain.save()
