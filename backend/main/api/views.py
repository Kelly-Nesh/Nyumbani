from . import serializer as sz
from main import models as mdl
from serializer.viewsets import ModelViewSet


class TownViewSet(ModelViewSet):
	serializer_class = sz.TownSerializer
	queryset = mdl.Town.objects.order_by("name")
	lookup_field = 'slug'

	def partial_update(self, request, **kwargs):
		# custom images updater
		super().partial_update(*args, **kwargs)


class SuburbViewSet(ModelViewSet):
	serializer_class = sz.SuburbSerializer
	queryset = mdl.Suburb.objects.order_by("name")
	lookup_field = 'slug'

	def partial_update(self, request, **kwargs):
		# custom images updater
		super().partial_update(*args, **kwargs)


class HouseViewSet(ModelViewSet):
	serializer_class = sz.HouseSerializer
	queryset = mdl.House.objects.order_by("name")
	lookup_field = 'slug'

	def partial_update(self, request, **kwargs):
		# custom images updater
		super().partial_update(*args, **kwargs)


class AgentViewSet(ModelViewSet):
	serializer_class = sz.AgentSerializer
	queryset = mdl.Agent.objects.order_by("name")
	lookup_field = 'slug'

	def partial_update(self, request, **kwargs):
		# custom images updater
		super().partial_update(*args, **kwargs)


class UserViewSet(ModelViewSet):
	serializer_class = sz.UserSerializer
	queryset = mdl.User.objects.order_by("name")
	lookup_field = 'slug'

	def partial_update(self, request, **kwargs):
		# custom images updater
		super().partial_update(*args, **kwargs)

