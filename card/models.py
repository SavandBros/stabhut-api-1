from django.contrib.auth.models import User
from django.db import models

from column.models import Column
from milestone.models import Milestone


class Card(models.Model):
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    assignee = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    epic = models.ForeignKey('Card', blank=True, null=True, default=None, on_delete=models.SET_NULL)
    is_epic = models.BooleanField(default=False)
    milestone = models.ForeignKey(Milestone, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    points = models.FloatField(blank=True, null=True, default=None)
    points_estimate = models.FloatField(blank=True, null=True, default=None)
    order = models.FloatField(default=0)
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
        ordering = ('order', 'updated',)
