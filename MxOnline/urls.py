
import xadmin
from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from django.views.static import serve
from MxOnline.settings import MEDIA_ROOT, STATICROOT

from users.views import IndexView
from users.views import LoginView, LogoutView, RegisterView, AciveUserView, ForgetPwdView, ResetView, ModifyPwdView
from organization.views import OrgView


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    url('^$', IndexView.as_view(), name="index"),
    url('^login/$', LoginView.as_view(), name="login"),
    url('^logout/$', LogoutView.as_view(), name="logout"),
    url('^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', AciveUserView.as_view(), name="user_active"),
    url(r'^forgetpwd/$', ForgetPwdView.as_view(), name="forget_pwd"),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),

    #课程机构url配置
    url(r'^org/', include('organization.urls', namespace="org")),

    #课程相关url配置
    url(r'^course/', include('courses.urls', namespace="course")),

    #配置上传文件的处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),

    # url(r'^static/(?P<path>.*)$', serve, {"document_root": STATICROOT}),

    #课程相关url配置
    url(r'^users/', include('users.urls', namespace="users")),

    #富文本相关url
    url(r'^ueditor/',include('DjangoUeditor.urls' )),

]

#全局404页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'