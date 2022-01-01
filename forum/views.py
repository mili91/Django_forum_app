from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from .forms import ThreadForm

def index(request):
    form = ThreadForm()

    context = {'form' : form}
    return render(request, 'forum/index.html', context)

def thread(request):
    return render(request, 'forum/thread.html')
    
@require_POST
def new_thread(request):
    form = ThreadForm(request.POST)
    thread = form.save()
    return redirect('thread')