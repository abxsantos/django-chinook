from django.db import models
from django.forms import model_to_dict
from django.utils import timezone


class BaseModel(models.Model):
    class Meta:
        abstract = True

    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)

    @property
    def model_name(self) -> str:
        return str(self.__class__.__name__)

    def __repr__(self) -> str:
        columns = ', '.join(f'{field}="{value}"' for field, value in model_to_dict(self).items())
        return f'{self.model_name}({columns})'
