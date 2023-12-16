from django.contrib import admin
from django.urls import path
from api import views
from api.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index.hmtl'),
    path('stuinfo/<int:pk>',views.student_detail),
    path('stuinfo/',views.student_detail),
]
