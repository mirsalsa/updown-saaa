from django.urls import path
from . import views

app_name = 'feature_aaya'
urlpatterns = [
    path('', views.files, name='files'),
    path('preform/', views.preform, name='preform'),
    path('postform/', views.postform, name='postform'),
    path('download/', views.download, name='download')
]
