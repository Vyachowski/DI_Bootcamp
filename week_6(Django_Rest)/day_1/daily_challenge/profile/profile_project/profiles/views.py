from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render
from .models import Profile
# Create your views here.


@csrf_exempt
def create_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name and email:
            profile = Profile.objects.create(name=name, email=email)
            return JsonResponse({'success': f'Profile {profile.name} created successfully.'})


@csrf_exempt
def delete_profile(request, id):
    if request.method == 'POST':
        profile = get_object_or_404(Profile, id=id)
        profile.delete()
        return JsonResponse({'success': f'Profile {profile.name} deleted successfully.'})