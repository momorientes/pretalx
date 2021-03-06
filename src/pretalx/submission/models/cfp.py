from django.db import models
from django.utils.timezone import now
from i18nfield.fields import I18nCharField, I18nTextField

from pretalx.common.mixins import LogMixin


class CfP(LogMixin, models.Model):
    event = models.OneToOneField(
        to='event.Event',
        on_delete=models.PROTECT,
    )
    headline = I18nCharField(
        max_length=300,
        null=True, blank=True,
    )
    text = I18nTextField(null=True, blank=True)
    default_type = models.ForeignKey(
        to='submission.SubmissionType',
        on_delete=models.PROTECT,
        related_name='+',
    )
    deadline = models.DateTimeField(null=True, blank=True)

    @property
    def is_open(self):
        if self.deadline is not None:
            return now() <= self.deadline
        return True

    def __str__(self) -> str:
        return str(self.headline)
