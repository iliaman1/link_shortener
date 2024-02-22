from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _


class SmartUrl(BaseModel):
    full_url = models.URLField(verbose_name=_('Полная ссылка'))
    short_url = models.CharField(db_index=True, verbose_name=_('Сокращенная ссылка'))

    class Meta:
        ordering = ('-updated_at',)
        unique_together = ["full_url", "short_url"]
