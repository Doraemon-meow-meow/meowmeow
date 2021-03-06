from django import template
from django.utils.html import format_html

register = template.Library()


#自定义页面优化显示标签
@register.simple_tag
def Fy(count,request):

	p = int(request.GET.get('p',1))

	#开始页
	ks = p-4

	#结束页
	js = p+5

	#判断如果当前页 小于5
	if p < 5:
		#则开始页为1
		ks = 1
		#结束页为10
		js = 10

	#判断如果当前页 大于 总页数-5
	if p > count-5:

		ks = count-9

		js = count

	#判断如果开始页 小于等于 0,则开始页为1
	if ks<=0:

		ks = 1

	#拼接当前请求的参数  '&keywords=11&type=all'
	u = ''
	for x in request.GET:

		#排除p参数
		if x != 'p':
			u+= '&'+x+'='+request.GET[x]

	s = ''
	s += '<li><a href="?p=1'+u+'">首页</a></li>'
	if p - 1 <= 0:
		s += '<li class="am-disabled"><a href="?p=1'+u+'">上一页</a></li>'
	else:
		s += '<li><a href="?p='+str(p-1)+u+'">上一页</a></li>'

	for x in range(ks,js+1):
	# 判断是否为当前页
		if p == x:
			s += '<li class="am-active"><a href="?p='+str(x)+u+'">'+str(x)+'</a></li>'
		else:
			s += '<li><a href="?p='+str(x)+u+'">'+str(x)+'</a></li>'


	if p+1 > count:
		s += '<li class="am-disabled"><a href="?p='+str(count)+u+'">下一页</a></li>'
	else:
		s += '<li><a href="?p='+str(p+1)+u+'">下一页</a></li>'

		s += '<li><a href="?p='+str(count)+u+'">尾页</a></li>'



	return format_html(s)

