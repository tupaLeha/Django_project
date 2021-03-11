from django.urls import path
from myapp.views import form_view, new_form, gtfo, well_done, login_page


urlpatterns = [
    path('form-url/', form_view, name='form-view'),
    path('new_form/', new_form, name='new_form'),
    path('gtfo/', gtfo, name='gtfo'),
    path('well_done/', well_done, name='well_done'),
    path('login_page/', login_page, name='login_page')

]
