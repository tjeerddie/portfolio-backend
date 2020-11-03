from django.db import models
from django.utils.translation import gettext_lazy as _
from .time_stamped import TimeStampedModel


class MediaProfile(TimeStampedModel):
    portfolio = models.ForeignKey('Portfolio', on_delete=models.CASCADE)
    network = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    url = models.URLField(blank=True)
    private = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Media profile")
        verbose_name_plural = _("Media profiles")

    def __str__(self):
        return self.network
