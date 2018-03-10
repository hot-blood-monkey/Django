from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm

# Create your views here.

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
            messages.success(request, '图片添加成功')

            #返回一个新建的item的细节视图
            return redirect(new_item.get_absolute_url())

    else:
        #通过GET建立一个表单
        form = ImageCreateForm(data=request.GET)

    return render(request, 'images/image/create.html', {'section':'images',
                                                        'form':form})

