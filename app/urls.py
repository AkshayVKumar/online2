from django.urls import path,re_path
from . import views
app_name="app"

urlpatterns = [
    path('',views.index,name="index"),
    path('radio/',views.radio,name="radio"),
    path('checkbox/',views.checkbox,name="checkbox"),
    path('select/',views.select,name="select"),
    path('radioop/',views.radio_output,name="radioop"),
    path('file/',views.file_demo,name="file_demo"),
    path('create_topic/',views.create_topic,name="create_topic"),
    path('create_webpage/',views.create_webpage,name="create_webpage"),
    path('select_topic/',views.select_topic,name="select_topic"),
    path('topic_select/',views.topic_select,name="topic_select"),
    path('disp_web/',views.disp_web,name="disp_web"),
]
