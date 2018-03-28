from django.shortcuts import render
from django.views.generic.base import View

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Course, Lesson




# class Course(models.Model):
#     course_org = models.ForeignKey(CourseOrg, null=True, on_delete=models.CASCADE, verbose_name=u"课程机构")
#     name = models.CharField(max_length=50, verbose_name=u"课程名")
#     desc = models.CharField(max_length=300, verbose_name=u"课程描述")
#     detail = models.TextField(verbose_name=u"课程详情")
#     degree = models.CharField(choices=(("cj","初级"),("zj","中级"),("gj","高级")),max_length=2)
#     learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
#     students = models.IntegerField(default=0,verbose_name=u"学习人数")
#     fav_nums = models.IntegerField(default=0,verbose_name=u"收藏人数")
#     image = models.ImageField(upload_to="courses/%Y/%m",verbose_name=u"封面图",max_length=100)
#     click_nums = models.IntegerField(default=0,verbose_name=u"点击数")
#     add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
#
#     class Meta:
#         verbose_name = u"课程"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name
class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by(("-add_time"))

        hot_course = Course.objects.all().order_by(("-click_nums"))[:3]

        #课程排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_courses = all_courses.order_by("-students")
            elif sort == "hot":
                all_courses = all_courses.order_by("-click_nums")

        #对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, 3, request=request)

        courses = p.page(page)

        return render(request, 'course-list.html', {
            "all_courses": courses,
            "sort": sort,
            "hot_courses": hot_course

        })

class CourseDetailVIew(View):
    """
    课程详情页
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        #增加课程点击数
        course.click_nums += 1
        course.save()

        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:3]
        else:
            relate_courses = []
        return render(request, "course-detail.html", {
            "course": course,
            "relate_courses": relate_courses,
            # "has_fav_course": has_fav_course,
            # "has_fav_org": has_fav_org

        })

