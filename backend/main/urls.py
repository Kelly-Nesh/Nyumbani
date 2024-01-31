from django.urls import path
from rest_framework.routers import SimpleRouter
from main.api import views as v

router = SimpleRouter()
router.register("town", v.TownViewSet)
router.register("suburb", v.SuburbViewSet)
router.register("house", v.HouseViewSet)
router.register("agent", v.AgentViewSet)
router.register("user", v.UserViewSet)

urlpatterns = router.urls
