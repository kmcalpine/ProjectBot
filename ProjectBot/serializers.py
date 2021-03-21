from rest_framework import serializers
from .models import Reporter

class ReporterSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=70, allow_blank=False)
    msg_response = serializers.CharField(max_length=255, allow_blank=False)
    class Meta:
        model = Reporter
        fields = ['full_name', 'msg_response']
