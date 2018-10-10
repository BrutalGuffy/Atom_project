from django.http import JsonResponse


def test(request):
    return JsonResponse({"test": "test"})
