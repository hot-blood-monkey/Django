

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post,Comment
from .forms import EmailPostForm,CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

def post_detail(request, year, month, day, post):
    """将一篇文章单独展示"""
    post = get_object_or_404(Post, slug=post,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    #调用get_object_or_404函数，通过slug和时间参数，获取对应的object

    comments = post.comments.filter(active=True) #列出有效的评论
    new_comment = None

    #推荐相似的帖子
    post_tag_ids = post.tags.values_list('id',flat=True)
    similar_posts = Post.published.filter(tags__in=post_tag_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]


    if request.method == "POST":
        #提交评论
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)#创建一条新评论，但是还没有保存到数据库
            new_comment.post = post #把这条评论与对应文章联系在一起
            new_comment.save() #把这条评论保存到数据库
    else:
        comment_form = CommentForm()

    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                   'comments':comments,
                   'new_comment':new_comment,
                   'comment_form':comment_form,
                   'similar_posts':similar_posts})


def post_list(request, tag_slug=None):
    """将全部文章列出来"""
    object_list = Post.published.all()
    tag = None # 标签

    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    #如果点击tag来过滤post ，object_list就会更新
    paginator = Paginator(object_list,3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'page':page,
                   'posts':posts,
                   'tag':tag
                   })

def post_share(request,post_id):
    #同过id 来分享 文章
    post = get_object_or_404(Post, id=post_id, status="published")
    cd = None
    sent = False
    if request.method == "POST":
        #提交表单
        form = EmailPostForm(request.POST)
        if form.is_valid():
            #发送的表单是有效的
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'],cd['email'],post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, '290322402@qq.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html',
                  {'post':post,
                   'form':form,
                   'sent':sent,
                   'cd':cd})





def index(request):
    return HttpResponse('hello,my name is zhoudahao')