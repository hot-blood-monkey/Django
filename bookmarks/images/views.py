from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm

# Create your views here.

@login_required
def image_create(request):
    """使用图片的视图函数"""
    if request.method == 'POST':
        form = ImageCreateForm(date=request.POST)
        if form.cleaned_data:
            new_item = form
