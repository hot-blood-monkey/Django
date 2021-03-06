# -*- coding: utf-8 -*-


from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from .forms import LoginForm, UserRegistrationForm,UserEditForm,ProfileEditForm
from .models import Profile, Contact
from django.contrib import messages
from actions.utils import create_action
from actions.models import Action

# Create your views here.



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def dashboard(request):
    #展示默认的行为
    actions = Action.objects.all().exclude(user=request.user)
    following_ids = request.user.following.values_list('id',flat=True)
    if following_ids:
        actions = actions.filter(user_id__in=following_ids.select_related('user','user__profile').prefetch_related('target'))

    actions = actions[:10]
    return render(request,'account/dashboard.html',{'section':'dashboard',
                                                    'actions':actions})


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #创建一个用户，但是还没有保存
            new_user = user_form.save(commit=False)

            #选择密码
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()

            # Create the user profile
            profile = Profile.objects.create(user=new_user)

            # 添加用户行为
            create_action(new_user,'已经创建一个用户')
            return render(request,'account/register_done.html',{'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'account/register.html',{'user_form':user_form})


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'个人资料已经成功更新')

        else:
            messages.error(request,'Failure: 个人资料更新失败')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form':user_form,
                   'profile_form':profile_form})



@login_required
def user_list(request):
    """查询可用用户"""
    users = User.objects.filter(is_active=True)
    return render(request,'account/user/list.html',
                  {'section':'people',
                   'user':users})

@login_required
def user_detail(request,username):
    """应用来用户验证"""
    user = get_object_or_404(User,username=username,is_active=True)
    return render(request,'account/user/detail.html',{'section':'people','user':user})


@ajax_required
@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == "follow":
                Contact.objects.get_or_create(user_form=request.user, user_to=user)
                # 添加用户行为
                create_action(request.user,'正在关注',user)
            else:
                Contact.objects.filter(user_form=request.user, user_to=user).delete()
            return JsonResponse({'status':'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status':'ko'})

    return JsonResponse({'status':'ko'})