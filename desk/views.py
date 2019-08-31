from django.shortcuts import render
from .models import Post
from django.utils import timezone
from .forms import PostForm,QuestionForm,AnswerForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
# Create your views here.
def index(request):
	posts=Post.objects.filter(created_date__lte=timezone.now())
	return render(request,'desk/index.html', {'post':posts})



def answer_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date=timezone.now()
            post.save()
            return redirect('index')
    else:
        form = AnswerForm(instance=post)
    return render(request, 'desk/answer_post.html', {'form': form})
                
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = PostForm(instance=post)
    return render(request, 'desk/post_edit.html', {'form': form})        


def question_post(request):
    if request.method =='POST':
        form=QuestionForm(request.POST)    
        if form.is_valid():
            post=form.save(commit=False)
            post.created_date=timezone.now()
            post.save()
            return redirect('index')
    else:
        form =QuestionForm()
        return render(request,'desk/question_post.html',{'form':form})        