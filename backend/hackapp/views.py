from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import PersonSerializer
from .models import Person

# Create your views here.
class PersonView(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    permission_classes = [permissions.AllowAny]
    
def index(request):
    return render(request, 'frontend/index.html')