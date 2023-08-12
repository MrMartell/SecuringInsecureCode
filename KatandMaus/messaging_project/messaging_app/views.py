from django.shortcuts import render
from .models import Message

def list_messages(request):
    messages = Message.objects.all().order_by('-timestamp')
    return render(request, 'messaging_app/list_messages.html', {'messages': messages})

def compose_message(request):
    if request.method == 'POST':
        sender = request.POST['sender']
        content = request.POST['content']
        Message.objects.create(sender=sender, content=content)
    return render(request, 'messaging_app/compose_message.html')


#from django.contrib.auth.decorators import login_required

#@login_required
#def compose_message(request):
    #if request.method == 'POST':
        #sender = request.POST['sender']
        #content = request.POST['content']
        #Message.objects.create(sender=sender, content=content)
    #return render(request, 'messaging_app/compose_message.html')
  
# Set up Django's authentication settings properly in your settings.py file.