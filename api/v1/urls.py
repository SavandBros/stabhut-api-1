from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from account.views import UserViewSet
from api.v1.stabber.views import (
    CardViewSet,
    ColumnViewSet,
    LabelObjectViewSet,
    LabelViewSet,
    MilestoneViewSet,
    OrganizationViewSet,
    ProjectViewSet,
    TaskViewSet,
    ChatViewSet,
)


router = routers.DefaultRouter()

router.register("user", UserViewSet)
router.register("organization", OrganizationViewSet)
router.register("milestone", MilestoneViewSet)
router.register("project", ProjectViewSet)
router.register("label", LabelViewSet)
router.register("label-object", LabelObjectViewSet)
router.register("task", TaskViewSet)
router.register("chat", ChatViewSet)
router.register("column", ColumnViewSet)
router.register("card", CardViewSet)

urlpatterns = router.urls

urlpatterns += [
    path("auth/", include("rest_framework.urls")),
    path("auth/", obtain_jwt_token),
]
