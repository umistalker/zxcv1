from django.db import models
from django.contrib.postgres.fields.jsonb import JSONField


class Model(models.Model):
    text = JSONField()
    models.JSONField