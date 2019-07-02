from django.db.models import Max, F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from helloworld.models import Counter


def hello(request):
    # forward 개념이 아니라 rendering을 하는 개념
    return render(request, 'helloworld/hello.html')



def hello2(request,id=0):
    return HttpResponse(f'id:{id}')

def hello3(request):
    jsonresult= {
        'result':'success',
        'data':['hello',1,2,True,('a','b','c')]
    }
    return JsonResponse(jsonresult)

def counter_max(request):
    value=Counter.objects.aggregate(max_groupno=Max('groupno'))
    max_groupno=0 if value['max_groupno'] is None else value['max_groupno']

    return HttpResponse(f'max groupno: {max_groupno}')


def counter_add(request):
    c=Counter()
    c.groupno=1
    c.depth=1
    c.orderno=1
    c.save()

    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 2
    c.save()

    c = Counter()
    c.groupno = 1
    c.depth = 1
    c.orderno = 3
    c.save()
    return HttpResponse('OK')


def counter_update(request):
    # queryset 예제
    # groupno = 1 이고 orderno >= 2 의 게시물의
    # orderno를 1씩 증가
    # __gt, __lt, __gte, __lte
    r = Counter.objects.filter(groupno=1).filter(orderno__gte=2).update(orderno=F('orderno')+1)

    return HttpResponse('OK')
