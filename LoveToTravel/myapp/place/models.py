import os
import uuid

from django.db import models


# Create your models here.


class TagModel(models.Model):
    level = models.CharField(max_length=20, verbose_name='级别', unique=True)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    # objects = models.Manager()
    class Meta:
        db_table = 't_tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name  # 去掉复数表示
        ordering = ['-add_time', 'level']

    def __str__(self):
        return self.level


class AreaModel(models.Model):
    title = models.CharField(max_length=20, verbose_name='地区')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    parent = models.ForeignKey('self', verbose_name='所属地区', on_delete=models.SET_NULL, null=True, blank=True, )

    class Meta:
        db_table = 't_area'
        verbose_name = '地区'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ScenicSpotModel(models.Model):
    name = models.CharField(max_length=50, verbose_name='景点')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    area = models.ForeignKey(AreaModel, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属地区')
    hot = models.IntegerField(default=0, verbose_name='热度')
    address = models.CharField(max_length=100, verbose_name='详细地址')
    tags = models.ManyToManyField(TagModel, verbose_name='标签')
    summary = models.TextField(verbose_name='介绍')
    cover = models.ImageField(verbose_name='封面',  # 依赖pillow库
                              upload_to='', null=True, blank=True, default=None)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.cover:
            newFileName = str(uuid.uuid4()).replace('-', '') + os.path.splitext(self.cover.name)[1]
            self.cover.name = newFileName
        else:
            self.cover.name = ''
        super(ScenicSpotModel, self).save()

    class Meta:
        db_table = 't_scenicspot'
        verbose_name = '景点'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name