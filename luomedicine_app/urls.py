from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("medicine/", views.medicine, name="medicine"),
    path("food/", views.luo_food, name="luofoods"),
    path("religion/", views.luo_religion, name="religion"),
    path("ceremonies/", views.luo_ceremonies, name="ceremonies"),
    path("plant/<int:id>/", views.get_medicinal_plant_by_id, name="plant"),
    path("subscribe/", views.subscribe, name="subscribe"),
    path('success/', views.success, name='success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# default: "Django Administration"
admin.site.site_header = "LUO MEDICINE"
# default: "Site administration"
admin.site.index_title = "LUO MEDIC"
# default: "Django site admin"
admin.site.site_title = "HTML title from administration"
