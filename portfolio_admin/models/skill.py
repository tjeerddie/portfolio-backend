from django.db import models
from django.utils.translation import gettext_lazy as _
from .time_stamped import TimeStampedModel


class Skill(TimeStampedModel):
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    summary = models.TextField(blank=True)
    source_url = models.URLField(blank=True)

    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")

    def __str__(self):
        return self.name
