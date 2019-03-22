from django.db import models

from project.models import Project


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    checked = models.BooleanField(default=False)

    @property
    def organization(self):
        return self.project.organization

    def __str__(self):
        return self.content

    class Meta:
        ordering = ('-id',)
