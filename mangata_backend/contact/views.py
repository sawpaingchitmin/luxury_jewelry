from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ContactMessage

@csrf_exempt
def contact_api(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            return JsonResponse({"success": True})

    return JsonResponse({"error": "Invalid request"}, status=400)
