from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url,include
from accounts.api.views import UserLoginViewSet
from rest_framework_jwt.views import obtain_jwt_token
from .routers import router


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/login', UserLoginViewSet.as_view(), name='login'),
    url(r'^api/', include(router.urls,namespace='myapp')),
    url(r'^api/auth/token/', obtain_jwt_token),
    

]
