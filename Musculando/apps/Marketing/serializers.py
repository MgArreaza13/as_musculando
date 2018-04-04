from rest_framework import serializers
from django.contrib.auth.models import User 
from apps.Marketing.models import tb_mail

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User 
		fields = ('username',)

class MailSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	class Meta:
		model = tb_mail
		fields = '__all__'
		depth = 1
