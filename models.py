from django.db.models import (
    Model,
    TextField
)

# Create your models here.
class JobListing(Model):
    title = TextField(null=True, blank=True)
    description = TextField(null=True, blank=True)