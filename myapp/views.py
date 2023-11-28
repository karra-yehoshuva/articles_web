from django.shortcuts import render, get_object_or_404,redirect,HttpResponse,HttpResponseRedirect
from .models import Article
from .forms import ArticlecreateForm,LoginForm,LoginForm,UserRegisterForm,ArticleEditForm
import datetime as dt
from django.db.models import Q
from django.contrib import messages
date1 = dt.datetime.now().date()
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
#from django.shortcuts import render, redirect


# Create your views here.
def new_future(request):
    pass

def article_list(request):
    query = request.GET.get('query')
    articles_list = Article.objects.all() #serch_title
    if query:
        #articles=Article.search_by_title(title_query)
        article = Article.objects.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query) |
            Q(author__username=query)
        )
    paginator = Paginator(articles_list,3)
    page = request.GET.get('page')
    try:
        article = paginator.page(page)
    except PageNotAnInteger:
        article = paginator.page(1)
    except EmptyPage:
        article = paginator.page(paginator.num_pages)

    return render(request,'all_articles_list.html',{'article':article})

def Artical_Detail(request,id,slug):
    article = get_object_or_404(Article,id=id)
    is_liked = False
    if article.likes.filter(id=request.user.id).exists():
        is_liked=True
    return render(request,'Artical_detail.html',{
        'article':article,
        'is_liked':is_liked,
        'total_likes':article.total_likes()})

def Likes_View(request):
    aid = request.POST.get('article_id')
    article = get_object_or_404(Article,id=aid)

    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
        is_liked = False
    else:
        try:
            article.likes.add(request.user)
            is_liked = True
        except:
            return redirect('loginform')

    return HttpResponseRedirect(article.get_absolute_url())


def article_create(request):
    if request.method == 'POST':
        form = ArticlecreateForm(request.POST)
        if form.is_valid:
            title1 = request.POST.get('title')
            body1 = request.POST.get('body')
            print("body",body1)

            Article(
                title = title1,
                body = body1,
                author = request.user,
                created_date = date1

            ).save()
            messages.success(request,"New article is created successfully")
            return redirect('articlelist')
        
    else:
        form = ArticlecreateForm()
        return render(request, 'article_create.html',{'form':form})
    

def UserLoginView(request):    
    if request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username , password=password )
            if user :
                if user.is_active:
                    login(request,user)
                    return redirect('articlelist')
                    messages.success(request,"login successfully")
                else:
                    return HttpResponse('Inactive Person')
                    #messages.error(request,"Account is not active")
            else:
                return HttpResponse('NOne')
        else:
            return HttpResponse('Incorrect Details')
        

        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect('home')  # Redirect to a success page
        # else:
        #     # Handle invalid login
        #     return render(request, 'login.html', {'error': 'Invalid credentials'})
        
    else:
        loginform = LoginForm()
        return render(request,'loginform.html',{'loginform':loginform})

    #return render(request, 'login.html')


def logoutview(request):
    logout(request)
    messages.error(request,"logout done")
    return redirect('articlelist')

def UserRegisterview(request):
    if request.method == 'POST':
        register_form = UserRegisterForm(request.POST)
        if register_form.is_valid():
            new_user = register_form.save(commit=False)
            new_user.set_password(register_form.cleaned_data['password'])
            new_user.save()
            return redirect('loginform')

        else:
            HttpResponse('invalid data')
    else:
        register_form = UserRegisterForm()
        return render(request,'register_form.html',{'register_form':register_form})
    

def ArticleEditView(request,id):
    article = get_object_or_404(Article,id=id)
    if request.method == "POST":
        pass
    else:
        form = ArticleEditForm(instance = article)
        return render(request,'article_edit.html',{'form':form} )
    
