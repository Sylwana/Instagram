from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views import View

from Igers.models import User
from Photos.models import Photo


class PhotoListView(View):
    #
    # permission_required = 'Photos.list_photo'
    # raise_exception = True

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        photos = Photo.objects.all()
        return request('photo_list.html', {'user': user,
                                           'photos': photos})
