from django.test import TestCase

from file_synchronizer.utils import get_files_list
from file_synchronizer.utils import search_for_files
from file_synchronizer.utils import get_classes
from file_synchronizer.utils import DisableSignals
from file_synchronizer.models import FileSynchronizer

ROOT = 'media/'
DIR = 'test'


class AnimalTestCase(TestCase):
    """Проверка метода get_media_files(). Создает в указанной директории
    текстовый файл и проверяет будет ли он найден тестируемым методом."""
    def test_get_media_files(self):
        test_file = open("media/test/test.txt", "w+")
        for x in range(10):
            test_file.write("This is line %d\r\n" % (x + 1))
        test_file.close()
        self.assertEqual(get_files_list(root_media=ROOT, dir=DIR).__len__(), 1)
        search_for_files(classes=get_classes(),
                         media_files=get_files_list(root_media=ROOT, dir=DIR))
        FileSynchronizer.objects.all().filter(model_name='No model').delete()

    def test_search_for_files(self):
        """Проверка метода search_for_files(). Создает в указаной
        дирректории текстовый файл и проверяет, будет ли создан инстанс
        FileSynchronizer для этого файла."""
        test_file = open("media/test/test.txt", "w+")
        for x in range(10):
            test_file.write("This is line %d\r\n" % (x + 1))
        test_file.close()
        search_for_files(classes=get_classes(),
                         media_files=get_files_list(root_media=ROOT, dir=DIR))
        self.assertEqual(list(FileSynchronizer.objects.all()
                              .filter(model_name='No model')).__len__(), 1)
        search_for_files(classes=get_classes(),
                         media_files=get_files_list(root_media=ROOT, dir=DIR))
        FileSynchronizer.objects.all().filter(model_name='No model').delete()

    def test_disable_signals(self):
        """Проверка управления сигналами. Создает в указаной
        дирректории текстовый файл и инстанс FileSynchronizer для этого
        файла. Проверяет, случай, когда удаление инстанса происходит без
        декоратора, удаляющего файл."""
        test_file = open("media/test/test.txt", "w+")
        for x in range(10):
            test_file.write("This is line %d\r\n" % (x + 1))
        test_file.close()
        search_for_files(classes=get_classes(),
                         media_files=get_files_list(root_media=ROOT, dir=DIR))
        with DisableSignals():
            FileSynchronizer.objects.all()\
                .filter(model_name='No model').delete()
        self.assertEqual(list(FileSynchronizer.objects.all()
                              .filter(model_name='No model')).__len__(), 0)
        self.assertEqual(get_files_list(root_media=ROOT, dir=DIR).__len__(), 1)
        FileSynchronizer.objects.all().filter(model_name='No model').delete()
        self.assertEqual(list(FileSynchronizer.objects.all()
                              .filter(model_name='No model')).__len__(), 0)

    def test_delete(self):
        """Проверка удаления инстанса. Создает в указаной
        дирректории текстовый файл и инстанс FileSynchronizer для этого
        файла. Проверяет, что при удалении инстанса файл так-же будет
        удален."""
        test_file = open("media/test/test.txt", "w+")
        for x in range(10):
            test_file.write("This is line %d\r\n" % (x + 1))
        test_file.close()
        search_for_files(classes=get_classes(),
                         media_files=get_files_list(root_media=ROOT, dir=DIR))
        FileSynchronizer.objects.all().filter(model_name='No model').delete()
        self.assertEqual(list(FileSynchronizer.objects.all()
                              .filter(model_name='No model')).__len__(), 0)
