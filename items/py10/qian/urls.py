from django.conf.urls import url
from . import views

urlpatterns = [
	#首页
    url(r'^$',views.qian,name='qian_qian'),

    #详情页
    url(r'^info/$',views.info,name='qian_info'),

    #列表页
    url(r'^list/$',views.list,name='qian_list'),

    #注册
    url(r'^register/$',views.register,name='qian_register'),

    #验证码
    url(r'^yanzhen/$',views.yanzhen,name='qian_yanzhen'),

    #登录
    url(r'^login/$',views.login,name='qian_login'),

    #退出登录
    url(r'^togin/$',views.login,name='qian_tlogin')
    #购物车
    #订单
    #个人中心

]