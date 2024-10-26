
from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment


# Create your views here.
def index(request):
    return render(request, 'guestbookapp/index.html')

def guest_book(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('guest_book')
    else:
        form = CommentForm()
    comments = Comment.objects.all().order_by('-create_at')
    return render(request, 'guestbookapp/book.html', {'form': form, 'comments': comments})