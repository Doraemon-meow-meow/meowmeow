from django.conf.urls import url
from . views import views,userviews,typesviews,goodsviews

urlpatterns = [
	#后台首页
    url(r'^$',views.hou,name='hou_hou'),

    #会员添加
    url(r'^user/add/$',userviews.add,name='hou_add'),

    #会员列表
    url(r'^user/index/$',userviews.index,name='hou_list'),

    # 会员删除
    url(r'^user/delete/$',userviews.delete,name='hou_delete'),

    #会员编辑
    url(r'^user/edit/$',userviews.edit,name='hou_edit'),


    # 商品分类
    url(r'^type/add/$',typesviews.add,name='hou1_add'),

    url(r'^type/index/$',typesviews.index,name='hou1_list'),

    url(r'^type/delete/$',typesviews.delete,name='hou1_delete'),

    url(r'^type/edit/$',typesviews.edit,name='hou1_edit'),

    # 商品
    url(r'^goods/add/$',goodsviews.add,name='hou2_add'),

    url(r'^goods/index/$',goodsviews.index,name='hou2_list'),

    url(r'^goods/delete/$',goodsviews.delete,name='hou2_delete'),

    url(r'^goods/edit/$',goodsviews.edit,name='hou2_edit'),


]
