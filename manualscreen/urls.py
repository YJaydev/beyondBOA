from django.urls import path
from . import views

urlpatterns = [
    path('try/', views.screen, name='manualscreen-screen'),
    path('try1', views.try1, name='try1'),
    path('dataupdate/', views.dataupdate, name='dataUpdate'),
    path('data/', views.data, name='data'),
    path('update/', views.update, name='update'),
    path('metadata/', views.metadata, name='metadata'),
    path('anydata/', views.anydata, name='anydata'),
]


