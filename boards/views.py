from django.shortcuts import render
from .models import Board
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
