from rest_framework import serializers as sz
from main import models as mdl



class TownSerializer(sz.ModelSerializer):
	class Meta:
		model = mdl.Town
		fields = "__all__"


class SuburbSerializer(sz.ModelSerializer):
	town = TownSerializer()
	class Meta:
		model = mdl.Suburb
		fields = "__all__"


class AgentSerializer(sz.ModelSerializer):
	class Meta:
		model = mdl.Agent
		fields = "__all__"


class HouseSerializer(sz.ModelSerializer):
	location = SuburbSerializer
	Agent = AgentSerializer
	class Meta:
		model = mdl.House
		fields = "__all__"


class UserSerializer(sz.ModelSerializer):
	class Meta:
		model = mdl.User
		fields = "__all__"