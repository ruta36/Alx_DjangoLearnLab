from django.urls import path
from .views import BookList
pythonCopy codefrom django.urls import path
from .views import BookListCreateAPIView

urlpatterns = [
    path("api/books", views.BookListCreateAPIView.as_view(), name="book_list_create"),
]

urlpatterns = [
     path('admin/', admin.site.urls),  
    path('api/', include('api.urls')),
    # path('api/books', BookList.as_view(), name='book-list'),
]