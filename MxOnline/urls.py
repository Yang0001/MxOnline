
import xadmin
from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from django.views.generic import TemplateView
from django.views.static import serve
from MxOnline.settings import MEDIA_ROOT

from users.views import LoginView, RegisterView, ActiveUserView
from organization.views import OrgView


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    url('^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url('^login/$', LoginView.as_view(), name="login"),
    url('^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$',ActiveUserView.as_view(), name="user_active"),
    #课程机构url配置
    url(r'^org/', include('organization.urls', namespace="org")),
    #课程相关url配置
    url(r'^course/', include('courses.urls', namespace="course")),

    #配置上传文件的处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),

    #课程相关url配置
    url(r'^users/', include('users.urls', namespace="users")),



]
