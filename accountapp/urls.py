from django.urls import path

from accountapp.views import hello_world

#실제 주소를 안적어도 accountapp으로 바로 라우팅 하기 위해 썼음
app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]