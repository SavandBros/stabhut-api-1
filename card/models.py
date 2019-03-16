from django.contrib.auth.models import User
from django.db import models

from column.models import Column


class Card(models.Model):
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    content = models.TextField()
    assignee = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    order = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def project(self):
        return self.column.project

    @property
    def organization(self):
        return self.project.organization

    def __str__(self):
        return self.content

    class Meta:
        ordering = (
            '-order',
            '-updated',
        )
