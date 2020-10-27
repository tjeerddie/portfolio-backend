from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from .time_stamped import TimeStampedModel


class Portfolio(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    # TODO: libary needs to be added to allow for easy phone number field
    # https://github.com/stefanfoulis/django-phonenumber-field
    phone = models.IntegerField()
    profession = models.CharField(max_length=45)
    summary = models.TextField(blank=True)
    website = models.URLField(max_length=200, blank=True)
    picture = models.ImageField(upload_to=None, blank=True)
    private = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Portfolio")
        verbose_name_plural = _("Portfolios")

    def __str__(self):
        return self.name
