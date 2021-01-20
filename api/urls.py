from rest_framework.routers import SimpleRouter
from api import views


router = SimpleRouter()

router.register(r'user', views.UserViewSet, 'User')
router.register(r'sms', views.SMSViewSet, 'SMS')

urlpatterns = router.urls
