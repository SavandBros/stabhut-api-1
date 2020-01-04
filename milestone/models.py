from django.db import models

from organization.models import Organization
from project.models import Project


class Milestone(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    closed = models.BooleanField(default=False)
    due_date = models.DateField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
