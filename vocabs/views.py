from .models import Vocab
from rest_framework import viewsets, permissions
from .serializers import VocabSerializer
class VocabViewSet(viewsets.ModelViewSet):
    ## queryset is a list of all Vocab objects
    queryset = Vocab.objects.all()
    # The serializer_class attribute is used to control which serializer class should be used for serializing and deserializing queryset and model instances.
    serializer_class = VocabSerializer
    # Set permission_classes to allow unrestricted access to the API.
    permission_classes = [permissions.AllowAny]