from django.db import models

from project.models import Project


class Column(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    @property
    def organization(self):
        return self.project.organization

    def __str__(self):
        return self.name
