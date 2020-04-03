from django.db import models

from account.models import User


class Organization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("order",)


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
        ordering = ("-id",)


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


class Column(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    order = models.IntegerField(default=0)

    @property
    def organization(self):
        return self.project.organization

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("order",)


class Card(models.Model):
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    assignee = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    epic = models.ForeignKey("Card", blank=True, null=True, default=None, on_delete=models.SET_NULL)
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
        ordering = (
            "order",
            "updated",
        )


class Label(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=25, blank=True, null=True)

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
        if self.kind == LabelObject.Kind.CARD:
            return Card.objects.get(pk=self.to)

    def __str__(self):
        return "{kind} named {to_object} is labeled with {label}".format(
            kind=self.get_kind_display(), to_object=self.to_object, label=self.label,
        )

    class Meta:
        unique_together = (("label", "kind", "to"),)
