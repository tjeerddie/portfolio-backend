from django.db import models
from django.utils.translation import gettext_lazy as _
from .time_stamped import TimeStampedModel
from .portfolio import Portfolio


class Project(TimeStampedModel):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    company = models.CharField(max_length=120)
    position = models.CharField(max_length=120)
    summary = models.TextField(blank=True)
    website = models.URLField(blank=True)
    source = models.URLField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    private = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.name
