from django.db import models

from organization.models import Organization
from project.models import Project


class Milestone(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    closed = models.BooleanField(default=False)
    due_date = models.DateField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def organization(self) -> Organization:
        return self.project.organization

    def __str__(self):
        return self.name
