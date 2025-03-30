from django.urls import path
from .views import ResumeUploadView,index,result_view

urlpatterns = [
    path('upload/', ResumeUploadView.as_view(), name='resume-upload'),
    path("", index, name="index"),
    path('result/', result_view, name='result-page'),
]
