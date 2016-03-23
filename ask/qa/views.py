from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator

# Create your views here.
from django.http import HttpResponse
def test(request, *args, **kwargs):
	return HttpResponse('OK')

def questions_all(request, *args, **kwargs):
	questions = Question.objects.order_by('-added_at')
	limit = request.GET.get('limit', 10)
	page = request.GET.get('page', 1)
	paginator = Paginator(questions, limit)
	paginator.baseurl = '/?page='
	page = paginator.page(page)
	return render(request, '/')
