from django.http import JsonResponse

def index(request):
    return JsonResponse({"message": "Backend is working!"})

def root(request):
    return JsonResponse({"message": "Welcome to the root!"})