from django.shortcuts import render,reverse
from django.http import HttpResponse,JsonResponse
from .. models import Types

# Create your views here.

def fenlei():
	#获取所有的分类信息
	tlist = Types.objects.extra(select = {'paths':'concat(path,id)'}).order_by('paths')

	for x in tlist:
		if x.pid == 0:
			x.pname = '顶级分类'
		else:
			t = Types.objects.get(id=x.pid)
			x.pname = t.name
		num = x.path.count(',')-1
		x.name = (num*'>>>')+x.name

	return tlist


def add(request):
	if request.method == 'GET':
		# 返回一个添加的页面
		tlist = fenlei()

		context = {'tlist':tlist}

		return render(request,'hou/types/add.html',context)

	else:
		#执行分类的添加
		ob = Types()
		ob.name = request.POST['name']
		ob.pid = request.POST['pid']
		if ob.pid == '0':
			ob.path ='0,'
		else:
			#根据当前父级id获取path,再添加当前父级id
			t = Types.objects.get(id=ob.pid)
			ob.path = t.path+str(ob.pid)+','
		ob.save()


		return HttpResponse('<script>alert("添加成功");location.href="'+reverse('hou1_list')+'"</script>')


def index(request):

	#获取搜索条件
	types = request.GET.get('type',None)
	keywords = request.GET.get('keywords',None)

	#判断是否具有搜索条件

	if types:
		if types == 'all':
			#全条件搜索
			#select * from user where username like '%aa%' 
			from django.db.models import Q
			tlist = Types.objects.filter(
				Q(name__contains=keywords)|
				Q(pid__contains=keywords)
			)
		elif types == 'name':
			# 按照用户名搜索
			tlist = Types.objects.filter(name__contains=keywords)
		elif types=='pid':
			if keywords == '顶级分类':
				tlist=Types.objects.filter(pid__contains=0)
			else:
				ks=Typesinfo.objects.get(name=keywords).id
				tlist=Types.objects.filter(pid__contains=ks)
	else:

		# tlist = Types.objects.filter()
		tlist = fenlei()

	#导入分页类
	from django.core.paginator import Paginator

	# 实例化分页对象,参数1,数据集合,参数2 每页显示条数
	paginator = Paginator(tlist, 5)

	#获取当前页码数
	p = request.GET.get('p',1)

	#获取当前页的数据
	ulist = paginator.page(p)

	# tlist = fenlei()

	for x in ulist:
		if x.pid == 0:
			x.pname = '顶级分类'
		else:
			t = Types.objects.get(id=x.pid)
			x.pname = t.name
		num = x.path.count(',')-1
		x.name = (num*'>>>')+x.name

	# 分配数据
	context = {'tlist':ulist}

	# 加载模板
	return render(request,'hou/types/list.html',context)


def delete(request):
	tid = request.GET.get('uid',None)

	#判断当前类下是否子类
	num = Types.objects.filter(pid=tid).count()

	if num != 0:
		data = {'msg':'有子类,不能删','code':1}

	else:
		#判断当前类下是否商品
		ob = Types.objects.get(id=tid)
		ob.delete()

		data = {'msg':'删除成功','code':0}

	return JsonResponse(data)



def edit(request):
	# 接受参数
    uid = request.GET.get('uid',None)
    # 获取对象
    ob = Types.objects.get(id=uid)

    if request.method == 'GET':
       
        # 分配数据
        context = {'uinfo':ob}
        # 显示编辑页面
        return render(request,'hou/types/edit.html',context)

    elif request.method == 'POST':

        ob.name = request.POST['name']
        ob.save()

        return HttpResponse('<script>alert("更新成功");location.href="'+reverse('hou1_list')+'"</script>')





