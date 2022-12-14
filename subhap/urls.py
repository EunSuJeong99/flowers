
"""hap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
   
    path('', views.home, name='home'),
    path('coocr_upload/<int:i>',views.ocr),
    path('info/<int:i>',views.result),
    path('coocr_upload/army/<int:i>',views.ocrarmy),
    path('coocr_upload/body/<int:i>',views.ocrbody),
    path('coocr_upload/resident/<int:i>',views.ocrresident),
    path('coocr_upload/cont/<int:i>', views.ocrcont),
    path('stats/',views.stats),

    # DB insert path
    path('coocr_insert/body/<int:i>', views.insertBody),
    path('coocr_insert/army/<int:i>', views.insertArmy),
    path('coocr_insert/resume/<int:i>', views.insertResume),
    path('coocr_insert/resident/<int:i>', views.insertResident),
    path('coocr_insert/cont/<int:i>', views.insertCont),
    

]

