from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

from account.views import UserViewSet
from card.views import CardViewSet
from chat.views import ChatViewSet
from column.views import ColumnViewSet
from label.views import LabelViewSet, LabelObjectViewSet
from organization.views import OrganizationViewSet
from project.views import ProjectViewSet
from stabhut.settings import ADMIN_URL
from task.views import TaskViewSet

router = routers.DefaultRouter()

router.register('user', UserViewSet)
router.register('organization', OrganizationViewSet)
router.register('project', ProjectViewSet)
router.register('label', LabelViewSet)
router.register('label-object', LabelObjectViewSet)
router.register('task', TaskViewSet)
router.register('chat', ChatViewSet)
router.register('column', ColumnViewSet)
router.register('card', CardViewSet)

urlpatterns = router.urls
urlpatterns += [
    path(ADMIN_URL, admin.site.urls),
    path('docs/', include_docs_urls(title='StabHut API')),
    path('auth/', include('rest_framework.urls')),
    path('auth/', obtain_jwt_token),
]
