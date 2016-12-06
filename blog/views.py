from django.shortcuts import render , HttpResponseRedirect
from blog.forms import CommentForm , PostForm
from blog.models import Comment , Post
from django.core.exceptions import ObjectDoesNotExist
import bleach
# Create your views here.


def viewPosts(request):
    postlist = Post.objects.all().order_by('date')
    return render(request , 'posts.html' , {'posts' : postlist[::-1] , 'nposts' : len(postlist)})

def NewPost(request):
    if request.method == "POST":
        if request.user.is_staff:
            pform = PostForm(request.POST)
            if pform.is_valid():
                p = pform.save(commit=False)
                p.author = request.user
                p.body = bleach.clean(p.body)
                p.body = p.body.replace("\n" , "<br>")
                p.save()
                return HttpResponseRedirect('/blog')
            else:
                return render(request , 'new_post.html' , {'action' : '/blog/new' , 'do' : 'Post' ,  'merrors' : True , 'form' : pform})
        else:
            return HttpResponseRedirect('/blog')
    else:
        return render(request , 'new_post.html' , {'action' : '/blog/new' , 'do' : 'Post' , 'form' : PostForm()})

def viewPost(request , postid):
    c =""
    cf= CommentForm()
    try:
        p = Post.objects.get(id=postid)
        c = Comment.objects.filter(post=postid)
    except ObjectDoesNotExist:
        if p == None:
            return HttpResponseRedirect("/blog")
        elif c == None:
            c = ""
    return render(request , 'view_post.html' , {'post' : p , 'comments' : c[::-1]})


def DeletePost(request , postid):
    if request.user.is_staff:
        try:
            Post.objects.get(id=postid).delete()
        except ObjectDoesNotExist:
            pass
    return HttpResponseRedirect('/blog')


def EditPost(request , postid):
    if request.user.is_staff:
        if request.method == "GET":
            try:
                p     = Post.objects.get(id=postid)
                pform = PostForm(initial={'body':p.body , 'title':p.title})
                return render(request , 'new_post.html' , {'action' : '/blog/edit/%s' % postid , 'do' : 'Edit' , 'form' : pform})
            except ObjectDoesNotExist:
                pass
        else:
            pform = PostForm(request.POST)
            if pform.is_valid():
                try:
                    p = Post.objects.get(id=postid)
                    p.title = pform.cleaned_data['title']
                    p.body  = bleach.clean(pform.cleaned_data['body'])
                    p.save()
                    return HttpResponseRedirect("/blog/%s" % postid)
                except ObjectDoesNotExist:
                    pass
            else:
                return render(request , 'new_post.html' , {'action' : 'blog/edit/%s' % postid , 'do' : 'Edit' ,  'merrors' : True , 'form' : pform})
    return HttpResponseRedirect("/blog")

def postComment(request , postid):
    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                p = Post.objects.get(id=postid)
                cf= CommentForm(request.POST)
                if cf.is_valid():
                    c = cf.save(commit=False)
                    c.post     = p
                    c.poster   = request.user
                    c.username = request.user.username
                    c.bodytext = bleach.clean(c.bodytext)
                    c.save()
                    p.comments += 1
                    p.save()
                    return HttpResponseRedirect("/blog/%s" % postid)
                else:
                    c = Comment.objects.filter(post=postid)
                    return render(request , 'view_post.html', { 'comments' : c , 'post' : p , 'commenterror' : 'minimum length allowed : 10 chars, maxmimum length : 200 chars'})
            except ObjectDoesNotExist:
                pass
    return HttpResponseRedirect("/blog")


def DeleteComment(request , postid , commentid):
    if request.user.is_staff:
        try:
            p = Post.objects.get(id=postid)
            Comment.objects.get(id=commentid).delete()
            p.comments -= 1
            p.save()
            return HttpResponseRedirect("/blog/%s" %postid)
        except ObjectDoesNotExist:
            pass
    return HttpResponseRedirect("/blog")
