from django.contrib.auth.models import User
from django.db import models

from stabber.models import Project


class Chat(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    @property
    def organization(self):
        return self.project.organization

    def __str__(self):
        return "{user}: {content}".format(user=self.user, content=self.content)

    class Meta:
        ordering = ("-id",)
