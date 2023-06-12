from django.urls import path, include

# after '/user/' ->
urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
]

# -------------------------------
#           ROUTERS
# -------------------------------

from rest_framework.routers import DefaultRouter
from .views import UserView,UserCreateView

router = DefaultRouter()
router.register("create",UserCreateView) #Allowany
router.register('', UserView)            #İsStaff
urlpatterns += router.urls
