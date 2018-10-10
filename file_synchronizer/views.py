from django.http import JsonResponse

from file_synchronizer.utils import get_classes, clear
from file_synchronizer.utils import get_files_list
from file_synchronizer.utils import search_for_files

MEDIA_ROOT = 'media/'
DIR = ''


def initial_synch(request):
    clear()
    search_for_files(classes=get_classes(),
                     media_files=get_files_list(root_media=MEDIA_ROOT))
    return JsonResponse({"test": "test"})
