from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404
from .forms import NewTopicForm
from .models import Board,Topic,Post
from django.http import Http404

def home(request):
    boards = Board.objects.all()
    return render(request, 'boards/home.html', {'boards': boards})

# Create your views here.
def board_topics(request,pk):
    try:
        board=Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request,'boards/topics.html',{'board':board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # T get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'boards/new_topic.html', {'board': board, 'form': form})
