from django.urls import path
from .views import BookList


urlpatterns = [
    # path('admin/', admin.site.urls),  
    # path('api/', include('api.urls')),
    path('books', BookList.as_view(), name='book-list'),
]