import xadmin
from xadmin import views
from place.models import TagModel, AreaModel, ScenicSpotModel


class GlobalSettings(object):
    # 整体配置
    site_title = '爱旅游后台管理系统'
    site_footer = '爱旅游python项目'
    menu_style = 'accordion'  # 菜单折叠

    # 设置app模块的标题
    apps_label_title = {
        'place': '地区管理'
    }

    # 设置app模块的图标
    apps_icons = {
        'place': 'glyphicon glyphicon-book'
    }
    # 模型的图标(参考bootstrap图标插件)
    global_models_icon = {
        AreaModel: "glyphicon glyphicon-book",
    }

class TagAdmin(object):
   # 后台列表显示列
   list_display = ['level', 'add_time']
   # 后台列表查询条件
   search_fields = ['level']


class AreaAdmin(object):
   # 后台列表显示列
   list_display = ['title', 'add_time', 'parent']
   # 后台列表查询条件
   search_fields = ['title']

class ScenicSpotAdmin:
    list_display = ['name', 'add_time', 'summary', 'hot', 'area', 'tags', 'address', 'cover']
    search_fields = ['name']

# class VolumeAdmin:
#     list_display = ['title', 'free_level', 'book', 'add_time']
#     search_fields = ['title', 'free_level', 'book', 'add_time']

# class ChapterAdmin:
#     list_display = ['title', 'content', 'totalNum', 'volume', 'add_time']
#     search_fields = ['title', 'content', 'totalNum', 'volume', 'add_time']

xadmin.site.register(TagModel, TagAdmin)
xadmin.site.register(AreaModel, AreaAdmin)
xadmin.site.register(ScenicSpotModel, ScenicSpotAdmin)
# xadmin.site.register(VolumeModel, VolumeAdmin)
# xadmin.site.register(ChapterModel, ChapterAdmin)

xadmin.site.register(views.CommAdminView, GlobalSettings)