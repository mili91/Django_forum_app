from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from .forms import ThreadForm
from .models import Thread


def index(request):
    form = ThreadForm()
    
    threads = Thread.objects.all()
    
    context = {'form' : form, 'threads' : threads}
    return render(request, 'forum/index.html', context)

def thread(request, thread_id):
    thread = Thread.objects.get(pk=thread_id) 

    context = {'thread' : thread}
    return render(request, 'forum/thread.html', context)
    
@require_POST
def new_thread(request):
    form = ThreadForm(request.POST)
    thread = form.save()
    return redirect('thread')