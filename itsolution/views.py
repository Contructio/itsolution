from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from .models import messageFromSpace
from .serializer import MessageSerializer


def index(request):
    return render(request, 'main_app.html')


def mark_read(request):
    id = request.GET.get("id", None)
    if id:
        a = messageFromSpace.objects.get(id=id)
        a.msg_read = True
        a.save()
    return HttpResponse('')


class messageView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        id = self.request.query_params['last_id']
        queryset = messageFromSpace.objects.filter(msg_read=False, id__gte=id)
        return queryset
