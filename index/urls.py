from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import Privocy, Catalog, About, Contact

app_name = "index"

urlpatterns = [
    path('', views.post_new, name="index"),
    path('privocy', Privocy.as_view(), name="privocy"),
    path('catalog', Catalog.as_view(), name="catalog"),
    path('about', About.as_view(), name="about"),
    path('contact', Contact.as_view(), name="contact"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
