from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url,include
from accounts.api.views import UserLoginViewSet
from checklist.api.views import FacebookLogin,TwitterLogin
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token

from .routers import router


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/login', UserLoginViewSet.as_view(), name='login'),
    url(r'^api/', include(router.urls,namespace='myapp')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^accounts/', include('allauth.urls')),
    # url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    # url(r'^rest-auth/twitter/$', TwitterLogin.as_view(), name='twitter_login'),










    

]
