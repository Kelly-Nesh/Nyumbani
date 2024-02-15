from . import serializer as sz
from main import models as mdl
from rest_framework.viewsets import ModelViewSet
from asgiref.sync import sync_to_async


class TownViewSet(ModelViewSet):
    serializer_class = sz.TownSerializer
    queryset = mdl.Town.objects.order_by("name")
    lookup_field = 'slug'

    def partial_update(self, request, **kwargs):
        super().partial_update(request, **kwargs)


class SuburbViewSet(ModelViewSet):
    serializer_class = sz.SuburbSerializer
    queryset = mdl.Suburb.objects.order_by("name")
    lookup_field = 'slug'

    def partial_update(self, request, **kwargs):
        super().partial_update(request, **kwargs)


class HouseViewSet(ModelViewSet):
    serializer_class = sz.HouseSerializer
    queryset = mdl.House.objects.order_by("name")
    lookup_field = 'slug'

    def partial_update(self, request, **kwargs):
        # custom images updater
        partial_update(mdl.House, request, **kwargs)
        super().partial_update(request, **kwargs)


class AgentViewSet(ModelViewSet):
    serializer_class = sz.AgentSerializer
    queryset = mdl.Agent.objects.order_by("name")
    lookup_field = 'slug'

    def partial_update(self, request, **kwargs):
        super().partial_update(request, **kwargs)


class UserViewSet(ModelViewSet):
    serializer_class = sz.UserSerializer
    queryset = mdl.User.objects.order_by("name")
    lookup_field = 'slug'

    def partial_update(self, request, **kwargs):
        super().partial_update(request, **kwargs)



def partial_update(model, request, **kwargs):
    """patches product instance
    Args:
        model: Model to be updated
        request: request
        kwargs: kwargs
    Attrs:
        qs: Queryset
    """
    post = request.POST
    data_dict = dict(**request.data)
    qs = model.objects.filter(slug=kwargs['slug'])
    instance = qs[0]

    # delete images
    try:
        removed_images = post.getlist('images')
    except KeyError:
        pass
    else:
        del_imgs = [mdl.Image.objects.get(image=i[7:]) for i in removed_images]
        instance.images.remove(*del_imgs)

    # Add new images
    async_add = sync_to_async(add_images(instance, post),
                  thread_sensitive=False)

    async_update = sync_to_async(qs.aupdate(**format_dict(data_dict)),
                                 thread_sensitive=False)
    return Response(data=f'{instance.name} updated')


def add_images(instance, postdata):
    # Adds images to instance m2m image field
    try:
        new_images = postdata.getlist('newimages')
    except KeyError:
        return
    images = [mdl.Image.objects.get(image=i[7:])
              for i in new_images]
    return instance.images.add(*images)


def format_dict(qdict) -> dict:
    """Turns immutable queryDict into mutable dict"""
    newdict = {}
    for k, v in qdict.items():
        if k == 'newimages' or k == 'images':
            continue
        newdict[k] = v[0]
    return newdict
