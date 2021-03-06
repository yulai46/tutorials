from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from .category import Category
from .profile import Profile


class Subscription(models.Model):

    profile = models.ForeignKey(
        Profile, related_name="subscriptions", on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category, related_name="subscriptions", on_delete=models.CASCADE
    )

    expires = models.DateTimeField()

    class Meta:

        verbose_name = _("subscription")
        verbose_name_plural = _("subscriptions")

    def __str__(self):

        return f"{self.profile} to {self.category}"

    def is_expired(self):

        return self.expires < now()
