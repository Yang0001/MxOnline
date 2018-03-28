app_name = 'course'

from django.conf.urls import url, include

from .views import CourseListView, CourseDetailVIew

urlpatterns = [

    #课程列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),
    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailVIew.as_view(), name="course_detail"),

]
