from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST,require_GET
from .models import Image
from .forms import ImageCreateForm
#import redis
from django.conf import settings
from common.decorators import ajax_required
from actions.utils import create_action

# Create your views here.

#连接Redis数据库   heroku 不能用双数据库
# r = redis.StrictRedis(host=settings.REDIS_HOST,
#                       port=settings.REDIS_PORT,
#                       db=settings.REDIS_DB)


@login_required
def image_create(request):
    """使用图片的视图函数"""
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)

            #指定用户
            new_item.user = request.user
            new_item.save()
            create_action(request.user,'bookmarked image',new_item) #添加用户行为
            messages.success(request, '图片添加成功')

            #返回一个新建的item的细节视图
            return redirect(new_item.get_absolute_url())

    else:
        #通过GET建立一个表单
        form = ImageCreateForm(data=request.GET)
    return render(request, 'images/image/create.html', {'section':'images',
                                                        'form':form})



def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)

    total_views = image.views_time()
    #total_views = r.incr('image:{}:views'.format(image.id))
    # 利用redis
    #r.zincrby('image_ranking', image.id, 1)
    return render(request,
                  'images/image/detail.html',
                  {'section': 'images',
                   'image': image,
                   'total_views': total_views
                   })






@ajax_required
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
                create_action(request.user,'likes',image)  #添加用户行为
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status':'ko'})
        except:
            pass

    return JsonResponse({'status':'ok'})


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            # If the request is AJAX and the page is out of range return an empty page
            return HttpResponse('')
        # If page is out of range deliver last page of results
        images = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,
                      'images/image/list_ajax.html',
                      {'section': 'images', 'images': images})
    return render(request,
                  'images/image/list.html',
                   {'section': 'images', 'images': images})


@login_required
def image_ranking(request):
    # get image ranking dictionary
    #image_ranking = r.zrange('image_ranking', 0, -1, desc=True)[:10]

    image_ranking = Image.objects.all().order_by(Image.times)
    image_ranking_ids = [int(id) for id in image_ranking]
    # get most viewed images
    most_viewed = list(Image.objects.filter(id__in=image_ranking_ids))
    most_viewed.sort(key=lambda x: image_ranking_ids.index(x.id))
    return render(request,
                  'images/image/ranking.html',
                  {'section': 'images',
                   'most_viewed': most_viewed})