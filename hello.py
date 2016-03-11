# from urlparse import urlparse
def application(env, start_response):
	start_response('200 OK', [('Content-Type', 'text/plain')])
	qs = env['QUERY_STRING']
	res = qs.replace("&","\n")
	return res
