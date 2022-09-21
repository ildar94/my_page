from django.urls import path
from . import views


urlpatterns = [
    path('<int:sign_zodiac>', views.get_info_about_zign_zodiac_is_number),
    path('<str:sign_zodiac>', views.get_info_about_zign_zodiac),
    # path('leo/', views.leo),
    # path('scorpio/', views.scorpio),

]