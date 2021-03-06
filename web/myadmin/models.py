from django.db import models

# Create your models here.
class Users(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=80)
	email = models.CharField(max_length=50)
	phone = models.CharField(max_length=11)
	age = models.IntegerField(null=True)
	sex = models.CharField(max_length=1)
	pic = models.CharField(max_length=100,null=True)
    #
	status = models.IntegerField(default=0)
	addtime = models.DateTimeField(auto_now_add=True)




# 会员地址
class Address(models.Model):
    uid =  models.ForeignKey(to="Users", to_field="id")
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=20)
    xiangxi = models.CharField(max_length=50)
    status = models.IntegerField(default=0)

# 
class Types(models.Model):
    name = models.CharField(max_length=20)
    pid = models.IntegerField()
    path = models.CharField(max_length=50)

    def __str__(self):
        return '<Types: Types object:'+self.name+'>'
#
class  Goods(models.Model):
    # 一对多
    typeid =  models.ForeignKey(to="Types", to_field="id")
    title = models.CharField(max_length=255)
    descr = models.CharField(max_length=255,null=True)
    info = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pic = models.CharField(max_length=100)
    # 0 新发布,1下架
    status = models.IntegerField(default=0)
    store = models.IntegerField(default=0)
    num = models.IntegerField(default=0)
    clicknum = models.IntegerField(default=0)
    addtime = models.DateTimeField(auto_now_add=True)

#
# 订单模型
class Orders(models.Model):
    uid = models.ForeignKey(to="Users", to_field="id")
    addressid = models.ForeignKey(to="Address", to_field="id")
    totalprice = models.FloatField()
    totalnum = models.IntegerField()
    status = models.IntegerField(default=0)
    addtime = models.DateTimeField(auto_now_add=True,null=True)

# 订单详情
class OrderInfo(models.Model):
    orderid = models.ForeignKey(to="Orders", to_field="id")
    gid = models.ForeignKey(to="Goods", to_field="id")
    num = models.IntegerField()
#houtai
class Wordadmin(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=80)
    
    class Meta():
        db_table = 'admin_password'