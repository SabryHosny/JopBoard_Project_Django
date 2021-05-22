from django.urls import include, path
from . import views
from . import api

app_name = 'jop_appppppppppp'
urlpatterns = [
    # VIEWs
    path('', views.jop_list, name='jobs'),
    path('add', views.add_job, name='add_job'),
    path('<str:slug>', views.jop_detail, name='job_detailsssssss'),

    # APIs :
    # Function based
    path('api/jobs', api.job_list_api, name='job_list_api'),
    path('api/jobs/<int:id>', api.job_detail_api, name='job_detail_api'),

    # class based
    path('api/v2/jobs', api.JopListApi.as_view(), name='job_list_api'),
    path('api/v2/jobs/<int:id>', api.JobDetail.as_view(), name='job_detail_api'),
]
