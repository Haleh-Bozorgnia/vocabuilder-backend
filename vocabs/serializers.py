from .models import Vocab
from rest_framework import serializers


class VocabSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        # model to serialize
        model = Vocab
        # fields to show in json
        fields = ('id', 'vocab', 'translation', 'pronounciation', 'type')