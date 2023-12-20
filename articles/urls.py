from django.urls import path
from . import views
urlpatterns = [
    path('',views.articles_list),
    # path('<slug>/',views.article_detail),
    path('extract/', views.extract_text_from_pdf),
    path('search/',views.search_view),
    path('test/',views.tagged_post_view)

]