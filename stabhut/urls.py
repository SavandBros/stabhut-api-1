from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

from account.views import UserViewSet
from card.views import CardViewSet
from column.views import ColumnViewSet
from organization.views import OrganizationViewSet
from project.views import ProjectViewSet
from stabhut.settings import ADMIN_URL
from task.views import TaskViewSet

router = routers.DefaultRouter()

router.register('users', UserViewSet)
router.register('organizations', OrganizationViewSet)
router.register('projects', ProjectViewSet)
router.register('tasks', TaskViewSet)
router.register('columns', ColumnViewSet)
router.register('cards', CardViewSet)

urlpatterns = router.urls
urlpatterns += [
    path(ADMIN_URL, admin.site.urls),
    path('docs/', include_docs_urls(title='Nano Gaming API')),
    path('auth/', include('rest_framework.urls')),
    path('auth/', obtain_jwt_token),
]
