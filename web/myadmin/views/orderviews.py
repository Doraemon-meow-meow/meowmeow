from django.shortcuts import render,reverse
from django.http import HttpResponse,JsonResponse
from .. models import OrderInfo,Orders

# Create your views here.
def list(request):

	orders=Orders.objects.all()
	context = {'orders':orders}

	# 加载模板
	return render(request,'myadmin/orders/list.html',context)
def edit(request):
	
	uid = request.GET.get('uid',None)
	if not uid:
		return HttpResponse('<script>alert("没有用户数据");location.href="'+reverse('myadmin_orders_list')+'"</script>')

	ob = Orders.objects.get(id = uid )

	if request.method  == 'GET':

		context = {'uinfo':ob}

		return render(request,'myadmin/orders/edit.html',context)
	
	elif request.method == 'POST':
		try:

			ob.status = request.POST['status']
			ob.save()
			return HttpResponse('<script>alert("success");location.href="'+reverse('myadmin_orders_list')+'"</script>'	)
		except:
			return HttpResponse('<script>alert("fiald");location.href="'+reverse('myadmin_orders_edit')+'"</script>'	)	