from yang_app import views;
from django.urls import path;
urlpatterns = [
    path('yang/', views.comeon_yy),
    path('yang_app/test1',views.test1),
    path('yang_app/test2',views.test2),
]