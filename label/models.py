from django.db import models

from card.models import Card
from organization.models import Organization


class Label(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class LabelObject(models.Model):
    class Kind(models.IntegerChoices):
        CARD = 1

    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    kind = models.PositiveIntegerField(choices=Kind.choices, db_index=True)
    to = models.PositiveIntegerField(db_index=True)

    @property
    def organization(self):
        return self.label.organization

    @property
    def to_object(self) -> Card:
        if self.kind == LabelObject.Kind.USER:
            return Card.objects.get(username=self.to)

    def __str__(self):
        return '[{kind}] {to_object} is labeled with {label}'.format(
            kind=self.get_kind_display(),
            to_object=self.to_object,
            label=self.label,
        )

    class Meta:
        unique_together = (('label', 'kind', 'to'),)
