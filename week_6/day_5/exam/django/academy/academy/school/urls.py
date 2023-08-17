from django.urls import path
from .views import course_details, teacher_list

urlpatterns = [
    path('course/<int:course_id>/', course_details.as_view(), name='courses'),
    path('teachers/', teacher_list.as_view(), name='teachers'),
]





