from django.http import JsonResponse

def index(request):
    return JsonResponse({"message": "Backend is working!"})