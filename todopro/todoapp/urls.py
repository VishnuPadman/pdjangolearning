from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cview/', views.Tasklistview.as_view(), name='cview'),
    path('cdetail/<int:pk>/', views.cdetailview.as_view(),name='cdetail'),
    path('cupdate/<int:pk>/', views.updateview.as_view(), name='cupdate'),
    path('cdelete/<int:pk>/', views.deleteview.as_view(), name='cdelete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
