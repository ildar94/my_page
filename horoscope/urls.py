from django.urls import path,  register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.My_converter, 'float')




urlpatterns = [
    path('', views.index),
    path('<yyyy:sign_zodiac>', views.yyyy_number),
    path('<int:sign_zodiac>', views.get_info_about_zign_zodiac_is_number),
    path('float:sign_zodiac', views.float_number),
    path('<str:sign_zodiac>', views.get_info_about_zign_zodiac, name="zodiac_name"),
    # path('leo/', views.leo),
    # path('scorpio/', views.scorpio),

]