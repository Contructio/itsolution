from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import messageFromSpace
from .serializer import MessageSerializer


def index(request):
    return render(request, 'main_app.html')


class messageView(ModelViewSet):
    queryset = messageFromSpace.objects.filter(msg_read=False)
    serializer_class = MessageSerializer
