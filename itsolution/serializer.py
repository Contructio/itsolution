from rest_framework.serializers import ModelSerializer

from itsolution.models import messageFromSpace


class MessageSerializer(ModelSerializer):
    class Meta:
        model = messageFromSpace
        fields = ['id', 'msg_text', 'msg_date']