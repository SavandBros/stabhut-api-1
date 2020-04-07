from django.contrib import admin

from stabber.models import Organization, Project, Task, Milestone, Column, Card, Label, LabelObject, Chat

admin.site.register(Organization)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Chat)
admin.site.register(Milestone)
admin.site.register(Column)
admin.site.register(Card)
admin.site.register(Label)
admin.site.register(LabelObject)
