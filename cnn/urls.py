from django.urls import path
from . import views


urlpatterns = [
    path('',views.UploadView.as_view(),name='upload'),
    path('paint/',views.PaintView.as_view(),name='paint'),
]