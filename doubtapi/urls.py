from django.urls import path

from . import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns=[
    path('student',views.student.as_view(),name='Student'),
    path('teacher',views.teacher,name='Teacher')
]
