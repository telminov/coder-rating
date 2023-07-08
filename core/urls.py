from rest_framework.routers import DefaultRouter
import core.views

urlpatterns = [

]

router = DefaultRouter()
router.register('coders', core.views.CoderViewSet, basename='coders')
urlpatterns += router.urls
