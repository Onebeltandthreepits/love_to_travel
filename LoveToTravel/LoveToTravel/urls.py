"""LoveToTravel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.core.paginator import Paginator
from django.shortcuts import render

import xadmin
from place.models import AreaModel, ScenicSpotModel
def index(request):
    # 查询一级地区
    areas = AreaModel.objects.filter(parent__isnull=True)
    # 获取当前显示的分类id
    area_id = int(request.GET.get('area_id', 0))
    if area_id:
        print(area_id)
        scenic_spots = ScenicSpotModel.objects.filter(area__parent_id=area_id).all()
        for spot in scenic_spots:
            print(spot)
            print(spot.cover)
    else:
        # 查询所有景点
        scenic_spots = ScenicSpotModel.objects.all()
        for scenic_spot in scenic_spots:
            print(scenic_spot)
            print(scenic_spot.cover)
    # 实现分页
    paginator = Paginator(scenic_spots, 2)  # 2表示每页显示的记录数
    pager = paginator.page(int(request.GET.get('page', 1)))  # 获取指定页面的小说

    return render(request, 'index.html', locals())

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^index/', index)
]
