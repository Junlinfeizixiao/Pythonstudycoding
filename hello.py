
#wsgi只要求web开发者实现一个函数，就可以响应HTTP请求
#environ :一个包含所有HTTP请求信息的dict对象
#start_response: 一个发送HTTP响应的函数
def application(environ,start_response):
	start_response('200 OK',[('Content-Type','text/html;charset=utf-8')])
	body = '<h1>Hello,%s!</h1>'%(environ['PATH_INFO'][1:]or'web')
	return [body.encode('utf-8')]