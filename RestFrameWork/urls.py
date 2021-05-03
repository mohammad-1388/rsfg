from django.urls import path
from RestFrameWork.views import GetAllData, GetFavData, EditFavData, PostModelData, PostData, SearchData, DeleteData, \
    get_all_data, set_data

app_name = "RestFrameWork"

urlpatterns = [
    path('get-all-data/', GetAllData.as_view(), name="getAllData"),
    path('get-fav-data/', GetFavData.as_view(), name="getFavData"),
    path('edit-fav-data/<int:pk>/', EditFavData.as_view(), name="editFavData"),
    path('post-model/', PostModelData.as_view(), name="PostModelData"),
    path('post-data/', PostData.as_view(), name="PostData"),
    path('set-data/', set_data, name="setData"),
    path('search/', SearchData.as_view(), name="SearchData"),
    path('delete/<int:pk>', DeleteData.as_view(), name="DeleteData"),
    path('all-data/', get_all_data, name="get_all_data"),
]
