from django.http import JsonResponse

from file_synchronizer.utils import search_for_files, get_classes, get_files_list
MEDIA_ROOT = 'media/'
DIR = ''


def initial_synch(request):
    search_for_files(classes=get_classes(),
                     media_files=get_files_list(root_media=MEDIA_ROOT,
                                                dir=DIR))
    return JsonResponse({"test": "test"})
