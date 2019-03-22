from django.db import models

from organization.models import Organization
from stabhut.utils import OBJECT_TYPE_CHOICES


class Label(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class ObjectLabel(models.Model):
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    for_type = models.PositiveIntegerField(choices=OBJECT_TYPE_CHOICES, db_index=True)
    for_object = models.TextField(db_index=True)

    @property
    def organization(self):
        return self.label.organization

    def __str__(self):
        return '{label} of {for_object}'.format(label=self.label, for_object=self.for_object)

    class Meta:
        ordering = ('-id',)
